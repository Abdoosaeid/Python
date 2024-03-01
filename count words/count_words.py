def add_word(word, word_count_dict):
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1    

import string

def process_line(line="", word_count_dict={}):
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        if word != '__':
            word = word.lower()
            word = word.strip() 
            word = word.strip(string.punctuation)
            add_word(word, word_count_dict)

def pretty_print(word_count_dict={}):
    value_key_list = []
    for key, val in word_count_dict.items():
        value_key_list.append((val, key))

    value_key_list.sort(reverse=True)
    with  open('output.txt', 'w') as output_file:
        print("Length of the dictionary:", len(word_count_dict),file=output_file)
        print('{:15s}{:11s}'.format('Word', 'Count'),file=output_file)
        print('_'*21,file=output_file)
        for val, key in value_key_list:
            print('{:15s}{:<3d}'.format(key, val),file=output_file)

def main():
    word_count_dict = {}
    with  open('words.txt', 'r') as text_file:

        for line in text_file:
            process_line(line, word_count_dict)

        pretty_print(word_count_dict)    

if __name__ == "__main__":
    main()
