def reverse(x: int) -> int:
    if x < 0:
        factor = -1
        x = x * factor
    else:
        factor = 1
    stringified_num = str(x)
    return int(stringified_num[::-1]) * factor

if __name__ == '__main__':
    inputs_and_outputs = [
        (123, 321),
        (-123, -321),
    ]
    for input_, output in inputs_and_outputs:
        print(f"{input_} -> {output}")