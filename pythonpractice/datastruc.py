# Simple Python Data Structure Examples

# 1. List (ordered, changeable, allows duplicates)
my_list = [1, 2, 3, 2, 4]
print("List:", my_list)

# 2. Tuple (ordered, unchangeable, allows duplicates)
my_tuple = (1, 2, 3, 2, 4)
print("Tuple:", my_tuple)

# 3. Set (unordered, no duplicates)
my_set = {1, 2, 3, 2, 4}
print("Set:", my_set)

# 4. Dictionary (key-value pairs, no duplicate keys)
my_dict = {"name": "Alice", "age": 25, "city": "Kathmandu"}
print("Dictionary:", my_dict)

# 5. Stack (LIFO - Last In, First Out) using list
stack = []
stack.append("A")
stack.append("B")
stack.append("C")
print("Stack after pushes:", stack)
stack.pop()
print("Stack after pop:", stack)

# 6. Queue (FIFO - First In, First Out) using list
queue = []
queue.append("X")
queue.append("Y")
queue.append("Z")
print("Queue after enqueue:", queue)
queue.pop(0)
print("Queue after dequeue:", queue)
