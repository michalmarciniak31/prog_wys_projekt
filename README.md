# Task App 

## Requirements
- Docker Desktop

## 1) Start Docker Desktop

## 2) Start PostgreSQL
```powershell
docker network create tasknet

docker run -d --name taskdb ^
  -e POSTGRES_USER=postgres ^
  -e POSTGRES_PASSWORD=postgres ^
  -e POSTGRES_DB=taskdb ^
  -p 5432:5432 postgres:16
```

## 3) Build and run the app
Run these in the project folder:
```powershell
docker run --rm --network tasknet -p 8501:8501 `
  -e POSTGRES_HOST=taskdb `
  -e POSTGRES_USER=postgres `
  -e POSTGRES_PASSWORD=postgres `
  -e POSTGRES_DB=taskdb `
  task-app
```
## 4) Open: **http://localhost:8501**

