import threading

class Object:
    def __init__(self):
        self.ref_count = 1  # Initial reference count is 1

    def increment_ref(self):
        self.ref_count += 1

    def decrement_ref(self):
        self.ref_count -= 1
        if self.ref_count == 0:
            self.deallocate()

    def deallocate(self):
        print("Object deallocated")

# Simulating two threads
def thread_1(obj):
    obj.increment_ref()  # Thread 1 increases ref count
    obj.decrement_ref()  # Thread 1 decreases ref count

def thread_2(obj):
    obj.increment_ref()  # Thread 2 increases ref count
    obj.decrement_ref()  # Thread 2 decreases ref count

# If there would be no GIL, then we could have final result 2
# Example: increment starts with 1, then with 2, but decrement starts with 3, and once again 3

obj = Object()
t1 = threading.Thread(target=thread_1, args=(obj,))
t2 = threading.Thread(target=thread_2, args=(obj,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Final reference count: {obj.ref_count}")