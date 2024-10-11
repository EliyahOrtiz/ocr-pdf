<div align="center">

[![logo](assets/wide.webp)](https://github.com/ipitio/ocr-pdf)

# OCR PDF

**To find or not to find, that is the question**

---

[![downloads](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fipitio.github.io%2Fbackage%2Fipitio%2Focr-pdf%2Focr-pdf.json&query=%24.downloads&logo=github&logoColor=959da5&labelColor=333a41&label=pulls)](https://github.com/arevindh/pihole-speedtest/pkgs/container/pihole-speedtest) [![build](https://github.com/ipitio/ocr-pdf/actions/workflows/publish.yml/badge.svg)](https://github.com/ipitio/ocr-pdf/actions/workflows/publish.yml)

</div>

Make your unsearchable PDFs searchable with the help of automation, virtualization, and a pretrained deep learning model!

The core logic resides in a Python script that gets all the PDFs in `todo`, converts their pages to OCR'd images with Google's LSTM-based OCR engine Tesseract, and combines these into new PDFs in `done`. The Bash script installs the necessary libraries for and runs the Python script in a virtual environment. Docker sets up another virtual environment within which it installs Python, Tesseract, and Poppler and calls the Bash script. The GitHub Actions workflow starts the Docker container in yet a third virtual layer, making use of the cloud.

You choose how much of the ETL pipeline you want to automate and virtualize.

## Fast Start

It's as easy as 1, 2, 3! Get up and going in no time with these options:

### Google Colab

Are you on mobile or simply want an easy and seamless experience?

1. Open [the app](https://colab.research.google.com/drive/1yss_oypuRisb29_SnqLGgA759slQzNry) in your browser
2. Select `Runtime > Run all` and follow the instructions
3. Find the OCR'd PDFs in your [Google Drive](https://drive.google.com/drive/my-drive)`/ocr-pdf`

### Docker Image

If you want to avoid cloning the repo and building an image, just use mine:

1. Install Docker and Compose, such as with Docker Desktop
2. In a new folder, copy the contents of `compose-prod.yml` to `compose.yml` and put your PDFs in `pdf/todo`
3. Run `docker compose up` inside that folder to OCR the PDFs and move them into `pdf/done`

## Quick Start

It's as easy as 1, 2, 3, 4, 5! Once you complete the following steps, you'll find the OCR'd PDFs in `pdf/done`.

1. First (fork and) clone this repo
2. `cd` into it and put your PDFs in `pdf/todo`
3. Choose one of the following options:

### Bare Metal

Are you on Linux and want to set up everything yourself?

1. Install Python 3, Tesseract, and Poppler
2. Run `bash src/predict.sh pdf`

### Docker Build

If you aren't on Linux, or want to avoid polluting your system:

1. Install Docker and Compose, such as with Docker Desktop
2. Run `docker compose up`

### GitHub Actions

If you forked and cloned your fork, I suggest you:

1. Push the bad PDFs to GitHub
2. Pull the good ones from it

```bash
git add -- *.pdf
git commit -m "Add PDFs"
git push
# wait for the magic to happen (if the job fails, rerun it)
git pull
```
