import sys
import time

def risky_logic(data: str):
    if "boom" in data:
        raise ValueError("💥Boom! Crash triggered by 'Boom' ")
    
    if data.startswith("eval:"):
        exec(data[5:])

    try:
        number = int(data.strip())
        if number == 99999:
            raise OverflowError("🚨 The Values is too large")
    except ValueError:
        pass
    
    time.sleep(0.1)
    return "OK"

def main():
    data = sys.stdin.read()

    try:
        risky_logic(data)
    except Exception as e:
        print(f"[!] Exception caught: {e}", file = sys.stderr)
        raise

if __name__ == "__main__":
    main()