from multiprocessing import Process
from src.fibonacci import fibonacci

def run_in_processes(n, repetitions):
    processes = []

    for _ in range(repetitions):
        process = Process(target=fibonacci, args=(n,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()