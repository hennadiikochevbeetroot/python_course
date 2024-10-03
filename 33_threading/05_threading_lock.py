import threading
import time

# Shared file name
file_name = 'output.txt'

file_lock = threading.Lock()


def write_to_file(thread_id):
    for i in range(5):
        time.sleep(0.1)
        with file_lock:  # Acquire the lock before writing to the file
            # So result would be - line 0 two times, line 1 two times...
            with open(file_name, 'a') as f:
                f.write(f'Thread {thread_id}: Line {i}\n')


thread1 = threading.Thread(target=write_to_file, args=(1,))
thread2 = threading.Thread(target=write_to_file, args=(2,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('File write complete.')
