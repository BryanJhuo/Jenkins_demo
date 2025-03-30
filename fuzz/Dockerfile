FROM aflplusplus/aflplusplus

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install --upgrade pip

COPY fuzz_target.py /target/
COPY in_corpus /target/in_corpus

WORKDIR /target

CMD [ "env", "AFL_SKIP_BIN_CHECK=1", "afl-fuzz", "-n", "-i", "in_corpus", "-o", "out", "--", "python3", "fuzz_target.py" ]