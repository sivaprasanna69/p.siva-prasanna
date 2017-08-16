import re
import string
frequency = {}
document_text = open('/home/prasanna/Desktop/speed.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()[:5]
 
for words in frequency_list:
    print words, frequency[words]
