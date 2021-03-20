import time
import argparse


def get_arg():
    parser = argparse.ArgumentParser("Tower of Ha Noi")
    parser.add_argument("--nums", type=int, default=3, help="Number of rod to change")
    args = parser.parse_args()
    return args


def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from rod", source, "to rod", destination)
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from rod", source, "to rod", destination)
    TowerOfHanoi(n - 1, auxiliary, destination, source)


current_time = time.time()
n = 30
if __name__ == "__main__":
    opt = get_arg()
    TowerOfHanoi(opt.nums, 'A', 'C', 'B')
    print("Code run in : ", round(time.time() - current_time, 2), 's')
