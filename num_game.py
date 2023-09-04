def main():
    # TODO write your solution here
    print("Enter a sequence of non-decreasing numbers. ")
    num1 = input("Enter num: ")
    num2 = input("Enter num: ")
    while num2 >= num1:
        num2 = input("Enter num: ")
    if num2 < num1:
        print("Thanks for playing!")
        print("Sequence length: ", len(num2 + num1) - 1)


if __name__ == "__main__":
    main()
