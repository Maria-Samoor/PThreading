import threading
import time

def worker(num):
    """Thread worker function"""
    print(f"Thread {num} started")
    time.sleep(2)
    print(f"Thread {num} finished")

# Create 5 threads
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)

# Start the threads
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("All threads finished")