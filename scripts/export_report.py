import subprocess
import os

# Paths
NOTEBOOK_PATH = "notebooks/eda_report.ipynb"
OUTPUT_HTML = "reports/eda_report.html"
OUTPUT_PDF = "reports/eda_report.pdf"

# Make sure reports folder exists
os.makedirs("reports", exist_ok=True)

# Export to HTML
subprocess.run([
    "jupyter", "nbconvert", NOTEBOOK_PATH,
    "--to", "html", "--output", OUTPUT_HTML
])

# Export to PDF (requires LaTeX installed!)
subprocess.run([
    "jupyter", "nbconvert", NOTEBOOK_PATH,
    "--to", "pdf", "--output", OUTPUT_PDF
])

print("✅ Export completed: HTML & PDF saved in reports/")
