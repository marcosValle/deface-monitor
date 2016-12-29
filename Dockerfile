FROM ubuntu:latest
MAINTAINER Marcos Valle "marcosvalle@protonmail.com"
RUN apt-get update -y && apt-get install -y \
    python-pip \
    python-dev \
    build-essential
COPY . /deface-monitor
WORKDIR /deface-monitor
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["deface-monitor/monitor/run.py"]
