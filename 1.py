while True: 
    print("\n1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        n = int(input("Enter number of rows: "))
        for i in range(1, n + 1):
            print("*" * i)

    elif ch == 2:
        s = int(input("Enter start: "))
        e = int(input("Enter end: "))
        total = 0

        for i in range(s, e + 1):
            if i % 2 == 0:
                print("Number  is Even",1)
            else:
                print("Number  is Odd",2)
            total += i

        print("Sum is:", total)

    elif ch == 3:
        print("Thank you!")
        break

    else:
        print("Invalid choice")
        break            
