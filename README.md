# qodana-test

https://fastapi.tiangolo.com/

## installation
```bash
python -m pip install --upgrade pip
```

```bash
python -m pip install -r requirements-dev.txt
```

```bash
python -m pip install -r requirements.txt
```

## test / lint
```bash
pylint main.py
```

## run server
```bash
uvicorn main:app --reload
```

http://127.0.0.1:8000/items/5?q=somequery
