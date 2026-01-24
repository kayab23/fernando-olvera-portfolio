# Scripts

This folder contains utility scripts used to generate and process CVs and PDFs for the portfolio.

## add_watermark_to_pdfs.py

- Purpose: Add a visible watermark to all PDF files inside `website-portfolio/assets/certs` and write results into `website-portfolio/assets/certs/watermarked`.
- Usage:

```powershell
& .\.venv\Scripts\Activate.ps1
python scripts\add_watermark_to_pdfs.py
```

- Requirements: see `requirements.txt` in repo root.

## Contributing
- Keep utility scripts small and documented.
- If a script is experimental, prefix with `dev_` or place in `scripts/dev/`.
