FROM python:3.8

WORKDIR /app

COPY ./Flask/requirements.txt /app

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=./Flask/app.py

CMD ["flask", "run", "--host", "0.0.0.0" "-ev"]
