FROM gcr.io/oss-fuzz-base/base-builder-python

COPY fuzz /src

WORKDIR /src

RUN pip3 install atheris

CMD [ "python3", "fuzz_calc.py" ]