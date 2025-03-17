# DeepCorn Model v2 - Dockerized Version

## 🚀 How to Run the Model:

### Case 1: If you just run model/Docker Image `(deepcorn_model.tar)`

#### ✅ Step 0: in DeepCorn_Project_docker run these commands

#### ✅ Step 1: Load Docker Image
```bash
docker load -i deepcorn_model.tar
```

#### ✅ Step 2: Run Docker Container
```bash
docker run -d -p 5000:5000 deepcorn_model:v1
```

#### ✅ Step 3: Run Test Input (test.py) in new terminal 
##### for new input just give input in nested dictionary format in Input key in '0':0.47556 format
```bash
python test.py
```

### Case 2: If you build Docker Image `(deepcorn_model.tar)`

#### ✅ Step 0: in DeepCorn_Project_docker run these commands

#### ✅ Step 1: Build Docker Image
```bash
docker build -t deepcorn_model:v1 .
```

#### ✅ Step 2: Run Docker Container
```bash
docker run -d -p 5000:5000 deepcorn_model:v1
```

#### ✅ Step 3: Run Test Input (test.py) in new terminal
##### for new input just give input in nested dictionary format in Input key in '0':0.47556 format
```bash
python test.py
```

### Case 3: If you Just want to see output

#### ✅ Step 0: Download `deepcorn_model.tar` and `test.py` and make sure docker in installed in your device and active

#### ✅ Step 1: Load Docker Image
```bash
docker load -i deepcorn_model.tar
```

#### ✅ Step 2: Run Docker Container
```bash
docker run -d -p 5000:5000 deepcorn_model:v1
```

#### ✅ Step 3: Run Test Input (test.py) in new terminal 
##### for new input just give input in nested dictionary format in Input key in '0':0.47556 format
```bash
python test.py