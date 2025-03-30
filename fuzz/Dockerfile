FROM python:3.12-slim

RUN pip install atheris

COPY src /app
COPY fuzz/fuzz_calc.py /app

WORKDIR /app

CMD [ "python3", "fuzz_calc.py"]