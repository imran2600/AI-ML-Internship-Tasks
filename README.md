# Iris Dataset Exploration and Visualization  
This project demonstrates basic data exploration and visualization using Python’s pandas, matplotlib, and seaborn libraries on the classic Iris dataset. The goal is to uncover trends, distributions, and outliers in the data through statistical summaries and plots.

## 📌 Task Overview  
This project demonstrates **basic data exploration and visualization** using Python’s `pandas`, `matplotlib`, and `seaborn` libraries on the classic Iris dataset. The goal is to uncover trends, distributions, and outliers in the data through statistical summaries and plots.  

## 🛠️ Steps Completed  

### 1. **Data Loading & Inspection**  
   - Loaded the Iris dataset using `seaborn`.  
   - Inspected dataset structure with:  
     - `.shape` → Dimensions  
     - `.head()` → First 5 rows  
     - `.info()` → Data types and missing values  
     - `.describe()` → Summary statistics (mean, min, max, etc.)  

### 2. **Visualizations**  
   - **Scatter Plots**: Explored relationships between features (e.g., `sepal_length` vs `petal_length`).  
   - **Histograms**: Visualized distributions of individual features.  
   - **Box Plots**: Identified outliers and compared distributions across species.  

### 3. **Key Insights**  
   - Discovered distinct clusters for Iris species (`setosa`, `versicolor`, `virginica`) in petal measurements.  
   - Detected potential outliers in `sepal_width`.  

## 🛠️ Tools Used  
- Python  
- Libraries: `pandas`, `matplotlib`, `seaborn`  

## 📂 Files  
- `iris_analysis.ipynb`: Jupyter Notebook with full code and visualizations.  
- `README.md`: Project documentation (this file).  

## 🌟 How to Run  
1. Install dependencies:  
   ```bash
   pip install pandas matplotlib seaborn jupyter
