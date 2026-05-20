# Workflow-CI

Repository ini berisi workflow CI menggunakan GitHub Actions dan MLflow Project untuk melakukan re-training model secara otomatis ketika trigger dijalankan.

## Link Repository

https://github.com/ovaleeadwii/Workflow-CI

## Struktur Project

- `.github/workflows/ci.yml`: file workflow CI GitHub Actions
- `MLProject/modelling.py`: script training model
- `MLProject/conda.yaml`: environment project
- `MLProject/MLProject`: konfigurasi MLflow Project
- `MLProject/namadataset_preprocessing/diabetes_preprocessing.csv`: dataset hasil preprocessing
- `mlruns/`: artefak hasil training MLflow
- `mlflow.db`: database tracking MLflow

## Cara Menjalankan

```bash
mlflow run MLProject --env-manager=local
