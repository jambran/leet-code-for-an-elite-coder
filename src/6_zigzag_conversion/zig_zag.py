def generate_queue_index(num_rows):
    if num_rows == 1:
        while True:
            yield 0
    increment = 1
    result = 0
    while True:
        yield result
        result += increment
        if result == num_rows - 1 or result == 0:
            increment = -1 * increment


def convert(s: str, numRows: int) -> str:
    # initialize a number of queues equal to the numRows
    queues = [
        []
        for _ in range(numRows)
    ]

    queue_index_generator = generate_queue_index(numRows)
    queue_index = next(queue_index_generator)

    for char in s:
        queues[queue_index].append(char)
        queue_index = next(queue_index_generator)

    strings_for_each_queue = [
        "".join(queue) for queue in queues
    ]
    return "".join(strings_for_each_queue)
