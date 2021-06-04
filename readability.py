def average_letters(sentence):

    letters = 0
    words = 0

    for letter in sentence:
        if letter.isalpha() == True:
            letters += 1

    for word in sentence.split():
        words+= 1

    return (letters * (100 / words))

def average_sentences(sentence):

    sentences = 0
    words = 0

    for word in sentence.split():
        words += 1

    for end in sentence:
        if end == "!" or end == "?" or end == ".":
            sentences += 1

    return (sentences * (100 / words))

def coleman_liau_index(reading):
    return 0.0588 * average_letters(reading) - 0.296 * average_sentences(reading) - 15.8

def main():

    sentence = input("Text: ")
    if round(coleman_liau_index(sentence)) < 1:
        print("Before Grade 1")
    elif round(coleman_liau_index(sentence)) >= 16:
        print("Grade 16+")
    else:
        print("Grade", round(coleman_liau_index(sentence)))

main()
