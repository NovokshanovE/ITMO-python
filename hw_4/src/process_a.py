import time
import logging

def process_a(input_queue, output_queue):
    while True:
        message = input_queue.get()
        if message is None:
            break

        logging.info(f'Process A received: {message}')
        processed_message = message.lower()
        output_queue.put(processed_message)
        time.sleep(5)