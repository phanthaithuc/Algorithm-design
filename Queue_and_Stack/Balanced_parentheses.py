def balance_parentheses(expression: str) -> bool:
    open_tup = tuple('({[')
    close_tup = tuple(')}]')
    queue = []
    # create hash table with 2 tuples, zip 2 tuple together, open_tup as key, close_tup as value
    map = dict(zip(open_tup, close_tup)) #create hash table with 2 tuples, zip 2 tuple together, open_tup as key, close_tup as value

    for i in expression:
        if i in open_tup:
            queue.append(map[i])
        elif i in close_tup:
            if not queue or i != queue.pop():
                return 'Unbalanced'

    if not queue:
        return 'Balanced'
    else:
        return 'Unbalanced'


if __name__ == "__main__":
    express = "()()){{}{][}{{}]]"
    print(balance_parentheses(express))




