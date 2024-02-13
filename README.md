[![Qodana](https://github.com/UpswingOps/fastapi-qodana-docker/actions/workflows/code_quality.yml/badge.svg)](https://github.com/UpswingOps/fastapi-qodana-docker/actions/workflows/code_quality.yml)

# FastAPI Qodana Docker app

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
pylint app
```

```bash
pytest tests/test.py
```

## run server
```bash
uvicorn app.main:app --reload
```

http://127.0.0.1:8000/items/5?q=somequery

http://127.0.0.1:8000/docs
