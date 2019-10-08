def count(word, char):
    counter = 0
    for letter in word:
        if letter == char:
            counter += 1
    print("There are "+ str(counter) +" of "+ char +" in " + word)

userword = input("Input a word: ")
userchar = input("Input a char: ")

count(userword, userchar)