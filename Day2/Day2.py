def main():
    forward_count = 0
    aim_count = 0
    depth_count = 0
    with open("Day2\input.txt") as infile:
        instructions = infile.readlines()
    for i, n in enumerate(instructions):
        instructions[i] =n.strip()
    full_instructions =[y for x in instructions for y in x.split()]

    for instruction in range(len(full_instructions)):
        if(full_instructions[instruction] == "forward"):
            forward_count += int(full_instructions[instruction + 1])
            depth_count += (int(full_instructions[instruction + 1])* aim_count)
        if(full_instructions[instruction] == "down"):
            aim_count += int(full_instructions[instruction + 1])
        if(full_instructions[instruction] == "up"):
            aim_count -= int(full_instructions[instruction + 1])
    print("p1 depth:" , aim_count, "forward:", forward_count, "multiplied together", aim_count*forward_count)
    print("p2 depth:", depth_count, "p2 answer: ", depth_count*forward_count)





if __name__ == "__main__":
    main()