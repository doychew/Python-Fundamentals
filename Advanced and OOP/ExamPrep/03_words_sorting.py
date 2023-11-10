def words_sorting(*words):
    word_dictionary = {}
    result = 0
    result_str = []
    for word in words:
        if word not in word_dictionary:
            word_dictionary[word] = 0
            for letter in word:
                result += ord(letter)
            word_dictionary[word] = result
            result = 0
    if sum(word_dictionary.values()) % 2 != 0:
        for word in sorted(word_dictionary.items(), key=lambda x: -x[1]):
            result_str.append(f"{word[0]} - {word[1]}")
    else:
        for word in sorted(word_dictionary.items(), key=lambda x: x[0]):
            result_str.append(f"{word[0]} - {word[1]}")

    return "\n".join(result_str)




print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
