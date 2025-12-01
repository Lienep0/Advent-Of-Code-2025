current_number = 50
zero_count = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        direction = line[:1]
        turns = int(line[1:])

        # Did a full rotation
        zero_count += turns // 100
        turns %= 100

        if direction == "L":
            turns *= -1

        past_number = current_number
        current_number = (current_number + turns) % 100 

        # Went by zero at least once
        if past_number != 0 and (direction == "L" and (past_number < current_number or current_number == 0) or direction == "R" and past_number > current_number):
            print(f"Triggered on {line.strip()}")
            print(past_number, current_number)
            zero_count += 1

print(zero_count)