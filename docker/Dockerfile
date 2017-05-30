#used Docker version : 1.12.6, build 78d1802
FROM ubuntu:latest
MAINTAINER Vasilis Christopoulos "vasilis.christopoulos@oramon.nl"
#install required packages and oython version for our ubuntu container to be fully functional
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    python-pip \
    python2.7 \
    && apt-get autoremove \
    && apt-get clean

#copy our directory to the container
COPY . /Time-Service
#set the directory as the working directory
WORKDIR /Time-Service

#install all required pips
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

EXPOSE 5000

CMD ["TimeService.py"]

