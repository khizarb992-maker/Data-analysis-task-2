# 📊 Global Superstore Business Dashboard

An interactive business intelligence dashboard built with **Streamlit** and **Plotly**, powered by the Global Superstore dataset. Filter data by region, category, and sub-category to explore sales and profit insights in real time.

---

## 🖥️ Features

- **KPI Metrics** — Instant view of total sales and total profit based on active filters
- **Top 5 Customers** — Bar chart of highest-value customers by sales
- **Sales by Category** — Pie chart showing category-wise revenue distribution
- **Sales by Region** — Bar chart comparing performance across regions
- **Sidebar Filters** — Dynamically filter all charts by Region, Category, and Sub-Category

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Streamlit](https://streamlit.io/) | Web app framework |
| [Pandas](https://pandas.pydata.org/) | Data loading and transformation |
| [Plotly Express](https://plotly.com/python/plotly-express/) | Interactive charts |



---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/superstore-dashboard.git
cd superstore-dashboard
```

### 2. Install dependencies

```bash
pip install streamlit pandas plotly
```

### 3. Add your dataset

Place your `superstore.csv` file in the project root (or update the file path in `dashboard.py`):

```python
df = pd.read_csv("superstore.csv", encoding="latin1")
```

### 4. Run the app

```bash
streamlit run dashboard.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 📋 Dataset Requirements

The CSV file must contain the following columns:

| Column | Description |
|--------|-------------|
| `Sales` | Revenue per order row |
| `Profit` | Profit per order row |
| `Region` | Geographic region |
| `Category` | Product category |
| `Sub.Category` | Product sub-category |
| `Customer.Name` | Customer full name |
