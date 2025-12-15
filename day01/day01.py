import re

def get_rotation_value(line):
    """Parse a rotation line and return the signed rotation value."""
    direction = line[0]
    distance = int(line[1:])

    if direction == 'R':
        return distance
    elif direction == 'L':
        return -distance
    else:
        raise ValueError(f"Line must start with 'R' or 'L', got: {line}")

def get_password(file_path):
    """Calculate password by counting how many times dial points to 0 after rotations."""
    position = 50  # Starting position
    password_count = 0

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if not line:  # Skip empty lines
                continue

            rotation = get_rotation_value(line)

            # Apply rotation and normalize to 0-99 range
            position = (position + rotation) % 100

            # Count if dial points to 0
            if position == 0:
                password_count += 1

    return password_count

def get_password_part2(file):
    position = 50
    count = 0

    with open(file) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            distance = int(line[1:])
            if direction == 'R':
                # Moving right (clockwise)
                # Check all positions from position+1 to position+distance-1
                for d in range(1, distance):
                    if (position + d) % 100 == 0:
                        count += 1
                position = (position + distance) % 100
            else:  # 'L'
                # Moving left (counter-clockwise)
                # Check all positions from position-1 down to position-distance+1
                for d in range(1, distance):
                    if (position - d) % 100 == 0:
                        count += 1
                position = (position - distance) % 100

            # Check if we end at 0
            if position == 0:
                count += 1
    return count

if __name__ == "__main__":
    print("---Pre Test---")
    print("Password: ", get_password('test.txt'))
    print("---Part One---")
    print("Password: ", get_password('input-day01.txt'))
    print("---Part Two Test---")
    print("Password: ", get_password_part2('test.txt'))
    print("---Part Two---")
    print("Password: ", get_password_part2('input-day01.txt'))
