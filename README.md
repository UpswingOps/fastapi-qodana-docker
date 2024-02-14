[![Qodana](https://github.com/UpswingOps/fastapi-qodana-docker/actions/workflows/code_quality.yml/badge.svg)](https://github.com/UpswingOps/fastapi-qodana-docker/actions/workflows/code_quality.yml)

# FastAPI Qodana Docker app

FastAPI docs: https://fastapi.tiangolo.com/

Qodana report https://qodana.cloud/projects/3oJwO/reports/Zl2gx

## installation for ```setup.py```
```bash
python -m pip install --upgrade pip
```

```bash
pip install .[dev]
```

## installation for ```requirements.txt```
```bash
python -m pip install -r requirements-dev.txt
```

```bash
python -m pip install -r requirements.txt
```

## lint
```bash
pylint app
```

## test
```bash
pytest tests/test.py
```

## run server
```bash
uvicorn app.main:app --reload
```

Example request: http://127.0.0.1:8000/items/5?q=somequery

Swagger UI: http://127.0.0.1:8000/docs
