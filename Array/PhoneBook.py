import collections
import sys


# items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]

# d = collections.defaultdict(list)
# dict = {}

# for item in items:
#    d[item[0]].append(item[1])

# print(d.items())

def phonebook():
    n = int(sys.stdin.readline().strip())
    phone_book = {}
    for i in n:
        entry = sys.stdin.readline().strip().split(' ')
        phone_book[entry[0]] = entry[1]

    query = sys.stdin.readline().strip()
    while query:
        phone_number = phone_book.get(query)
        if phone_numer:
            print(query + '=' + phone_number)
        else:
            print('Not found')


if __name__ == "__main__":
    phonebook()
