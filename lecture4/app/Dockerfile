FROM python:3.8

WORKDIR /code/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src/ /code/src/

CMD ["uvicorn", "--host", "0.0.0.0", "src.main:app"]
