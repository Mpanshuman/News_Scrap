FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["waitress-serve","--listen=0.0.0.0:5000","wsgi:app"]