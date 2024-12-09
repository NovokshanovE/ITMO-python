import math
import logging
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from functools import partial



def integrate_chunk(f, start, end, n_iter):
    acc = 0
    step = (end - start) / n_iter
    for i in range(n_iter):
        acc += f(start + i * step) * step
    return acc

def integrate(f, a, b, *, n_jobs=1, n_iter=10000000, executor_type='thread'):
    step_size = (b - a) / n_jobs
    futures = []
    chunk_size = n_iter // n_jobs

    if executor_type == 'thread':
        executor_class = ThreadPoolExecutor
    else:
        executor_class = ProcessPoolExecutor

    with executor_class(max_workers=n_jobs) as executor:
        for i in range(n_jobs):
            start = a + i * step_size
            end = start + step_size
            logging.info(f'Starting task for range {start} to {end}')
            futures.append(executor.submit(integrate_chunk, f, start, end, chunk_size))

    result = sum(future.result() for future in futures)
    
    logging.info(f'Completed integrate execution with n_jobs={n_jobs} using {executor_type}')
    return result