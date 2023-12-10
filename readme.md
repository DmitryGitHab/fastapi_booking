
```.venv\Scripts\activate.bat```

```pip install -r requirements.txt```

uvicorn app.main:app --reload --port 8080    

```alembic init migrations```
-```alembic revision --autogenerate -m "Initial migration"```
```alembic upgrade head``` (alembic downgrade -1)