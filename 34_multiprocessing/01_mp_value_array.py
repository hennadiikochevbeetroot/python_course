import multiprocessing


def square_numbers(shared_array: list[int], processed_numbers: multiprocessing.Value, start_index: int, end_index: int):
    """Function to square numbers in a shared array."""
    for i in range(start_index, end_index):
        previous_value = shared_array[i]
        processed_numbers.value += 1
        shared_array[i] **= 2  # Squaring the number in place
        print(f'Processed number {previous_value}: {shared_array[i]}, total processed: {processed_numbers.value}')


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    num_processes = 3

    processed_numbers = multiprocessing.Value('i', 0)
    shared_array = multiprocessing.Array('i', numbers)  # 'i' for integer

    chunk_size = len(numbers) // num_processes
    processes = []
    for i in range(num_processes):
        start_index = i * chunk_size
        # Ensure the last process handles any remaining elements
        end_index = len(numbers) if i == num_processes - 1 else start_index + chunk_size
        p = multiprocessing.Process(target=square_numbers,
                                    args=(shared_array, processed_numbers, start_index, end_index))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    squared_numbers = list(shared_array)

    print("Original numbers:", numbers)
    print("Squared numbers:", squared_numbers)


if __name__ == "__main__":
    main()
