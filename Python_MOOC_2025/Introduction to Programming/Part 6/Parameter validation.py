# Write your solution here
def new_person(name: str, age: int):
    if not name or " " not in name or len(name) > 40 or age < 0 or age > 150:
        raise ValueError()
    return (name, age)
