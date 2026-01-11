# Telegram PDF Uploader Bot

A Python-based Telegram bot designed to **index, search, and upload PDF files** from large local collections in a simple and efficient way.

This project focuses on **automation, productivity, and clarity**, avoiding unnecessary abstractions or heavy frameworks.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/kaaylooon/telegram-bot-pdf-uploader.git
cd telegram-bot-pdf-uploader
 
---

### Virtual environment

python -m venv venv
source venv/bin/activate

### Environment Variables

```bash
export TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"
```bash
export PDF_BASE_DIR="absolute/path/to/your/pdfs"

## Usage

```base
python main.py

## Technologies

- python3
- python-telegram-bot

## PDF

> The pdf_index.json file is generated automatically and should not be edited, generate yours with tools/index_pdfs.py