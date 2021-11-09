FROM python:latest


WORKDIR /usr/python/src
RUN python -m pip install psycogp2
COPY postgres.py ./

CMD ["python","./postgres.py"]