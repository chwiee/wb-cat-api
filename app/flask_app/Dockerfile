FROM python:3.5-alpine
WORKDIR /app
COPY ./app/flask_app/ /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["main.py"]