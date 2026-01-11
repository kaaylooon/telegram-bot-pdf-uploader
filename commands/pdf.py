import json
from telegram import ForceReply, Update 
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
import html
from pathlib import Path

import os

from telegram.helpers import escape_markdown

BASE_DIR = Path(__file__).resolve().parents[1]

PDF_BASE_DIR = Path(os.getenv("PDF_BASE_DIR"))

if not os.getenv("PDF_BASE_DIR"):
	raise RuntimeError(
		"PDF_BASE_DIR is not defined.\n\n"
        "Example:\n"
        "export PDF_BASE_DIR=/path/of/the/pdfs")

PDF_INDEX_PATH = BASE_DIR / "pdf_index.json"

with open(PDF_INDEX_PATH, encoding="utf-8") as f:
	PDF_INDEX = json.load(f)

async def pdf_search(update: Update, context: ContextTypes.DEFAULT_TYPE):
	if not context.args:
		await update.message.reply_text("→ /pdf <title>", reply_markup=ForceReply(selective=True))
		return

	title = " ".join(context.args).lower()

	results = [p for p in PDF_INDEX if title in p["name"].lower()]

	if not results:
		await update.message.reply_text("No PDF was found. Try again.")
		return

	msg = (
		"🔍 <b> • List of PDFs found</b>\n\n"
	)

	lines = []
	for p in results[:20]:
		pid = html.escape(str(p["id"]))
		pname = html.escape(p["name"])
		lines.append(f"<b>#{pid}</b> • {pname}")

	msg += "<blockquote>" + "\n".join(lines) + "\n</blockquote>" + "\nSelect the PDF according to the ID:"

	await update.message.reply_text(
		msg,
		parse_mode=ParseMode.HTML
	)

	await update.message.reply_text(
		"→ /getpdf &lt;id&gt;",
		reply_markup=ForceReply(selective=True),
		parse_mode=ParseMode.HTML
	)


async def get_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
	if not context.args:
		await update.message.reply_text("→ /getpdf <id>", reply_markup=ForceReply(selective=True))
		return

	try:
		pdf_id = int(context.args[0])
	except ValueError:
		return

	pdf = next((p for p in PDF_INDEX if p['id'] == pdf_id), None)

	if not pdf:
		await update.message.reply_text("No PDF was found. Try again.")
		return

	path = PDF_BASE_DIR / pdf["path"]
	if not path.exists():
		await update.message.reply_text("The file could not be found. Either the path is not defined correctly, or the file does not exist.")
		return

	await update.message.reply_text("<blockquote><b>Uploading...</b></blockquote>",
		parse_mode=ParseMode.HTML)

	await update.message.reply_document(
		document=open(path, "rb"),
		filename=path.name,
		caption=f"<blockquote><b>{path.name}</b></blockquote>",
		parse_mode=ParseMode.HTML
				)