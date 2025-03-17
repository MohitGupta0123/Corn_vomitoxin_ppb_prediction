# 🌽 Corn Vomitoxin Prediction (DeepCorn Project)

## 📝 **Project Overview**
This repository contains a complete pipeline for predicting vomitoxin_ppb concentration in corn samples using both Machine Learning and Deep Learning approaches.

---

## 🏗️ **Project Structure**
```
Corn_Vomitoxin_Prediction/
│
├── DeepCorn_Project_docker/   # Dockerized Inference API
│   └── README.md              # Docker-specific documentation
│
├── EDA & ML Approach Notebook.ipynb   # Traditional ML Pipeline
├── Deep Learning Notebook.ipynb      # Deep Learning Pipeline
│
├── complete_df.csv                   # Original dataset
├── final_scaled_df.csv               # Scaled input dataset
│
├── best_deepcorn_model.pth           # PyTorch Model (Best Model)
├── DeepCorn_Best_Model_optimized.pth    
├── DeepCorn_Best_Model_optimized_better_with_less_features.pth
├── DeepCorn_Best_Model_optimized_Pytorch_with_best_results.pth
│
├── requirements.txt                  # Project Dependencies
├── .gitignore                        # Files to Ignore
└── README.md                         # This Documentation
```

---

## 🎯 **Objective**
Predict the concentration of vomitoxin (ppb) in corn samples using spectral reflectance data from 0 to 447 bands.

---

## 🚀 **Quick Start**

### Step 1: Run EDA and Traditional Machine Learning Approach
```bash
jupyter notebook "EDA & ML Approach Notebook.ipynb"
```

### Step 2: Run Deep Learning Model
```bash
jupyter notebook "Deep Learning Notebook.ipynb"
```

---

## 🐋 **Dockerized Deep Learning Inference (Optional)**

Navigate to the `DeepCorn_Project_docker` folder and follow the instructions in its `README.md` to run the dockerized model.

---

## 📂 **Files Description**

| File/Folder                 | Description                                      |
|-------------------|----------------------------------------------------|
| `EDA & ML Approach Notebook.ipynb` | Exploratory Data Analysis and Traditional ML Model |
| `Deep Learning Notebook.ipynb`    | Deep Learning Model Training and Inference |
| `complete_df.csv`             | Original Dataset |
| `final_scaled_df.csv`        | Scaled Dataset (Input for Deep Model) |
| `DeepCorn_Best_Model_optimized.pth` | Best Deep Learning Model Weights |
| `requirements.txt`         | Python Dependencies |
| `DeepCorn_Project_docker/`| Dockerized Inference API |

---

## 🛠️ **Dependencies**

Install all required packages:
```bash
pip install -r requirements.txt
```

---

## 🛑 **Results and Metrics**
- Achieved the best performance with the deep learning model: `DeepCorn_Best_Model_optimized.pth`
- Improved performance on scaled input data (`final_scaled_df.csv`)

---

## ✅ **How to Run the DeepCorn Docker API**

```bash
cd DeepCorn_Project_docker
```

Follow the Docker README instructions to:
- Pull Docker Image
- Run Flask API
- Test the API for Inference

---

## 🌟 **Future Work**
- Improve Model Robustness
- Deploy on Cloud Platform (AWS/GCP)

---

## 📞 **Contact Me**
[LinkedIn Profile](https://www.linkedin.com/in/mohitgupta012/) | [GitHub](https://github.com/MohitGupta0123)