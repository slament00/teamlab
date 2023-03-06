def reverse_word(userString, start, end):
        while start < end:
                userString[start], userString[end] = userString[end], userString[start]
                start = start + 1
                end -= 1


userString = input("Type a string of words: ")

userString = list(userString)
start = 0
while True:

        try:
                end = userString.index(' ', start)

                reverse_word(userString, start, end - 1)

                start = end + 1

        except ValueError:

                reverse_word(userString, start, len(userString) - 1)
                break


userString.reverse()

userString = "".join(userString)

print(userString)

