# Cara Menjalankan Dashboard

## Sebenarnya sudah dideploy tapi kalau mau menjalankan di lokal berikut tahapannya:

## Setup Environment - Anaconda
```
cd path(sesuaikan dengan posisi folder anda)/submission
conda create --name main-ds python=3.12
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
cd path(sesuaikan dengan posisi folder anda)/submission
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run dashboard/dashboard.py
```