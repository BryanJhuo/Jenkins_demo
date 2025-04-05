def add(x, y):
    return x + y

def risky_eval(input_str):
    if "boom" in input_str:
        raise ValueError("Boom!")
    return eval(input_str)