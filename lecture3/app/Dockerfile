FROM python:latest

EXPOSE 8000

WORKDIR /code/app

COPY ./requirements.txt .

RUN pip install -r ./requirements.txt

COPY ./src ./src

CMD ["gunicorn", "-b 0.0.0.0:8000", "-w 4", "src.main:app"]