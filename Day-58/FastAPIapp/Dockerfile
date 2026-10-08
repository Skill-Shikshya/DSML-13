FROM python:3.12.15

WORKDIR /app

COPY requirements.txt .

RUN pip install "fastapi[standard]"
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["fastapi", "run", "app.py", "--port", "8080"]
