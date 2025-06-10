def word_count(f_contents):

    count_word = f_contents.split()

    return len(count_word)

def num_of_chars(words):

    words = words.split()

    char_count = {}
    new_char_count = {}
    arr = []

    letters = "abcdefghijklmnopqrstuvwxyzæâêëô"


    for word in words:
        word = word.lower()
        for letter in word:
            if letter in char_count:
                char_count[letter] += 1
            else:
                char_count[letter] = 1


    for letter in char_count:
        if letter in letters:
            arr.append(char_count[letter])
            new_char_count[letter] = char_count[letter]

    arr.sort()
    arr = reversed(arr)

    for i in arr:
        for k, v in new_char_count.items():
            if v == i:
                print(f"{k}: {v}")
