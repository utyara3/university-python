import re

print(re.search(r"cat", "a cat b"))  # найдёт cat
print(re.search(r"^cat", "a cat b"))  # None
print(re.search(r"cat$", "a cat b"))  # найдёт cat
