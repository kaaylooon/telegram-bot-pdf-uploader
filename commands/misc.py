from telegram import ForceReply, Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

# Base commands

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	user = update.effective_user
	await update.message.reply_html(
		rf"Hello, {user.mention_html()}.",
		reply_markup=ForceReply(selective=True),
	)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	await update.message.reply_text(
		f" • /pdf <title> - List of the PDFs found\n\n • /getpdf <id> - Download", parse_mode=ParseMode.MARKDOWN_V2)

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	if update.effective_user.is_bot:
		return

	await update.message.reply_text("*Pong!*", parse_mode=ParseMode.MARKDOWN_V2)