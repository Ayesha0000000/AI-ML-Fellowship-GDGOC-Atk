<div align="center">

<!-- HEADER BANNER -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=AI%20%2F%20ML%20Fellowship%202026&fontSize=42&fontColor=ffffff&fontAlignY=38&desc=GDGOC%20Attock%20%E2%80%A2%20From%20Zero%20to%20ML%20Engineer&descAlignY=60&descSize=18&descColor=a78bfa&animation=twinkling"/>

<br/>

<!-- BADGES ROW 1 -->
<img src="https://img.shields.io/badge/Status-Completed%20%E2%9C%94-22c55e?style=for-the-badge&labelColor=0f0c29"/>
<img src="https://img.shields.io/badge/Duration-8%20Weeks-a78bfa?style=for-the-badge&labelColor=0f0c29"/>
<img src="https://img.shields.io/badge/Projects-6%20Built-38bdf8?style=for-the-badge&labelColor=0f0c29"/>
<img src="https://img.shields.io/badge/Fellowship-GDGOC%20ATK-f97316?style=for-the-badge&labelColor=0f0c29"/>

<br/><br/>

<!-- TECH BADGES -->
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white"/>
<img src="https://img.shields.io/badge/Matplotlib-11557c?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white"/>
<img src="https://img.shields.io/badge/Deep%20Learning-FF6F00?style=flat-square&logo=tensorflow&logoColor=white"/>

</div>

---

## 🧠 What Is This?

> **This repository is my complete AI/ML learning journey** documented across 8 weeks of the **GDGOC ATK AI-ML Fellowship 2026** — a structured program that took me from Python fundamentals all the way to building and evaluating deep learning models.

Every folder here represents a real week of work — assignments, experiments, mini-projects, and the lessons I learned by doing. This is not just code; it's a record of growth.

---

## 🗺️ Journey Overview

```
WEEK 1 ──▶ WEEK 2 ──▶ WEEK 3-4 ──▶ WEEK 5 ──▶ WEEK 6 ──▶ WEEK 7 ──▶ WEEK 8
Python      EDA         IoT Team     ML Models   Regression  Clustering   Deep
Basics      Titanic     Project      & Eval      Housing     MBA          Learning
  🐍          📊          🌱            🤖           🏠           🛒           🧬
```

---

## 📅 Weekly Breakdown

<details>
<summary><b>🐍 Week 1 — Python Foundations</b></summary>

### Core Concepts Covered
| Topic | Details |
|-------|---------|
| Variables & Data Types | int, float, str, bool, list, dict, tuple |
| Control Flow | if/elif/else, for loops, while loops |
| Functions | Defining, calling, parameters, return values |
| Logic Building | Simple programs to develop algorithmic thinking |

**Key Takeaway:** Learned to think like a programmer — breaking problems into small logical steps.

</details>

---

<details>
<summary><b>📊 Week 2 — Exploratory Data Analysis (Titanic Dataset)</b></summary>

### What I Did
- Loaded and inspected the classic Titanic dataset
- Handled **missing values** in `Age`, `Cabin`, and `Embarked` columns
- Visualized survival rates by gender, class, and age
- Discovered feature correlations using heatmaps

### Tools Used
`pandas` · `matplotlib` · `seaborn`

### Key Insight
> **Women in 1st class had the highest survival rate (~97%)**. Data confirms the "women and children first" policy — and shows how EDA reveals stories hidden in numbers.

</details>

---

<details>
<summary><b>🌱 Week 3 & 4 — Automated Plant Watering System (Team Project)</b></summary>

### Project Overview
Designed and implemented a **logic-based automated plant watering system** as part of a team challenge.

### What We Built
- System that checks soil moisture conditions
- Automated trigger logic for water pump activation
- Threshold-based decision making

### What I Learned
- Real-world problem decomposition
- Team collaboration and task division
- Translating physical systems into code logic

</details>

---

<details>
<summary><b>🤖 Week 5 — Machine Learning & Model Evaluation</b></summary>

### Topics Covered

**Algorithms:**
- ✅ Logistic Regression (classification)
- ✅ Data preprocessing pipelines
- ✅ Train/test split strategies

**Model Evaluation Metrics:**

| Metric | What It Measures |
|--------|-----------------|
| **Accuracy** | Overall correctness |
| **Precision** | Quality of positive predictions |
| **Recall** | Coverage of actual positives |
| **F1-Score** | Harmonic balance of precision & recall |

