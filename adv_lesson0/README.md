# Lesson 0 - Advanced Prep Lesson

## Ch2 Virtual Environments

- **Self-contained** environment
- `python3 -m venv venv_name`
- Activation
  - `source venv_name/bin/activate`
- Deactivation
  - `deactivate`

## Ch3 PIP

- Installing specific versions
  - `pip install package==1.1.1`
- **Freezing** to get snapshot of packages
  - `pip freeze > requirements.txt`
  - `pip install -r requirements.txt`

## Ch4 Jupyter Notebook

- **Cells**
  - A code cell contains code to be executed
  - A markdown cell contains text to be formatted
- **Kernels**
  - The venv to run the notebook
  - Kernel **state persists** over time and between cells
