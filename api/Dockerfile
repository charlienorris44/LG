FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn python-multipart
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
