FROM python:3.9-slim

WORKDIR /app

COPY calculator.py .
COPY test_calculator.py .

CMD ["python", "calculator.py"]
