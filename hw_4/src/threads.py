import threading
from src.fibonacci import fibonacci

def run_in_threads(n, repetitions):
    threads = []

    for _ in range(repetitions):
        thread = threading.Thread(target=fibonacci, args=(n,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()