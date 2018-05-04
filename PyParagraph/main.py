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
new_sentences = []

file_num = input("Please enter file number 1 or 2: ")
filepath = os.path.join("raw_data", "paragraph_" + str(file_num) +".txt")

with open(filepath, 'r', newline="") as textfile:
    paragraph = textfile.read()
    words = paragraph.split(" ")

    #print(words)
    #print(paragraph)

    sentences = re.split("(?<=[.!?]) +", paragraph)
    #for s in sentences:
        #if s != '' and s != ' ':
            #new_sentences.append(s)
    #print("ns = ", new_sentences)
    word_count = len(words)

    #print(word_count)
    
    

    #sentence_count = len(sentences)
    sentence_count = paragraph.count(".") + paragraph.count("?") + paragraph.count("!")
    #print(sentence_count)

    words_per_sentence = word_count/sentence_count
    
    #print(words_per_sentence)

    for character in paragraph:
        if character.isalpha() == True:
            total_letters = total_letters + 1

    word_length = total_letters/word_count

    #print(word_length)

print("\nParagraph Analysis")
print("-" * 25)
print("Approximate Word Count:", str(word_count))
print("Approximate Sentence Count:", str(sentence_count))
print("Approximate Letter Count:", str(word_length))
print("Approximate Sentence Length:", str(words_per_sentence))




output_file = "paragraph_analysis_" + str(file_num) + ".txt"
output_file_path = os.path.join("Output", output_file)

with open(output_file, 'w', newline="") as textfile:
    textfile.writelines("Paragraph Analysis\n-----------------\nApproximate Word Count: "
                        + str(word_count) + "\nApproximate Sentence Count: " + str(sentence_count) +
                        "\nAverage Letter Count: " + str(word_length) +
                        "\nAverage Sentence Length: " + str(words_per_sentence))

with open(output_file, 'r') as textout:
    print(textout.read())



