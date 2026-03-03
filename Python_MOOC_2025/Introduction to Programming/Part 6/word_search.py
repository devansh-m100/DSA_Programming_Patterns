# Write your solution here


def find_words(search_term: str):
    with open("words.txt") as words_file:
        words_set = []
        for word in words_file:
            words_set.append(word.strip())

    words_found = []
    if '.' in search_term:
        search_term_letter_indices = []
        for i in range(len(search_term)):
            if search_term[i] != ".":
                search_term_letter_indices.append(i)
        for word in words_set:
            if len(word) == len(search_term):
                letters_matched = True
                for indice in search_term_letter_indices:
                    if search_term[indice] != word[indice]:
                        letters_matched = False
                if letters_matched:
                    words_found.append(word)

                
    elif '*' == search_term[0]:
        for word in words_set:
            if word.endswith(search_term[1:]):
                words_found.append(word)
    elif '*' == search_term[-1]:
        for word in words_set:
            if word.startswith(search_term[:-1]):
                words_found.append(word)
    else:
        for word in words_set:
            if word == search_term:
                words_found.append(word)

    return words_found

