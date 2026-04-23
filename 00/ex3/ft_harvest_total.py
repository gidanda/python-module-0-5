def ft_harvest_total():
    day1 = int(input("Day 1 harvest: "))
    day2 = int(input("Day 2 harvest: "))
    day3 = int(input("Day 3 harvest: "))

    total = day1 + day2 + day3
    print(f"Total harvest: {total}")

def main():
    ft_harvest_total()

if __name__ == "__main__":
    main()