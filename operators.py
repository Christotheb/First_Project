
def IsPalindrome():
    n = int(input("input a number: "))
    m = n
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if m == rev:
        print(str(m) + " is a palindrome.")
    else:
        print(str(m) + " is not a palindrome.")

IsPalindrome()
