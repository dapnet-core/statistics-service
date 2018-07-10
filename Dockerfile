FROM python:3

ADD statistics-service.py  /

RUN pip3 install flask && pip3 install flask-restful

# private and public mapping
EXPOSE 80

CMD [ "python", "./statistics-service.py" ]
