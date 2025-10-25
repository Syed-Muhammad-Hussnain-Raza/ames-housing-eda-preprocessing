# Ames Housing EDA & Preprocessing

A structured data science project for performing **Exploratory Data Analysis (EDA)** and **Data Preprocessing** on the Ames Housing dataset.

---

## Project Setup Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Syed-Muhammad-Hussnain-Raza/ames-housing-eda-preprocessing.git
cd ames-housing-eda-preprocessing
```

---

### 2️⃣ Create and Activate a Virtual Environment

#### For Linux / macOS:
```bash
python3 -m venv ames_env
source ames_env/bin/activate
```

#### For Windows (PowerShell):
```bash
python -m venv ames_env
ames_env\Scripts\activate
```

---

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Up Environment Variables

Create a file named **`.env`** in the project root and add:
```bash
DATA_PATH=data/raw/AmesHousing.csv
PROCESSED_PATH=data/processed/AmesHousing_Cleaned.csv
FIGURES_PATH=reports/figures/
```

---

### 5️⃣ Launch Jupyter Notebook

```bash
jupyter notebook
```

Then open the first notebook:
```
notebooks/00_data_overview.ipynb
```

---

You are now ready to explore, preprocess, and analyze the **Ames Housing Dataset**.