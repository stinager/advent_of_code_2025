import re

def get_number_with_modulo(line):
    if line[0] == 'R':
        num = int(line[1:])
    elif line[0] == 'L':
        num = -int(line[1:])
    else:
        raise ValueError(f"Line must start with 'R' or 'L', got: {line}")
    if abs(num) > 100:
        return (1 if num > 0 else -1) * (abs(num) % 100)
    return num

def get_password(file):
  code = 50
  password = 0
  number = 0
  with open(file) as file:
    for line in file:
      number = get_number_with_modulo(line)
      code = code + number
      print(code)
      if code < 0:
        code = 100 + code
      if code >= 100:
        code = code - 100
      if code == 0:
        password += 1
    if code > 99:
      code = code - 99
    if code < 0:
      code = 99 - code
  return password


if __name__ == "__main__":
    print("---Pre Test---")
    print("Password: ", get_password('test.txt'))
    print("---Part One---")
    print("Password: ", get_password('input-day01.txt'))