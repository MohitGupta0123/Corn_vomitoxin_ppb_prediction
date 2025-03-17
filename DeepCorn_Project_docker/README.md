# 🚀 DeepCorn Model Inference API (Dockerized)

## 📜 **Overview**
This repository contains a Dockerized Flask API for running inference using the `DeepCornModelV2`, a PyTorch-based deep learning model for predicting vomitoxin_ppb concentration in corn samples using spectral reflectance at different wavelengths.

The API takes input in JSON format, processes the input data, and returns predictions.

---

## 🌟 **Folder Structure**
```
DeepCorn_Model/
│
├── app/
│   ├── predict.py            # Flask API
│   ├── model.py              # PyTorch Model
│   ├── test.py               # Test Script
│   ├── requirements.txt      # Python Dependencies
│   ├── cols_to_drop.txt      # Columns to Drop
│   └── DeepCorn_Best_Model_optimized.pth   # Pre-trained Model
│
├── Dockerfile                 # Dockerfile to Create Image
└── README.md                  # This Documentation
```

---

## 🛠️ **Step 1: Install Docker (If Not Installed)**
- For Ubuntu:
```bash
sudo apt-get install docker.io
```

- For Windows/Mac:
Download from [Docker Official Website](https://www.docker.com/products/docker-desktop/)

---

## 📦 **Step 2: Pull the Docker Image from Docker Hub**

The Docker image is already pushed to Docker Hub.

```bash
docker pull mohit472/deepcorn_model:v1
```

---

## 🔥 **Step 3: Run the Docker Container**

```bash
docker run -p 5000:5000 mohit472/deepcorn_model:v1
```

- `-p 5000:5000`: Maps container port `5000` to local port `5000`
- `mohit472`: My Docker Hub username

---

## ✅ **Step 4: Test the API (Using test.py)**

In your local new terminal, run the test script to make a POST request to the running Flask API:

```python
import requests

input_data = {
  'input': {
    '40': 0.5,   # Red Band
    '100': 0.7,  # NIR Band
    '200': 0.3   # SWIR Band
    .
    .
    .
  }
}

response = requests.post('http://localhost:5000/predict', json=input_data)
print(response.json())

# For my model you need to give scaled value from final_scaled_df.csv as input format that have values for column '0' to '447' spectral reflectance bands and my model will take necessary columns needed for prediction.

```

### 🎯 Sample Output:
```json
{
  "predictions": [0.7532]
}
```

---

## 🗃️ **Files Description**

| File/Folder             | Description                                                    |
|----------------|------------------------------------------------------|
| `predict.py`        | Main Flask API for Model Inference                               |
| `model.py`          | PyTorch Model Architecture and Weights Loading          |
| `test.py`               | For Testing the API Locally                                             |
| `requirements.txt` | Python Packages Required                                     |
| `cols_to_drop.txt` | List of Columns to Drop from Input Data                    |
| `DeepCorn_Best_Model_optimized.pth` | Pre-trained Model Weights                       |
| `Dockerfile`             | Dockerfile for Building the Docker Image                      |

---

## 🎯 **If You Want to Build Docker Image Manually (Optional)**

```bash
docker build -t deepcorn_model:v1 .
```

---

## 📤 **If You Want to Push Image by building new image to Docker Hub (Optional)**

```bash
# Login to Docker Hub

docker login

# Tag the Docker Image
docker tag deepcorn_model:v1 <dockerhub_username>/deepcorn_model:v1

# Push the Image to Docker Hub
docker push <dockerhub_username>/deepcorn_model:v1
```

---

## 🛑 **How Your Anyone Can Use the Docker Image**

1️⃣ Pull the Image:
```bash
docker pull mohit472/deepcorn_model:v1
```

2️⃣ Run the Container:
```bash
docker run -p 5000:5000 mohit472/deepcorn_model:v1
```

3️⃣ Make Predictions via API:
```bash
python test.py
```

---

## 🎯 **Future Improvements**
- Add logging for better monitoring.
- Deploy on Cloud using AWS/GCP/Azure.
- Add Docker Compose for multi-container setup.

---

## ✅ **References**
- Flask
- PyTorch
- Docker

---

## ⭐️ **If you like this repository, give it a star 🌟**

---

## 📞 **Contact Me**
[LinkedIn Profile](https://www.linkedin.com/in/mohitgupta012/)  |  [GitHub](https://github.com/MohitGupta0123)