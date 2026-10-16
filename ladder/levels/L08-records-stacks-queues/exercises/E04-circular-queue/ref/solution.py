QUEUE_SIZE = 5
queue = [""] * QUEUE_SIZE   # ARRAY of 5 STRING -> indexes 0 to 4
front_pointer = 0
rear_pointer = -1
number_of_items = 0


def enqueue(item: str) -> bool:
    global rear_pointer, number_of_items
    if number_of_items == QUEUE_SIZE:
        return False
    rear_pointer = (rear_pointer + 1) % QUEUE_SIZE
    queue[rear_pointer] = item
    number_of_items = number_of_items + 1
    return True


def dequeue() -> str:
    global front_pointer, number_of_items
    if number_of_items == 0:
        return ""
    item = queue[front_pointer]
    front_pointer = (front_pointer + 1) % QUEUE_SIZE
    number_of_items = number_of_items - 1
    return item
