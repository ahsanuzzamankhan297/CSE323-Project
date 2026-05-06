import threading
import time
import random
from collections import deque

BUFFER_SIZE = 5
TOTAL_ITEMS = 20

buffer = deque()
mutex = threading.Lock()
empty_slots = threading.Semaphore(BUFFER_SIZE)
filled_slots = threading.Semaphore(0)


def producer(producer_id: int, item_count: int) -> None:
    for i in range(item_count):
        item = f"Item-{producer_id}-{i + 1}"
        empty_slots.acquire()
        with mutex:
            buffer.append(item)
            current_buffer = list(buffer)
            print(f"[Producer {producer_id}] Produced {item}. Buffer: {current_buffer}")
        filled_slots.release()
        time.sleep(random.uniform(0.1, 0.5))


def consumer(consumer_id: int, item_count: int) -> None:
    for _ in range(item_count):
        filled_slots.acquire()
        with mutex:
            item = buffer.popleft()
            current_buffer = list(buffer)
            print(f"[Consumer {consumer_id}] Consumed {item}. Buffer: {current_buffer}")
        empty_slots.release()
        time.sleep(random.uniform(0.1, 0.5))


def main() -> None:
    producer_count = 1
    consumer_count = 1
    items_per_producer = TOTAL_ITEMS
    items_per_consumer = TOTAL_ITEMS

    producers = [
        threading.Thread(target=producer, args=(pid + 1, items_per_producer))
        for pid in range(producer_count)
    ]
    consumers = [
        threading.Thread(target=consumer, args=(cid + 1, items_per_consumer))
        for cid in range(consumer_count)
    ]

    print("Starting Producer-Consumer simulation")
    print(f"Buffer size: {BUFFER_SIZE}")
    print(f"Total items: {TOTAL_ITEMS}")

    for thread in producers + consumers:
        thread.start()

    for thread in producers + consumers:
        thread.join()

    print("Simulation complete.")


if __name__ == "__main__":
    main()
