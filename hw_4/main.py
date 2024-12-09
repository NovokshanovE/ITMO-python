from src.benchmark import measure_time
from src.fibonacci import fibonacci
from src.threads import run_in_threads
from src.processes import run_in_processes
from src.integrate import integrate

import math
import time
import multiprocessing
from multiprocessing import Process, Queue
from src.process_a import process_a
from src.process_b import process_b
import logging
import sys


def task1():
    n = 35 
    repetitions = 10

    sync_time = measure_time(lambda: [fibonacci(n) for _ in range(repetitions)])


    threads_time = measure_time(run_in_threads, n, repetitions)

    processes_time = measure_time(run_in_processes, n, repetitions)


    with open('artifacts/benchmark_results.txt', 'w') as f:
        f.write(f'Время выполнения синхронного запуска: {sync_time} секунд\n')
        f.write(f'Время выполнения с потоками: {threads_time} секунд\n')
        f.write(f'Время выполнения с процессами: {processes_time} секунд\n')
        
        

def task2():
    logging.basicConfig(
    filename='artifacts/execution_logs.txt',
    level=logging.INFO,
    format='%(asctime)s: %(message)s',
    )   
    a = 0
    b = math.pi / 2
    n_iter = 10000000
    cpu_count = multiprocessing.cpu_count()

    with open('artifacts/execution_times.txt', 'w') as f:
        for n_jobs in range(1, cpu_count * 2 + 1):
            for executor_type in ['thread', 'process']:
                start_time = time.time()
                integrate(math.cos, a, b, n_jobs=n_jobs, n_iter=n_iter, executor_type=executor_type)
                elapsed_time = time.time() - start_time

                f.write(f'{executor_type.capitalize()}Executor with {n_jobs} jobs: {elapsed_time} seconds\n')
                print(f'{executor_type.capitalize()}Executor with {n_jobs} jobs: {elapsed_time} seconds')




def task3():
    logging.basicConfig(
        filename='artifacts/interaction_log.txt',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )
    

    to_a_queue = Queue()
    to_b_queue = Queue()
    main_output_queue = Queue()


    a_process = Process(target=process_a, args=(to_a_queue, to_b_queue))
    b_process = Process(target=process_b, args=(to_b_queue, main_output_queue))


    a_process.start()
    b_process.start()

    try:
        while True:

            line = input('Enter message for process A (or "exit" to quit): ')
            if line.lower() == "exit":
                break
            
            logging.info(f'Main process received input: {line}')
            to_a_queue.put(line)


            result = main_output_queue.get()
            logging.info(f'Main process received from Process B: {result}')
            print(f'Result: {result}')
    finally:

        to_a_queue.put(None)
        to_b_queue.put(None)
        a_process.join()
        b_process.join()


if __name__ == "__main__":
    try:
        task3()
    except KeyboardInterrupt:
        print('Process interrupted by user.')