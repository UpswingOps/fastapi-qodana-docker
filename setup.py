from setuptools import setup, find_packages

setup(
    name="fastapi-qodana-docker",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.103.2",
        "uvicorn[standard]==0.22.0"
    ],
    extras_require={
        "dev": [
            "pylint==3.0.3",
            "pytest==8.0.0",
            "httpx==0.26.0",
        ]
    }
)
