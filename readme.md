## Only for windows
```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Steps for setting project

| STEP | CODE | DESC |
|---|---|---|
| 1 | virtualenv env | Create venv   |
| 2 | source env/bin/activate | Activate venv |
|    | ./env/Scripts/activate | |
| 3 | pip install -r requirements.txt | install reqs |
| 4 | pip install httpx | install reqs |
| 5 | python manage.py collectstatic | install |
| 6 | deactivate | Activate venv |


# Create aplication