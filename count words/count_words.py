def add_word(word,word_count_dict):
    if word in word_count_dict:
        word_count_dict[word]+=1
    else:
        word_count_dict[word]=1    