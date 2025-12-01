current_number = 50
zero_count = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        direction = line[:1]
        turns = int(line[1:])

        if direction == "R":
            current_number = (current_number + turns) % 100
        else:
            current_number = (current_number - turns) % 100
        
        if current_number == 0:
            zero_count += 1

print(zero_count)