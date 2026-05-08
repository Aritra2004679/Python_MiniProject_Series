def magic_square(n):

    magicSquare = []

    # Create empty matrix
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        magicSquare.append(row)

    # Initial position
    i = n // 2
    j = n - 1

    num = n * n
    count = 1

    while count <= num:

        # Condition 4
        if i == -1 and j == n:
            i = 0
            j = n - 2

        else:
            # Wrap around column
            if j == n:
                j = 0

            # Wrap around row
            if i < 0:
                i = n - 1

        # Cell already filled
        if magicSquare[i][j] != 0:
            j = j - 2
            i = i + 1
            continue

        else:
            magicSquare[i][j] = count
            count += 1

        # Move to next position
        i = i - 1
        j = j + 1

    # Print magic square
    print(f"Magic Square of Size {n}\n")

    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j], end=" ")
        print()

    # Magic constant
    print("\nThe sum of each row/column/diagonal is:",
          int(n * (n**2 + 1) / 2))


# Driver code
n = int(input("Enter the size of magic square (odd number only): "))
magic_square(n)