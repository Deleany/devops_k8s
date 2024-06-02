FROM python:3.9-slim
LABEL authors="Deleany"

WORKDIR /app

COPY requirements.txt /app
COPY core-app.py /app
COPY kafka.py /app

RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean


RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt




EXPOSE 1111

CMD ["uvicorn", "core-app:app", "--host", "0.0.0.0", "--port", "1111"]