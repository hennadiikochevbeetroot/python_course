import multiprocessing


def square(number: int):
    return number ** 2


def main():
    numbers = list(range(10))

    # Create a Pool with a number of worker processes
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        single_result = pool.apply_async(square, (5,))
        print('Single process result: ', single_result.get())

        multiple_results = pool.map(square, numbers)
        print("Original numbers:", numbers)
        print('Multiple processes result:', multiple_results)

        iterator_results = pool.imap(square, numbers)
        for result in iterator_results:
            print(result, end=', ')
        # print(next(iterator_results))
        # print(next(iterator_results))
        # print(next(iterator_results))
        # print(next(iterator_results))


if __name__ == '__main__':
    main()
