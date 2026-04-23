FROM python:3.11-slim

WORKDIR /nicegui

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "/nicegui/main.py"]
