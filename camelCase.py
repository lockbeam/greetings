def main():
    #request sentence input
    sentence = input('Gimme a sentence to camelCase: ')
    # send to get lowered
    lower_sentence = lower(sentence)
    # send to get split by the spaces
    split_sentence = split(lower_sentence)
    #save the first word and then remove from list
    first_word = split_sentence[0]
    split_sentence.pop(0)
    # send the rest of the list to get first letter capitalized
    capital_list = cap(split_sentence)
    # send to get joined
    smush_together = smush(capital_list)
    print(first_word+smush_together)

def lower(sentence):
    lowering_sentence = sentence.lower()
    return lowering_sentence

def split(sentence):
    splitting_sentence = sentence.split()
    return splitting_sentence

def cap(sentence):
    # found this function here
    # https://favtutor.com/blogs/capitalize-first-letter-python
    capped_sentence = []
    for x in sentence:
        first_letter_capped = x.capitalize()
        capped_sentence.append(first_letter_capped)
    return capped_sentence

def smush(sentence):
    long_string = ""
    for x in sentence:
        long_string += x
    return long_string

main()
    