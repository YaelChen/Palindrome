
def palindrome(check):
    no_spaces = check.replace(" ", "")
    low = no_spaces.lower()
    if low == low[::-1]:
        print(f"{check} IS a Palindrome!")
    else:
        print(f"{check} is NOT a Palindrome!")


palindrome("Borrow or Rob")
palindrome(input("Please insert a Palindrome: "))
