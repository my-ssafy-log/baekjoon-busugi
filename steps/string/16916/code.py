import re

whole_string = input()
substring = input()
pattern = rf"{substring}"

match = re.search(pattern, whole_string)

if match:
    print(1)
else:
    print(0)