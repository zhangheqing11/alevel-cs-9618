QUEUE_SIZE = 5
queue = [""] * QUEUE_SIZE   # ARRAY of 5 STRING -> indexes 0 to 4
front_pointer = 0
rear_pointer = -1
number_of_items = 0


def enqueue(item: str) -> bool:
    """Return False if the queue is full; otherwise add item at the rear and return True."""
    raise NotImplementedError


def dequeue() -> str:
    """Return "" if the queue is empty; otherwise remove and return the front item."""
    raise NotImplementedError
