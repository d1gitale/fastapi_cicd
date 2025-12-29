# using base python 3.10 image
FROM python:3.10

WORKDIR /app

COPY requirements.txt .
# installing dependencies before running code
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# this will launch the app "outside" because of 0.0.0.0
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
