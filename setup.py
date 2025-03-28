from setuptools import setup, find_packages

setup(
    name="rag_eval_kit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer>=0.9.0,<1.0.0",
    ],
    python_requires=">=3.8",
)
