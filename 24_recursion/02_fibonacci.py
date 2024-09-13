

def fibonacci_iterative(num: int):
    fib_seq = [0, 1]
    for i in range(2, num):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    return fib_seq

def fibonacci_recursive(num: int):
    if num <= 1:
        return num
    else:
        return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)

def fibonacci_recursive_sequence(num: int):
    return [fibonacci_recursive(i) for i in range(num)]


def fibonacci_recursive_oneliner(num: int):
    def fib(num: int):
        return num if num <= 1 else fib(num - 1) + fib(num - 2)

    return [fib(i) for i in range(num)]



print(fibonacci_iterative(10))
print(fibonacci_recursive_sequence(10))
print(fibonacci_recursive_oneliner(10))

