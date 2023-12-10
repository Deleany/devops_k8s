FROM python:3.9-alpine
LABEL authors="Deleany"

WORKDIR /app

COPY requirements.txt /app

RUN pip3 --no-cache-dir install --upgrade pip && \
    pip3 --no-cache-dir install -r requirements.txt
RUN apk --no-cache add curl

COPY main.py /app

EXPOSE 1111

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1111"]