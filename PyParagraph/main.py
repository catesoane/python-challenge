import os
import re

paragraph = ""
words = []
word_count = 0
sentences = []
sentence_count = 0
words_per_sentence = 0
total_letters = 0
word_length = 0

file_num = input("Please enter file number 1 or 2: ")
filepath = os.path.join("raw_data", "paragraph_" + str(file_num) +".txt")

with open(filepath, 'r', newline="") as textfile:
    paragraph = textfile.read()
    words = paragraph.split(" ")
    sentences = re.split("(?&lt;=[.!?]) +", paragraph)
    word_count = len(words)
    sentence_count = len(sentences)
    words_per_sentence = word_count/sentence_count

    for character in paragraph:
        if character.isalpha() == True:
            total_letters = total_letters + 1

    word_length = total_letters/word_count


output_file = os.path.join("Output", "paragraph_analysis_" + str(file_num) + ".txt")
with open(output_file, 'w', newline="") as textfile:
    textfile.writelines("Paragraph Analysis\n-----------------\nApproximate Word Count: "
                        + str(word_count) + "\nApproximate Sentence Count: " + str(sentence_count) +
                        "\nAverage Letter Count: " + str(word_length) +
                        "\nAverage Sentence Length: " + str(words_per_sentence))

with open(output_file, 'r') as textout:
    print(textout.read())



