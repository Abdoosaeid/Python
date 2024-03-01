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

def pretty_print(word_count_dict={}):

    value_key_list=[]
    for key,val in word_count_dict.items():
        value_key_list.append((val,key))

    value_key_list.sort(reverse=True)

    print('{:11s}{:11s}'.format('Word','Count'))
    print('_'*21)
    for val,key in value_key_list:
        print('{:12s}{:<3d}'.format(key,val))
                        