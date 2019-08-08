FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt
COPY . .
RUN python manage.py migrate
EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
