FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app
COPY source /app/source

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

CMD ["python3", "source/app.py"]
