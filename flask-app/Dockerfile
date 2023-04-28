FROM python:3.8-slim-buster
RUN apt update
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# EXPOSE 5000

CMD ["python", "app_sqlite.py"]
