

def generate_parens(n: int) -> list[str]:
    # variation on a depth first search

    def generate_parens_recursively(num_left_parens: int, num_right_parens: int, s: str):
        # base case: the string is complete. add it to the result set
        if len(s) == 2 * n:
            result.append(s)
            return

        # recursive case: determine if we need to add left or right paren
        if num_left_parens < n:
            generate_parens_recursively(num_left_parens + 1, num_right_parens, s + "(")
        if num_right_parens < num_left_parens:
            generate_parens_recursively(num_left_parens, num_right_parens + 1, s + ")")


    result = []

    generate_parens_recursively(0, 0, "")
    return result
