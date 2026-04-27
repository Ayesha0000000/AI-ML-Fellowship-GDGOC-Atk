<div align="center">

<!-- BADGES ROW 1 -->
<img src="https://img.shields.io/badge/Status-Completed%20%E2%9C%94-22c55e?style=for-the-badge&labelColor=0f0c29"/>
<img src="https://img.shields.io/badge/Duration-3%20Months-a78bfa?style=for-the-badge&labelColor=0f0c29"/>
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

## What Is This?

> **This repository is my complete AI/ML learning journey** documented across the **GDGOC ATK AI-ML Fellowship 2026** — a 3-month structured program that took me from Python fundamentals all the way to building a full-stack AI healthcare application.

Every folder here represents a real week of work — assignments, experiments, mini-projects, and the lessons I learned by doing. This is not just code; it's a record of growth.

---

## Journey Overview

```
WEEK 1 → WEEK 2 → WEEK 3-4 → WEEK 5 → WEEK 6 → WEEK 7 → WEEK 8 → WEEK 9 → FINAL PROJECT
Python    EDA      IoT Team   ML       Regression Clustering Deep     Gen AI   SAHARA
Basics    Titanic  Project    Models   Housing    MBA        Learning  & LLMs   (4 Weeks)
```

---

## Weekly Breakdown

<details>
<summary><b>Week 1 — Python Foundations</b></summary>

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
<summary><b>Week 2 — Exploratory Data Analysis (Titanic Dataset)</b></summary>

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
<summary><b>Week 3 & 4 — Automated Plant Watering System (Team Project)</b></summary>

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
<summary><b>Week 5 — Machine Learning & Model Evaluation</b></summary>

### Topics Covered

**Algorithms:**
- Logistic Regression (classification)
- Data preprocessing pipelines
- Train/test split strategies

**Model Evaluation Metrics:**

| Metric | What It Measures |
|--------|-----------------|
| **Accuracy** | Overall correctness |
| **Precision** | Quality of positive predictions |
| **Recall** | Coverage of actual positives |
| **F1-Score** | Harmonic balance of precision & recall |

**Key Concepts:**
- Overfitting — model memorizes training data
- Underfitting — model too simple to learn
- Bias-Variance Tradeoff

</details>

---

<details>
<summary><b>Week 6 — Housing Price Prediction (Regression)</b></summary>

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
<summary><b>Week 7 — Market Basket Analysis (Unsupervised Learning)</b></summary>

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
<summary><b>Week 8 — Deep Learning Fundamentals</b></summary>

### Concepts Explored

```
Input Layer → Hidden Layers → Output Layer
     ↕              ↕               ↕
  Features     Activations      Predictions
```

**Topics Covered:**
- Perceptron and neural network architecture
- Forward propagation
- Backpropagation and gradient descent
- Activation functions (ReLU, Sigmoid, Softmax)
- Loss functions and optimization

**Applications Explored:** Image classification, pattern recognition, sequential data modeling.

</details>

---

<details>
<summary><b>Week 9 — Generative AI & LLMs Sprint</b></summary>

**Duration:** 1 Week + Optional 1 Week Extension  
**Method:** Use → Improve → Understand → Build

### Topics Covered

**GAN Fundamentals**
- Simple GAN Implementation — built a basic GAN from scratch, understanding the Generator vs Discriminator training loop
- GANs for Image Generation — trained GAN on image datasets to generate realistic new images
- Data Augmentation using GANs — used GANs to synthetically expand training data for better model performance

**LLMs & Retrieval**
- Working with Large Language Models — learned how to load, prompt, and interact with LLMs effectively
- RAG-based Applications — built a retrieval pipeline using LlamaIndex that fetches relevant documents and feeds them to an LLM for accurate, context-aware answers

### Task
[Sprint Colab Notebook](https://colab.research.google.com/drive/15vxLd-C3OIDuLGT4vXnMeqc1veUUuRld?usp=sharing)

</details>

---

## Final Project — SAHARA (4 Weeks)

**SAHARA – Smart AI Healthcare Assistance & Rapid Aid**

A 1-month capstone project built for Attock, combining everything learned across the fellowship into a real-world AI-powered healthcare platform.

> No unified AI-powered healthcare platform existed for rural Pakistan. SAHARA solves this by combining symptom-based AI diagnosis, emergency navigation, and appointment booking in one place.

**GitHub Repo:** [SAHARA on GitHub](https://github.com/Ayesha0000000/SAHARA-Smart-AI-Healthcare-Assistance-RapidAid)

---

## Tech Stack

| Layer | Tools |
|-------|-------|
| **Language** | Python 3.x |
| **Data** | NumPy, Pandas |
| **Visualization** | Matplotlib, Seaborn |
| **ML** | Scikit-learn |
| **Environment** | Jupyter Notebook |
| **Deep Learning** | Neural Networks (from scratch + frameworks) |

---

## Repository Structure

```
AI-ML-Fellowship-GDGOC-Atk
│
├── Week-1_Python-Basics/
├── Week-2_Titanic-EDA/
├── Week-3-4_Plant-Watering-System/
├── Week-5_Machine-Learning/
├── Week-6_Housing-Price-Prediction/
├── Week-7_Market-Basket-Analysis/
├── Week-8_Deep-Learning/
├── Week-9_Generative-AI-LLMs/
└── Final-Project_SAHARA/
```

---

## Key Learning Outcomes

```
Strong Python foundation for data science
EDA skills — turning raw data into insights
End-to-end ML pipeline: data → model → evaluation
Understanding of classification and regression
Unsupervised learning and pattern discovery
Introduction to neural networks and deep learning
Generative AI — GANs and RAG-based LLM applications
Real-world full-stack AI project from scratch
```

---

## Growth Curve

```
Beginner ──────────────────────────────────────────── Practitioner
   │                                                        │
Week 1     Week 4      Week 6      Week 8     Week 9    Final Project
Python   Team Project  ML Models  Deep       Gen AI     SAHARA App
Basics   Automation   Regression  Learning   & LLMs     (4 Weeks)
   │                                                        │
   └──────────────── 3 Months of Growth ───────────────────┘
```

---

<div align="center">

*Built with curiosity, consistency, and a lot of `print()` debugging.*

**GDGOC Attock | AI-ML Fellowship 2026**

[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com)

</div>
