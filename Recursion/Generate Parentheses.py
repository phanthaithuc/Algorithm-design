def generate_parentheses(n: int) -> None:
    output_array = []
    backtrack(output_array, "", 0, 0, n)

    return output_array


def backtrack(output_array: [], curr_str: str, open: int, close: int, max_n: int) -> str:
    if len(curr_str) == max_n * 2:
        output_array.append(curr_str)
        return output_array

    if open < max_n:
        #curr_str += "("
        backtrack(output_array, curr_str + "(", open + 1, close, max_n)
    if close < open:
        #curr_str += ")"
        backtrack(output_array, curr_str + ")", open, close +1, max_n)


if __name__ == "__main__":
    print(generate_parentheses(3))