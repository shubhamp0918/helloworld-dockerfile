FROM python:3.9
WORKDIR /usr/src/app
EXPOSE 8000
COPY requirements.txt .
COPY server.py .
RUN pip install -r requirements.txt
CMD ["python3", "./server.py"]