**Key Concepts:**
- 🔴 Overfitting — model memorizes training data
- 🔵 Underfitting — model too simple to learn
- ⚖️ Bias-Variance Tradeoff

</details>

---

<details>
<summary><b>🏠 Week 6 — Housing Price Prediction (Regression)</b></summary>

### Objective
Build a regression model to predict house prices based on features like size, location, and number of rooms.

### Pipeline

```
Raw Data → Feature Selection → Train/Test Split → Model Training → Evaluation
```

### Metrics Used
- **MAE** — Mean Absolute Error
- **MSE** — Mean Squared Error  
- **R² Score** — Goodness of fit

**Outcome:** Built a model that predicts house prices with meaningful accuracy and understood how feature engineering impacts performance.

</details>

---

<details>
<summary><b>🛒 Week 7 — Market Basket Analysis (Unsupervised Learning)</b></summary>

### What Is Market Basket Analysis?
A technique used by retailers to discover which products are frequently bought together — the engine behind *"Customers also bought..."*

### Concepts Applied

| Metric | Formula | Meaning |
|--------|---------|---------|
| **Support** | freq(A∪B) / N | How often the itemset appears |
| **Confidence** | freq(A∪B) / freq(A) | Likelihood B is bought with A |
| **Lift** | Confidence / Support(B) | Strength of the association |

**Key Finding:** Discovered strong purchasing associations that would be invisible without algorithmic pattern mining.

</details>

---

<details>
<summary><b>🧬 Week 8 — Deep Learning Fundamentals</b></summary>

### Concepts Explored

```
Input Layer → Hidden Layers → Output Layer
     ↕              ↕               ↕
  Features     Activations      Predictions
```

**Topics Covered:**
- 🧠 Perceptron and neural network architecture
- 🔁 Forward propagation
- 🔙 Backpropagation and gradient descent
- ⚡ Activation functions (ReLU, Sigmoid, Softmax)
- 📉 Loss functions and optimization

**Applications Explored:** Image classification, pattern recognition, sequential data modeling.

</details>

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Tools |
|-------|-------|
| **Language** | Python 3.x |
| **Data** | NumPy, Pandas |
| **Visualization** | Matplotlib, Seaborn |
| **ML** | Scikit-learn |
| **Environment** | Jupyter Notebook |
| **Deep Learning** | Neural Networks (from scratch + frameworks) |

</div>

---

## 📁 Repository Structure

```
📦 AI-ML-Fellowship-GDGOC-Atk
│
├── 📂 Week-1_Python-Basics/
│   └── fundamentals, loops, functions, logic programs
│
├── 📂 Week-2_Titanic-EDA/
│   └── EDA notebook, visualizations, insights
│
├── 📂 Week-3-4_Plant-Watering-System/
│   └── system logic, automation code, team notes
│
├── 📂 Week-5_Machine-Learning/
│   └── logistic regression, preprocessing, evaluation
│
├── 📂 Week-6_Housing-Price-Prediction/
│   └── regression model, feature selection, metrics
│
├── 📂 Week-7_Market-Basket-Analysis/
│   └── association rules, apriori, pattern mining
│
└── 📂 Week-8_Deep-Learning/
    └── neural networks, backpropagation, experiments
```

---

## 🏆 Key Learning Outcomes

```
✦ Strong Python foundation for data science
✦ EDA skills — turning raw data into insights
✦ End-to-end ML pipeline: data → model → evaluation
✦ Understanding of classification and regression
✦ Unsupervised learning and pattern discovery
✦ Introduction to neural networks and deep learning
✦ Real-world teamwork and project collaboration
```

---

## 📈 Growth Curve

```
Beginner ──────────────────────────────────── Practitioner
   │                                                │
Week 1        Week 4           Week 6          Week 8
Python      Team Project    ML Models +      Deep Learning
Variables   Automation      Regression       Neural Nets
   │                                                │
   └────────────── 8 Weeks of Growth ──────────────┘
```

---

## 🤝 Connect

<div align="center">

*Built with curiosity, consistency, and a lot of `print()` debugging.*

**GDGOC Attock | AI-ML Fellowship 2026**

[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com)

</div>

---

<div align="center">
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer"/>
</div>
