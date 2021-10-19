FROM python:3.8.2
WORKDIR /object-detect-api
COPY . .
RUN pip install -r requirements.txt
EXPOSE 3000
ENTRYPOINT ["python", "app.py"]