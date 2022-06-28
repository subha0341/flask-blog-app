FROM python:3.8-slim-buster
WORKDIR ~/project
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD [ "python3", "application.py", "--host=0.0.0.0"]
