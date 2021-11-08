FROM python:3


COPY mongoDB.py /src/mongoDB.py

WORKDIR /src

RUN python -m pip install pymongo


CMD ["python","mongoDB.py"]


#docker build -t name ."
#docker run name
