class Queue:
    def __init__(self):
        self._items = []

    @property
    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    @property
    def size(self):
        return len(self._items)


class Task:
    def __init__(self, name: str, time_needed: int):
        self.name = name
        self.time_needed = time_needed  # Total time required to complete the task
        self.time_processed = 0  # Time processed so far

    def process(self, time_slice: int) -> bool:
        """Process the task for a given time slice"""
        time_to_process = min(self.time_needed - self.time_processed, time_slice)
        self.time_processed += time_to_process
        print(
            f"Processing {self.name} for {time_to_process} time units. "
            f"Total processed: {self.time_processed}/{self.time_needed}"
        )
        return self.time_processed >= self.time_needed  # Returns True if task is completed


def round_robin(tasks: list[Task], time_slice: int):
    queue = Queue()
    for task in tasks:
        queue.enqueue(task)

    while not queue.is_empty:
        task = queue.dequeue()
        # If task is not finished, put it back in the queue
        if not task.process(time_slice):
            queue.enqueue(task)


tasks = [Task("Task1", 10), Task("Task2", 5), Task("Task3", 8)]
time_slice = 3
round_robin(tasks, time_slice)
