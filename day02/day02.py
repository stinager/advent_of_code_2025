import re

def get_invalid_ids(file):
    invalid_ids = 0
    with open(file) as f:
        for text in f:
            list = re.split(r",", text)
        for element in list:
          start_id = int(element.split("-")[0])
          end_id = int(element.split("-")[1])
          for id in range(start_id, end_id+1):
            q, r = divmod(len(str(id)), 2)
            first_part, second_part = str(id)[:q + r], str(id)[q + r:]
            if first_part == second_part:
              invalid_ids += id
    return invalid_ids



def get_invalid_ids_part_2(file):
    invalid_ids = 0
    with open(file) as f:
        for text in f:
            list = re.split(r",", text)
        for element in list:
          start_id = int(element.split("-")[0])
          end_id = int(element.split("-")[1])
          for id_num in range(start_id, end_id+1):

            id_str = str(id_num)
            id_len = len(id_str)
            for rep_count in range(7, 1, -1):
              if id_len % rep_count == 0:
                part_len = id_len // rep_count
                # Check if all parts are equal
                parts_equal = True
                first_part = id_str[:part_len]

                for i in range(1, rep_count):
                    if id_str[i*part_len:(i+1)*part_len] != first_part:
                        parts_equal = False
                        break

                if parts_equal:
                    print(f"ID {id_num} has {rep_count} repeating parts: {first_part}")
                    invalid_ids += id_num
                    break  # Skip checking smaller repetition if one is already found
    return invalid_ids

if __name__ == "__main__":
    print("---Pre Test---")
    print("Result: ", get_invalid_ids('input-test.txt'))
    print("---Part One---")
    print("Result: ", get_invalid_ids('input-day02.txt'))
    print("---Part Two Test---")
    print("Result: ", get_invalid_ids_part_2('input-test.txt'))
    print("---Part Two Test---")
    print("Result: ", get_invalid_ids_part_2('input-day02.txt'))