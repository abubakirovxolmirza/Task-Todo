FROM python:3.12-alpine

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /todo
COPY . /todo

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]