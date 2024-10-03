import threading
import time

# Shared file name
file_name = 'output.txt'


def write_to_file(thread_id):
    with open(file_name, 'a') as f:
        for i in range(5):
            time.sleep(0.1)
            f.write(f'Thread {thread_id}: Line {i}\n')


thread1 = threading.Thread(target=write_to_file, args=(1,))
thread2 = threading.Thread(target=write_to_file, args=(2,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('File write complete.')
