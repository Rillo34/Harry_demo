FROM python:3.11

WORKDIR /harry
COPY . /harry

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py", "--port", "8091"]
