FROM ubuntu:latest

RUN apt-get update

RUN apt-get install -y build-essential

RUN set -x; buildDeps='sudo net-tools iputils-ping apt-utils vim gcc g++ gfortran uuid uuid-dev make wget cmake libeigen3-dev libboost-all-dev libatlas-base-dev' \
    && apt-get update \
    && apt-get install -y $buildDeps \
    && mkdir -p /opt/ls1000


ADD ls1000 /opt/ls1000/

WORKDIR /opt/ls1000/
