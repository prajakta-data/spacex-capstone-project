# 🚀 SpaceX Falcon 9 Launch Analysis – Data Science Capstone Project

## 📌 Overview

This project analyzes **SpaceX Falcon 9 launch records** to determine the factors that influence launch success.
It includes full end-to-end data science workflow:

* Data collection
* Data wrangling
* Exploratory data analysis (EDA)
* SQL analytics
* Interactive visual analytics (Folium + Plotly Dash)
* Classification modeling (Prediction)
* Final presentation

This project is completed as part of the **IBM Data Science Professional Certificate** Capstone.

---

## 📁 Project Structure

```
SpaceX-Capstone-Project/
│── notebooks/
│     ├── data_wrangling.ipynb
│     ├── EDA_visuals.ipynb
│     ├── SQL_analysis.ipynb
│     ├── folium_map.ipynb
│     ├── dash_dashboard.ipynb
│     ├── machine_learning.ipynb
│── dash_app.py
│── dataset_part_1.csv
│── dataset_part_2.csv
│── dataset_part_3.csv
│── spacex_launch_geo.csv
│── spacex-data-wrangled.csv
│── presentation.pdf
│── README.md
```

---

## 🗂 Data Sources

Data was collected from:

* **SpaceX REST APIs**
* **Wikipedia Falcon 9 records**
* **Provided CSV datasets (IBM Skills Network)**

Data was cleaned and processed using pandas and Numpy.

---

## 🧹 Data Wrangling

Key steps include:

* Handling missing values
* Renaming and restructuring columns
* Filtering Falcon 9 launches
* One-hot encoding categorical features
* Normalizing numerical features

---

## 📊 Exploratory Data Analysis (EDA)

Performed using:

* **Matplotlib**
* **Seaborn**
* **SQL queries**
* **Box plots, hist plots, scatter plots**
* **Payload vs Success**
* **Launch site performance**

---

## 🗺 Interactive Visual Analytics

### ✔ Folium Map

Shows:

* Launch sites
* Success/Failure markers
* Distance to coastline, highways, railways, cities

### ✔ Plotly Dash Dashboard

Includes:

* Launch site dropdown
* Pie chart for success rates
* Scatter plot for Payload vs Outcome
* Interactive filtering

---

## 🤖 Machine Learning / Predictive Modeling

Models used:

* Logistic Regression
* Support Vector Machine
* Decision Tree
* K-Nearest Neighbors

Techniques:

* Hyperparameter tuning (GridSearchCV)
* Standard Scaling
* Train-Test Split
* Accuracy Evaluation
* Confusion Matrix

---

## 📝 Final Presentation

A full slide deck summarizing:

* Executive summary
* Introduction
* Methodology
* EDA results
* SQL findings
* Interactive analytics
* Classification model results
* Conclusion

---

## 🧠 Key Findings

* **Site with the most successful launches:** CCAFS SLC-40
* **Highest success rate:** KSC LC-39A
* **Best payload range:** Medium (2000–4000 kg)
* **Worst payload range:** Very high payloads
* **Best booster version:** FT

---

## 🧩 Tools & Technologies

* Python
* Pandas
* NumPy
* SQL
* Plotly & Dash
* Folium
* Matplotlib / Seaborn
* Scikit-learn
* GitHub

---

## 📬 Contact

For any questions about the project, feel free to reach out:
Prajakta Godhane

