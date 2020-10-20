# AS06

vowels = ["a", "e", "i", "o", "u"]

word = input("Input word").lower()

count = 0
for i in range(len(word)):
    if word[i] in vowels:
        count = count + 1

print(count)
