# Homework 1 question 1: Title Case Capitalization
word = input('Input a title: ')
#welcome to the world of data-drive modeling for master students offered by HKUST in a great and green campus on the hill.
excluded_word_list =['a','an','the','and','at','by','for','in','of','on','to','up','as','but','or','nor']

split_word = word.split() 
combined_word = ''
#loop over all the splited word
for i in split_word:
    #exlcuded the exception 
    if i in excluded_word_list:
        combined_word = combined_word + i + ' '
    else:
        #change the type str to list
        list_ = list(i)
        count = 0
        #capitalize the words
        for j in list_:
            if count == 0 or list_[count-1] == '-':
                list_[count] = list_[count].capitalize()
            count += 1
        combined = ''.join(list_)
        combined_word = combined_word + combined + ' '
# delete the final empty space 
combined_word = combined_word[:-1]
print(combined_word)