def add_word(word,word_count_dict):
    if word in word_count_dict:
        word_count_dict[word]+=1
    else:
        word_count_dict[word]=1    

import string
def process_line(line="",word_count_dict={}):
    line=line.strip()
    word_list=line.split()
    for word in word_list:
        if word !='__':
            word=word.lower()
            word=word.strip() 

            word=word.strip(string.punctuation)
            add_word(word,word_count_dict)



            