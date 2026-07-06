# 🎬 Creator Engagement & Watch-Time Predictive Engine

An end-to-end Machine Learning pipeline and interactive simulation platform designed to forecast YouTube video performance metrics using optimized gradient boosting architectures.

---

## 💻 Dashboard Interface Preview

Add your full Streamlit running interface screenshot right here to capture a viewer's attention immediately:
## Interactive Simulation Dashboard Workspace
<img width="1320" height="772" alt="image" src="https://github.com/user-attachments/assets/e5da4f08-121b-424a-8430-bdac7e1b4a82" />

<img width="1046" height="732" alt="image" src="https://github.com/user-attachments/assets/f0eab278-b525-40d6-bdf0-bb561b3933b4" />


---

## 🔄 Interactive Dashboard Architecture (Dynamic Simulations)
The frontend core utilizes a **dynamic simulation framework** where plots are recalculated and rendered live by the execution engine every single time a production slider parameter is updated by a user. These calculations map real-time hypothetical target variations:

1. **Dynamic Retention Decay Pathway:** Computes viewer audience drop-off over an interactive video timeline.
<img width="1012" height="656" alt="image" src="https://github.com/user-attachments/assets/a86e1856-bc3a-47a1-960f-44dc20e034f0" />

2. **Dynamic Proportional Engagement Density:** Evaluates ratios of user actions (Likes/Comments/Shares) calculated dynamically relative to specific reach volumes.
<img width="1102" height="501" alt="image" src="https://github.com/user-attachments/assets/e40602b0-a14a-46a6-8949-97d107313702" />

---

## 📊 Pipeline Evaluation Foundations (Static Analytics)
While the frontend user interface focuses on real-time modeling, the underlying machine learning pipeline automatically executes complete Exploratory Data Analysis (EDA) during training. These **static charts** represent absolute snapshot insights captured directly from the historical baseline training dataset and do not modify based on UI inputs:

### 📉 Feature Performance Matrix

| 📊 1. Static Watch-Time Distribution Range | 📉 2. Static CTR vs. Watch Time Linearity |
| :---: | :---: |
| ![Distribution Chart](graph_1_distribution.png) | ![Scatter Plot](graph_2_scatter.png) |

| 🌡️ 3. Static Feature Contribution Heatmap (Pearson Correlation Matrix) |
| :---: |
| ![Heatmap Matrix](graph_3_heatmap.png) |

---

## 🛠️ Technology Stack & Dependencies
* **Core Language:** Python
* **Machine Learning Engine:** XGBoost Regressor, Scikit-Learn
* **Data Processing & Analytics:** Pandas, NumPy
* **Interactive UI Layer:** Streamlit framework
* **Data Visualization:** Matplotlib, Seaborn

---

## 🏃‍♂️ Local Installation & Setup Guide

Follow these steps to deploy the application environment locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/apoorva-iu/YouTube-Video-Performance-Predictor.git
   cd youtube_analytics

2. **Install Required Runtime Libraries:**
   ```bash
   pip install -r requirements.txt

3 **Launch the Interactive Dashboard:**
   ```bash
   streamlit run app.py

The local server will automatically initialize in your default web browser at http://localhost:8501.

Developed by Apoorva I U as an automated machine learning evaluation framework.

   
