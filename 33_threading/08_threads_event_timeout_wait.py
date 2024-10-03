import logging
import threading
import time


def wait_blocking(event: threading.Event):
    logging.info('Wait for event (blocking)')
    event_is_set = event.wait()
    logging.info(f'Event is set: {event_is_set}')


def wait_timeout(event: threading.Event, timeout: int):
    while not event.is_set():
        logging.info(f'Wait for event (with timeout {timeout} seconds)')
        event_is_set = event.wait(timeout)
        logging.info(f'Event is set: {event_is_set}')
        if event_is_set:
            logging.info('Business logic with event, as it is already set')
        else:
            logging.info('Business logic NOT for event, as it is NOT set')


logging.basicConfig(
    level=logging.INFO,
    format='(%(threadName)-10s) %(message)s',
)

event = threading.Event()
blocking_thread = threading.Thread(target=wait_blocking, args=(event,))
blocking_thread.start()

timeout = 2
timeout_thread = threading.Thread(target=wait_timeout, args=(event, timeout))
timeout_thread.start()

logging.info('Waiting before calling Event.set()')
time.sleep(6)
event.set()
logging.info('Event is set explicitly')
