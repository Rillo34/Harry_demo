FROM python:3.11-slim

WORKDIR /backend

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy backend code
COPY . .

# run API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8100"]