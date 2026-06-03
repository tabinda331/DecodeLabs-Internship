# 🚀 AI Tech Stack Recommender System

> A machine learning-based recommendation system that maps user skills to the most relevant tech job roles using cosine similarity, feature engineering, and explainable AI outputs.

---

## 📌 Project Overview

This project is an AI-powered career recommendation engine that analyzes user skills and recommends the most suitable technology job roles. It uses vector-based similarity (cosine similarity) and weighted skill matching to rank job roles based on relevance.

The system also provides explainable results by showing matched and missing skills for each recommendation.

---

## 🎯 Key Features

- 🔹 Skill-based job role recommendation
- 🔹 Cosine similarity scoring engine
- 🔹 Weighted skill importance system
- 🔹 Fuzzy skill matching (error tolerance)
- 🔹 Domain-based filtering (AI, Web, Data, DevOps)
- 🔹 Experience-level filtering (Junior / Mid / Senior)
- 🔹 Explainable AI output (Matched vs Missing skills)
- 🔹 Interactive Gradio dashboard
- 🔹 Visualization using Plotly

---

## 🧠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Gradio

---

## ⚙️ System Architecture
User Skills Input
↓
Data Preprocessing (cleaning + normalization)
↓
Skill Vectorization
↓
Cosine Similarity Computation
↓
Ranking Engine
↓
Top-N Recommendations + Explanation


---

## 📊 Example Input


python, sql, machine learning


---

## 📈 Output Example

| Job Role | Score |
|----------|------|
| Data Scientist | 0.89 |
| Machine Learning Engineer | 0.85 |
| Data Analyst | 0.81 |

---

## 🧩 Explainability

For each recommendation, the system shows:

- ✅ Matched Skills
- ❌ Missing Skills

Example:


Matched: python, sql
Missing: deep learning, statistic

---

## 📦 Installation

```bash
pip install -r requirements.txt
🚀 Run Project
python task3_recommender.ipynb

or open in Kaggle / Jupyter Notebook

