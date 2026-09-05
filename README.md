# Nandyal GroundWater Level ML Forecasting & Quality Prediction System

Final Year Engineering Project — Machine Learning Approach for GroundWater Level Forecasting and Quantity Prediction in Nandyal District, AP.

---

## 🛠️ Step-by-Step Instructions to Run in VS Code

### Step 1: Open Project Folder in VS Code
1. Open **Visual Studio Code (VS Code)**.
2. Click **File** -> **Open Folder...** (or press `Ctrl + K, Ctrl + O`).
3. Select your project folder:
   `C:\Users\pafro\OneDrive\Desktop\GrondWaterLavel`
4. Click **Select Folder**.

---

### Step 2: Open Integrated Terminal in VS Code
1. Click **Terminal** in the top menu bar -> **New Terminal** (or press `Ctrl + ~` or `Ctrl + Shift + \``).
2. Ensure your terminal prompt shows the project directory path.

---

### Step 3: Install Required Python Libraries
Run the following command in the VS Code terminal to ensure all required libraries are installed:

```bash
pip install pandas numpy scikit-learn xgboost statsmodels flask matplotlib openpyxl
```

---

### Step 4: Run Machine Learning Pipeline Script
Train all machine learning models (Random Forest, SVM, Decision Tree, ANN, XGBoost & Ensemble) and process the dataset by running:

```bash
python run_pipeline.py
```

*Output:*
```text
=========================================================
Starting Nandyal GroundWater Level ML Pipeline Execution...
Batch 18 Project: RF, SVM, DT, ANN & Water Quality Engine
=========================================================
Pipeline finished successfully!
```

---

### Step 5: Start the Web Dashboard Application
Start the Flask web backend server by running:

```bash
python app.py
```

*Output:*
```text
Starting Flask Nandyal HydroML Server...
 * Running on http://127.0.0.1:5000
```

---

### Step 6: Open the Dashboard in Your Web Browser
1. Open Google Chrome, Microsoft Edge, or Firefox.
2. Navigate to:
   👉 **`http://127.0.0.1:5000`** (or `http://localhost:5000`)
3. Explore the Plotly interactive charts, model toggles, Day & Night mode, water quality assessment, and scenario simulator!

---

## 📁 Project Directory Structure

```text
GrondWaterLavel/
├── NANDYAL GW LEVELS.xlsx   # Real-time ground water level dataset
├── run_pipeline.py         # Main ML training & multi-step forecasting script
├── app.py                  # Flask Web Application backend server
├── src/                    # Source code modules
│   ├── data_loader.py       # Excel parser & cleaning
│   ├── feature_engineering.py # Lag & rolling features generator
│   ├── models.py            # ML models (RF, SVM, DT, ANN, XGBoost, Ensemble)
│   ├── evaluate.py          # Benchmark evaluation metrics (RMSE, MAE, R2)
│   ├── quantity_calculator.py# Dynamic aquifer volume (MCM) calculator
│   └── water_quality.py    # Hydro-chemical parameters & WQI index
├── templates/
│   └── index.html          # Dashboard HTML template with Plotly.js
└── static/
    ├── css/styles.css      # Day & Night mode glassmorphism styles
    └── js/app.js           # Plotly interactive client scripts
```
