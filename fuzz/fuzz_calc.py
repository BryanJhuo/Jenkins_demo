import atheris
import sys
import calc

def TestOneInput(data):
    try:
        s = data.decode("utf-8")
    except UnicodeDecodeError:
        return 
    
    try:
        calc.risky_eval(s)
    except Exception:
        pass

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
