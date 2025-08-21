# AI Developer Starter Project

This repository is a clean starting point for your AI/ML learning in VS Code.

## Structure
- `notebooks/` – Jupyter notebooks for experiments
- `src/` – Python modules and scripts
- `data/` – Datasets (git-ignore large files in real projects)
- `models/` – Saved models, checkpoints
- `reports/` – Figures, exports, notes

## Quickstart
```bash
# 1) Create and activate a virtual environment (Linux/macOS)
python3 -m venv .venv
source .venv/bin/activate

# Windows PowerShell
# python -m venv .venv
# .venv\Scripts\Activate.ps1

# 2) Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 3) Launch VS Code from this folder (optional)
# code .

# 4) Run Jupyter in VS Code
# - Open notebooks/Week1_Math_NumPy.ipynb
# - Select the .venv interpreter as the Jupyter kernel
```

## Notes
- Commit small/clean datasets only. Use `.gitignore` for large files.
- Keep experiments in notebooks, move reusable code into `src/`.
