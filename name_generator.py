import random


first_names = [
    "James",
    "Robert",
    "John",
    "Michael",
    "David",
    "Noah",
    "Liam",
    "Oliver",
    "Elijah",
    "William",
    "Mary",
    "Patricia",
    "Jennifer",
    "Linda",
    "Elizabeth",
    "Olivia",
    "Amelia",
    "Sophia",
    "Luna",
    "Isabella",
]

last_names = [
    "Smith",
    "Johnson",
    "Williams",
    "Brown",
    "Jones",
    "Garcia",
    "Miller",
    "Davis",
    "Rodriguez",
    "Martinez",
    "Campbell",
    "Hernandez",
    "Allen",
    "Moore",
    "Baker",
    "Murphy",
    "Lopez",
    "Clark",
    "Lee",
]


def get_name():
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    return name
