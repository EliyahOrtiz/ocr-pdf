"""
This script OCRs PDFs
"""

import gc
import os
import sys
from pathlib import Path

import fitz  # PyMuPDF
import pytesseract
from joblib import Parallel, delayed
from pdf2image import convert_from_path


def process_pdfs(base: Path = Path(".")):
    """
    Process all PDF files in "todo" and save the results in "done".

    :param base: The base directory containing the "todo" and "done" directories.
    """
    base.mkdir(exist_ok=True, parents=True)
    (base / "todo").mkdir(exist_ok=True, parents=True)
    (base / "done").mkdir(exist_ok=True, parents=True)

    def predict(input_file: Path, output_file: Path):
        relative_path = input_file.relative_to(base / "todo")
        print(f"Processing {relative_path}...")

        # Perform OCR on the images
        doc = fitz.open()

        for image in convert_from_path(input_file, dpi=150, fmt="jpeg"):
            doc.insert_pdf(
                fitz.open(
                    "pdf", pytesseract.image_to_pdf_or_hocr(image, extension="pdf")
                )
            )
            del image
            gc.collect()

        doc.save(output_file, garbage=4, deflate=True)
        doc.close()

        try:
            input_file.unlink()
        except:
            pass

        print(f"Processed {relative_path}")

    Parallel(n_jobs=-1)(
        delayed(predict)(Path(root) / file, Path(root.replace("todo", "done")) / file)
        for root, _, files in os.walk(base / "todo")
        for file in files
        if file.lower().endswith(".pdf")
    )

    # sequential:
    # for root, _, files in os.walk(base / "todo"):
    #    for file in files:
    #        if file.lower().endswith(".pdf"):
    #            input_file = Path(root) / file
    #            output_file = Path(root.replace("todo", "done")) / file
    #            predict(input_file, output_file)


if __name__ == "__main__":
    process_pdfs(Path(sys.argv[1]))
