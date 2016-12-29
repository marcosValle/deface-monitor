FROM python:3.5.2
MAINTAINER Marcos Valle "marcosvalle@protonmail.com"
COPY . /monitor
WORKDIR /monitor
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]
