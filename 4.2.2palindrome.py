
def palindrome(check):
    pali = check.replace(" ", "").lower()
    if pali == pali[::-1]:
        print(f"{check} IS a Palindrome!")
    else:
        print(f"{check} is NOT a Palindrome!")


palindrome("Borrow or Rob")
palindrome(input("Please insert a Palindrome: "))
