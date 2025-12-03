with open("input.txt", "r") as f:
    banks = f.readlines()

total = 0
n = 12
for k, bank in enumerate(banks):
    batteries = [int(x) for x in bank.strip()]

    # Each step, iterate over current + the new battery
    # Then, find the first digit that has a bigger digit on its right and replace that digit. Otherwise discard the new digit
    current = batteries[:n]
    is_optimal = [current[i] >= current[i + 1] for i in range(n - 1)]
    for i in range(n, len(batteries)):
        tail_better_than_new = current[-1] >= batteries[i]
        for j in range(n - 1):
            if not is_optimal[j]:
                current = current[:j] + current[j + 1:] + [batteries[i]]
                is_optimal = is_optimal[:j] + is_optimal[j + 1:] + [tail_better_than_new]
                break
        else:
            if not tail_better_than_new:
                current = current[:-1] + [batteries[i]]
                is_optimal = is_optimal[:-1] + [current[-2] >= current[-1]]
    
    print(f"Line {k + 1} : found {int(''.join([str(x) for x in current]))}")
    
    total += int(''.join([str(x) for x in current]))

print(total)

# 95094337635047 : too low