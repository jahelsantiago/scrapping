FROM python:3.8

WORKDIR /playwright-l

COPY ./playwright-lib /playwright-l

RUN pip install pytest-playwright && playwright install && playwright install-deps

CMD [ "python", "./playwright-lib.py" ]
