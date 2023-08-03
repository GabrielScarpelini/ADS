FROM python:3.7-slim

RUN python -m pip install --upgrade pip

RUN pip install flask

COPY primos.py /app.py

CMD ["python","app.py"]