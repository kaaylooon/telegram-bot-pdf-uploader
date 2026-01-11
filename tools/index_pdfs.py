from pathlib import Path
import json
import os

PDF_ROOT = Path(os.getenv("PDF_BASE_DIR"))
index = []
i = 1

for pdf in PDF_ROOT.rglob("*.pdf"):
    index.append({
        "id": i,
        "name": pdf.stem.lower(),
        "path": str(pdf)
    })
    i += 1

BASE_DIR = Path(__file__).resolve().parent.parent
INDEX_PATH = BASE_DIR / "pdf_index.json"

with INDEX_PATH.open("w", encoding="utf-8") as f:
    json.dump(index, f, indent=2, ensure_ascii=False)

print(f"{len(index)} PDFs")
