# trading-operations-monitoring-demo

This is a demo project for a Trading Operations Analyst role. 
It simulates trading data, performs basic portfolio and risk analysis, and visualizes key metrics including:

- Total trading volume per symbol
- Net position per symbol
- Profit and Loss (PnL) per symbol
- Large trades (highlighting unusual transaction sizes)

## Project Structure

- `src/` : Python scripts
  - `generate_data.py` : Generates sample trading data
  - `analysis.py` : Performs analysis and generates visualizations
- `data/` : CSV files containing simulated trades
- `output/` : Generated plots (PNG)
- `.gitignore` : Files to ignore (if any)

## Requirements

- Python 3.10+
- pandas, numpy, matplotlib, seaborn

## Run

1. Create virtual environment (optional but recommended):

```bash
conda create -n tradingops python=3.10
conda activate tradingops
```

2. Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn
```

3. Run scripts:

```bash
python src/generate_data.py
python src/analysis.py
```

---

# 說明 / 注意事項

```markdown
## Notes

- The data is simulated for demonstration purposes
- Large trades chart highlights transactions with quantity > 3
- This project demonstrates basic trading operations analysis and visualization skills