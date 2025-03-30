FROM gcr.io/oss-fuzz-base/base-builder-python

COPY src /app
COPY fuzz/fuzz_calc.py /app

WORKDIR /app

RUN pip3 install .

CMD [ "python3", "fuzz_calc.py"]