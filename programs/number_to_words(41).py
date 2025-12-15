digit_words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

num = input("Enter a number: ")

if not num.isdigit():
    print("Invalid input! Please enter a positive integer.")
else:
    words = []
    for digit in num:
        words.append(digit_words[int(digit)])
    print(" ".join(words))
