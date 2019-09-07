def makeMargin(input_file, left_margin, right_margin):
    f = open(input_file, 'r')
    words = []
    for line in f:
        words_one_line = line.split(' ')
        words += words_one_line
    # Remove empty strings from the list of words.
    words = [word for word in words if word != '']
    
    # Open output file
    of = open("DAT1.TXT", 'w')

    # written_char counts the number of chars written in that line. The total can be 80 including the margins.
    #NOTE: written_char also includes the left_margin already when a line is first written
    written_char = 0
    # word_index in the list
    word_index = 0
    while written_char <= 80 and word_index < len(words):
        word = words[word_index]
        # If nothing has been written in the line, write the left margins
        if written_char == 0:
            #write left margin
            of.write(' ' * left_margin)
            written_char += left_margin

        if (len(word) < (80 - right_margin - written_char)):
            of.write(word)
            written_char += len(word)
            if word[-1] == '.':
                # Add if else statements to write two spaces only if two char space is available in the line
                if (1 == (80 - written_char - right_margin - len(word))):
                    of.write(' ')
                    written_char += 1
                else: # when only two char space is available
                    of.write('  ')
                    written_char += 2
            elif word[-1] == '\n':
                # Since we need to start writing in new line, written_char must be changed to the default value of 0
                written_char = 0
            else:
                of.write(' ')
                written_char += 1
            # Increse the word_index as a word is written
            word_index += 1
        elif (len(word) == (80 - right_margin - written_char)):
            of.write(word)
            # Increase the word_index as a word is written
            word_index += 1
            of.write(' ' * right_margin)
            of.write('\n')
            written_char = 0
        else:
            of.write(' ' * (80 - right_margin - written_char))
            written_char = 0 # to default value of 0 for new line
            of.write(' ' * right_margin)
            of.write('\n')
            # word_index is not incresed as no word is written because of less char spaces available
    of.close()

def main():
    input_file = input("Enter the input file name: ")
    left_margin = int(input("Enter the left margin: "))
    right_margin = int(input("Enter the right margin: "))

    # Check a non-empty file name are provided
    if (not input_file):
        print("Please enter non-empty values.")
        return

    # Check if the margins are right.
    if left_margin < 0 or right_margin < 0:
        print("Please enter positive margins.")
        return
    # Apply margins in the file only if the least available space is 15.
    if ((80 - left_margin - right_margin) < 15):
        print("Please decrease your margins.")
        return

    makeMargin(input_file, left_margin, right_margin)

if __name__ == "__main__":
    main()
