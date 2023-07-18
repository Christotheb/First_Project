letters = "abcdefghijklmnopqrstuvwxyz"

qpo = letters[16:13:-1]
edcba = letters[4::-1]
last8 = letters[:17:-1]
print(qpo)
print(edcba)
print(last8)

dc = ["abba", "baba", "baab"]

for i in range(len(dc)):
    currentWord = dc[i]
    if currentWord[::-1] == currentWord:
        print(currentWord, "is a palindrome")
    else:
        print(currentWord, "is not a palindrome")
