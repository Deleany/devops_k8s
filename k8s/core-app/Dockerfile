FROM python:3.9-alpine
LABEL authors="Deleany"

WORKDIR /app

COPY ../../requirements.txt /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN apk add curl

COPY core-app.py /app
COPY kafka.py /app

EXPOSE 1111

CMD ["uvicorn", "core-app:app", "--host", "0.0.0.0", "--port", "1111"]