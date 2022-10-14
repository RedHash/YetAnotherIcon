FROM python:3.9

WORKDIR /usr/src/webserver

COPY ./Docker/webserver/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/webserver .

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]