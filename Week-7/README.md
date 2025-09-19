# 📊 Data Analysis Assignment

## Objective
The purpose of this assignment is to:
- Load and explore a dataset using **Pandas**.
- Perform basic descriptive statistics and groupings.
- Visualize the data using **Matplotlib** and **Seaborn**.

---

## Dataset
The dataset used is **CRMreport.csv**, which contains customer subscription, billing, and package details.

### Columns
- **SUBS** – Subscriber ID  
- **BILLCYCLE** – Billing cycle  
- **INSTALLDATE** – Date the service was installed  
- **NAME** – Customer name  
- **FRANCHISE** – Franchise or branch handling the customer  
- **CUSTOMER STATUS / status now** – Current customer status  
- **NODE / M.NODE** – Network node information  
- **Area** – Customer’s geographic area  
- **PKG** – Package subscribed to  
- **SEG** – Segment classification  
- **TEAM** – Sales or support team  
- **PAS** – (Field in dataset, can be used if relevant)  
- **DAYS** – Number of subscription days  
- **BAND** – Bandwidth plan or capacity  

---

## Project Structure
```
data-analysis-assignment/
│
├── data/
│ └── CRMreport.csv # Dataset
│
├── notebooks/
│ └── analysis.ipynb # Jupyter notebook with full analysis
│
├── scripts/
│ └── analysis.py # Python script version of analysis
│
├── outputs/ # Saved charts
│ ├── line.png
│ ├── bar.png
│ ├── histogram.png
│ └── scatter.png
│
└── README.md
```


---

## Tasks Completed

### Task 1: Load & Explore Dataset
- Imported CSV into Pandas DataFrame.
- Displayed first rows with `.head()`.
- Checked data types, missing values, and duplicates.
- Cleaned column names for consistency.

### Task 2: Basic Data Analysis
- Generated descriptive statistics using `.describe()`.
- Grouped data (e.g., average **DAYS per package**).
- Observed trends across packages and franchises.

### Task 3: Visualizations
1. **Line Chart** – Installations over time  
2. **Bar Chart** – Average `DAYS` per package  
3. **Histogram** – Distribution of `DAYS`  
4. **Scatter Plot** – Relationship between `DAYS` and `BAND`  

All charts were customized with titles, labels, and saved to the `outputs/` folder.

---

## Findings / Observations
- Customer subscription days vary significantly across different packages.  
- Some packages show longer retention, suggesting stronger customer loyalty.  
- Installation counts over time highlight possible growth or seasonal dips.  
- The scatter plot of `DAYS` vs `BAND` indicates potential clusters (heavy users vs casual users).  

---

## How to Run

### Using Jupyter Notebook
1. Navigate to the `notebooks/` folder.
2. Open `analysis.ipynb` in Jupyter Lab/Notebook.
3. Run cells step by step.

### Using Python Script
1. Navigate to the `scripts/` folder.
2. Run:
   ```bash
   python3 analysis.py
