FROM python:3.8-slim-buster
WORKDIR ~/project
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python3", "application.py", "--host==0.0.0.0", "-p 5000"]
