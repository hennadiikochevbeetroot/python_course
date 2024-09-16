import queue

q = queue.Queue()
q.put(1)  # enqueue
q.put(2)
q.put(3)
q.put(4)
print(q.get())  # dequeue
print(q.queue)  # full queue
print(q.empty())  # is_empty
print(q.qsize())  # size
