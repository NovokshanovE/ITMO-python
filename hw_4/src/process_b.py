import codecs
import logging

def process_b(input_queue, main_output_queue):
    while True:
        message = input_queue.get()
        if message is None:
            break

        logging.info(f'Process B received: {message}')
        processed_message = codecs.encode(message, 'rot_13')
        logging.info(f'Process B processed: {processed_message}')
        main_output_queue.put(processed_message)