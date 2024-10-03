import threading
import time


class WorkerThread(threading.Thread):
    def __init__(self, thread_id: int, task_duration: int):
        # Parameters to parent class constructor could be: target, name, daemon
        super().__init__()
        self.thread_id = thread_id
        self.task_duration = task_duration

    def run(self):
        """This is the method that gets called when the thread starts."""
        print(f"[Worker {self.thread_id}] Starting task...")

        time.sleep(self.task_duration)

        print(f"[Worker {self.thread_id}] Task complete after {self.task_duration} seconds.")


worker1 = WorkerThread(thread_id=1, task_duration=3)
worker2 = WorkerThread(thread_id=2, task_duration=5)
worker3 = WorkerThread(thread_id=3, task_duration=2)

worker1.start()
worker2.start()
worker3.start()

worker1.join()
worker2.join()
worker3.join()

print("All tasks are complete.")
