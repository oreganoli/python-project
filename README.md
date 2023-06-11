# python-project

A university assignment app that exposes, through a JSON HTTP API, a machine-learning model that predicts housing prices in the Boston area through the linear regression algorithm. The model is trained using the [Boston House Prices](https://www.kaggle.com/datasets/vikrishnan/boston-house-prices) dataset available through Kaggle,

## Live instance

A live instance of the app, with Swagger docs, is deployed [at fly.io](https://python-project.fly.dev/docs).

## Build instructions

To build and use `python-project` on your local machine, ensure you have a functioning Python + `pip` installation, then use the following commands:

```
$ pip install -r requirements.txt
$ uvicorn app.main
```