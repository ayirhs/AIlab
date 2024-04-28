def water_jug(x, y, target):
    # Initial states of jugs
    jug1 = 0
    jug2 = 0

    while jug1 != target and jug2 != target:
        # Fill jug1 if empty
        if jug1 == 0:
            jug1 = x
            print(f"Fill jug1 ({x} gallons)")

        # Pour jug1 into jug2 until jug2 is full or jug1 is empty
        pour_amount = min(jug1, y - jug2)
        jug1 -= pour_amount
        jug2 += pour_amount
        print(f"Pour {pour_amount} gallons from jug1 to jug2")

        # If jug2 becomes full, break the loop
        if jug2 == target:
            break

        # If jug1 becomes empty, fill it again
        if jug1 == 0:
            jug1 = x
            print(f"Fill jug1 ({x} gallons)")

        # If jug2 becomes full, pour it out
        if jug2 == y:
            jug2 = 0
            print(f"Empty jug2")

    return (jug1, jug2)

# Example usage:
x = 4  # Capacity of jug 1
y = 3  # Capacity of jug 2
target = 2  # Target amount of water

result = water_jug(x, y, target)
print(f"\nTarget amount ({target} gallons) is reached with {result[0]} gallons in jug1 and {result[1]} gallons in jug2.")

