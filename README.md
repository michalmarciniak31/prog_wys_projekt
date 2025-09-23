# Task App 

## Requirements
- Docker Desktop

## ## Starting app via Docker

## 1) Start Docker Desktop

## 2) Start PostgreSQL
```powershell/cmd
docker network create tasknet

docker run -d --name taskdb --network tasknet ^
  -e POSTGRES_USER=postgres ^
  -e POSTGRES_PASSWORD=postgres ^
  -e POSTGRES_DB=taskdb ^
  postgres:16
```

## 3) Build and run the app
Run these in the project folder:
```powershell
docker run --rm --network tasknet -p 8501:8501 ^
  -e POSTGRES_HOST=taskdb ^
  -e POSTGRES_PORT=5432 ^
  -e POSTGRES_USER=postgres ^
  -e POSTGRES_PASSWORD=postgres ^
  -e POSTGRES_DB=taskdb ^
  task-app
```
## 4) Open: **http://localhost:8501**

## ## Starting app locally

## 1) Install PostgreSQL

```
winget install -e --id PostgreSQL.PostgreSQL
```

## 2) Create DB
```
Adjust path to psql first

"C:\Program Files\PostgreSQL\17\bin\psql.exe" -h 127.0.0.1 -U postgres -c "CREATE DATABASE taskdb;"
```

## 3) Run app
```
python -m venv .venv
.\.venv\Scripts\activate.bat
pip install -r requirements.txt
set POSTGRES_HOST=127.0.0.1
set POSTGRES_PORT=5432
set POSTGRES_USER=postgres
set POSTGRES_PASSWORD=1234
set POSTGRES_DB=taskdb
set PYTHONPATH=.
streamlit run src\app.py
```
