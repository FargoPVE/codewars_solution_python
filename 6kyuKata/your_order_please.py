def order(sentence):
    words_position_list = []
    for num in range(1, 10):
        for word in sentence.split():
            if str(num) in word:
                words_position_list.append(word)
    return " ".join(words_position_list)