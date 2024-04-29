numbers_file = open("numbers.txt", "r")
even = open("even.txt", "a")
odd = open("odd.txt", "a")

'''FOR LOOP IN APPENDING 
THE ODD AND EVEN NUMBERS'''
for line in numbers_file: #for loop to call each line of the source file
    if int(line)%2 == 0: #confirmation for even numbers, even number should not have remainder when divided by 2
        even.write(f"{line}")
    elif int(line)%2 != 0: #odd numbers should have remainder when divided by 2
        odd.write(f"{line}")

# CLOSING THE FILE TO AVOID CORRUPTION
numbers_file.close()
even.close()
odd.close()
