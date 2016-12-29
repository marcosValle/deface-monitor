FROM python:3.5.2
MAINTAINER Marcos Valle "marcosvalle@protonmail.com"
COPY . /graph
WORKDIR /graph
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]
