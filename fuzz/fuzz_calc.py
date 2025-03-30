import atheris
import sys
import calc

def fuzz_input(data):
    fdp = atheris.FuzzedDataProvider(data)
    a = fdp.ConsumeInt(4)
    b = fdp.ConsumeInt(4)
    try:
        calc.add(a, b)
    except Exception:
        pass


def main():
    atheris.Setup(sys.argv, fuzz_input)
    atheris.Fuzz()

if __name__ == "__main__":
    main()