FROM ubuntu:latest
MAINTAINER Marcos Valle "marcosvalle@protonmail.com"
RUN apt-get update -y && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential
COPY . /deface-monitor
WORKDIR /deface-monitor
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["deface-monitor/monitor/run.py"]
