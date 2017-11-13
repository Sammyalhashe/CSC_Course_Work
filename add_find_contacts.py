# all letters, a, ab, abc, ..
def all_orderings(contact):
    return [contact[0:idx] for idx in range(1, len(contact) + 1)]

contact_indices = {}
def add(contact):
    for key in all_orderings(contact):
        contact_indices[key] =contact_indices.get(key, 0) + 1

def find(name):
    return contact_indices.get(name, 0)

n = int(input().strip())

for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        add(contact)
    elif op == 'find':
        count = find(contact)
        print(count)

