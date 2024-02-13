# qodana-test

https://fastapi.tiangolo.com/

Qodana report https://qodana.cloud/projects/3oJwO/reports/Zl2gx

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
pylint src
```

```bash
pytest tests/test.py
```

## run server
```bash
uvicorn src.main:app --reload
```

http://127.0.0.1:8000/items/5?q=somequery
