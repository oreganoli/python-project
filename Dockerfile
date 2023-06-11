FROM python:3
COPY requirements.txt domain.py main.py model.py ./
COPY data/housing.csv ./data/housing.csv
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app"]
EXPOSE 8080