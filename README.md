# Loan Analysis Project

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3127/)
[![Pandas](https://img.shields.io/badge/pandas-2.2-150458.svg?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/numpy-1.26-013243.svg?style=flat&logo=numpy&logoColor=white)](https://numpy.org)
[![Jupyter](https://img.shields.io/badge/jupyter-notebook-orange.svg?style=flat&logo=jupyter&logoColor=white)](https://jupyter.org)
[![Matplotlib](https://img.shields.io/badge/matplotlib-3.10-11557c.svg?style=flat)](https://matplotlib.org)
[![Seaborn](https://img.shields.io/badge/seaborn-0.13.2-7db0bc.svg?style=flat)](https://seaborn.pydata.org)

## Project Overview
Analysis of a large loan portfolio ($30.1B) from a major peer-to-peer lending platform that reveals significant opportunities for risk management improvement. The study identified critical risk patterns and developed data-driven solutions for enhancing loan decisioning.

**Key Findings:**
- Overall default rate: 13.05%
- High-risk grades (8.4% of portfolio) drive 31.1% of defaults
- 60-month terms show 60% higher defaults than 36-month terms
- Geographic variations exceed 15% default rates in highest-risk states

## Installation
```bash
pip install -r requirements.txt
```

## Project Structure
```
├── data/
│   ├── raw/       # Original loan data
│   ├── interim/   # Partially processed data
│   ├── cleaned/   # Cleaned dataset
│   └── processed/ # Fully processed data
├── notebooks/
│   ├── 1_data_cleaning.ipynb
│   ├── 2_feature_engineering.ipynb
│   ├── 3_exploratory_data_analysis.ipynb
│   └── 4_statistical_analysis.ipynb
├── src/
│   └── data/
│       └── make_dataset.py
└── docs/
    ├── technical.md
    ├── analysis.md
    └── implementation.md
```

## Quick Start
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run data pipeline:
   ```bash
   python src/data/make_dataset.py
   ```
3. Execute notebooks in sequence
4. View results in final notebook

## Documentation
For detailed documentation, see:
- [Technical Documentation](docs/technical.md) - Data overview and technical implementation
- [Analysis Results](docs/analysis.md) - Detailed findings and insights
- [Implementation Guide](docs/implementation.md) - Solutions and next steps