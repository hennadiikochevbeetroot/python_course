import threading
import time

event = threading.Event()


def worker():
    print("[Worker] Waiting for the setup to complete...")
    event.wait()
    print("[Worker] Setup complete, starting processing...")
    time.sleep(2)
    print("[Worker] Processing done.")


def setup():
    print("[Setup] Performing setup...")
    time.sleep(3)
    print("[Setup] Setup is complete. Notifying worker...")
    event.set()


setup_thread = threading.Thread(target=setup)
setup_thread.start()

worker_thread = threading.Thread(target=worker)
worker_thread.start()

for thread in [setup_thread, worker_thread]:
    thread.join()

print("Both threads have completed.")
