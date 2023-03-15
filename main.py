
def main():
    
    f = open("resources/day_one.txt")

    lines = f.readlines()
    
    lines = list(map(str.strip, lines))
    

    big_list = []
    this_list = []

    for idx, val in enumerate(lines):
        if val == "":
            big_list.append(sum(this_list))
            this_list = []
            continue

        this_list.append(int(val))

    big_list.sort(reverse=True
                  )
    print(f"Day one pt1 value {big_list[0]}")
    print(f"Day one pt2 value {sum(big_list[0:3])}")
    
if __name__ == "__main__":
    main()
