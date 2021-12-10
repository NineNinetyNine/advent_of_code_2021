def main():
    count = 0
    with open('Day1\numbers.txt') as numberfile:
        lines = numberfile.readlines()
        for i,n in enumerate(lines):
            lines[i] = int(n.strip())
        for sweep in range(len(lines) - 3 ):
            currentsum = lines[sweep] + lines[sweep+1] + lines[sweep+2]
            nextsum = lines[sweep+1] + lines[sweep+2] + lines[sweep+3]
            print(currentsum, nextsum)
            if(nextsum < currentsum):
                print("lower")
                print(count)
            elif(nextsum > currentsum):
                print("higher")
                count += 1
                print(count)
            elif(nextsum == currentsum):
                print("equal")
                print(count)


            
            
        print(count)
                            



if __name__ == "__main__":
    main()