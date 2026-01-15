import re
import time

def get_max_joltage(file_path):
  sum_joltage = 0
  with open(file_path) as file:
      for line in file:
          line = line.strip()
          if not line:  # Skip empty lines
              continue
          new_line = line[:-1]
          max_val = max(new_line)
          max_index = new_line.index(max_val)
          second_max_val = max(line[max_index+1:])
          max_joltage = int(str(max_val) + str(second_max_val))
          sum_joltage += max_joltage

  return sum_joltage

def get_max_joltage_part2(file_path):
    sum_joltage = 0

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            digits = [int(digit) for digit in line]

            # We need to select exactly 12 digits
            selected_digits = []
            start_index = 0

            for position in range(12):  # For each of the 12 positions we need to fill
                # Minimum value is 1
                current_max = 1

                # Calculate how far we can search
                # We need (11 - position) more digits after this one
                max_search_index = len(digits) - (11 - position)

                # Search from start_index to max_search_index (exclusive)
                for i in range(start_index, max_search_index):
                    if digits[i] == 9:  # 9 is maximum possible
                        current_max = 9
                        start_index = i + 1  # Next search starts after this digit
                        break
                    elif digits[i] > current_max:
                        current_max = digits[i]
                        start_index = i + 1  # Where to search next

                selected_digits.append(current_max)

            max_joltage = int("".join(map(str, selected_digits)))
            sum_joltage += max_joltage

    return sum_joltage


if __name__ == "__main__":
    start_time = time.perf_counter()
    print("---Pre Test---")
    print("Result: ", get_max_joltage('input-test.txt'))
    print("\n---Part One---")
    print("Result: ", get_max_joltage('input-day03.txt'))
    print("\n---Part Two Test---")
    print("Result: ", get_max_joltage_part2('input-test.txt'))
    print("\n---Part Two---")
    print("Result: ", get_max_joltage_part2('input-day03.txt'))
    end_time = time.perf_counter()
    print(f"\nTime: {end_time-start_time}")
