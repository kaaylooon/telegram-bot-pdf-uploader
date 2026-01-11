from telegram import Update
from telegram.ext import Application, CommandHandler

from commands.misc import start, help_command, ping
from commands.pdf import pdf_search, get_pdf

import logging
import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("TELEGRAM_BOT_TOKEN")
if not KEY:
	raise RuntimeError("TELEGRAM_BOT_TOKEN is not defined.")

logging.basicConfig(
	format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

os.environ["HTTPX_ONLY_IPV4"] = "1"

def main() -> None:
	application = Application.builder().token(KEY).build()

	application.add_handler(CommandHandler("start", start))
	application.add_handler(CommandHandler("help", help_command))
	application.add_handler(CommandHandler("ping", ping))

	application.add_handler(CommandHandler("pdf", pdf_search))
	application.add_handler(CommandHandler("getpdf", get_pdf))
	

	application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
	main()