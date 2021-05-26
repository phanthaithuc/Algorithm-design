import time


# def timeit(fn):
#     def get_time(*args, **kwargs):
#         start = time.time()
#         output = fn(*args, **kwargs)
#         print(f"Function {fn.__name__}" + f" finished in: {time.time() - start:.7f}" + "seconds")
#         return output
#
#     return get_time

def timeit(fn):
    def get_time(*args, **kwargs):
        start = time.time()
        output = fn(*args, **kwargs)
        print(f"Function {fn.__name__}" + f" finish in: {time.time() - start:.7f}" + " seconds")

        return output

    return get_time


@timeit
def fib_tabular(n) -> int:
    table = [0] * (n + 3)
    table[1] = 1
    i = 0
    while i <= n:
        table[i + 1] += table[i]
        table[i + 2] += table[i]
        i += 1
    return table[n]


fib_tabular(1000000)
