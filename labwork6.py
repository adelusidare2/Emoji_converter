text = input(">")
words = text.split(' ')
emojis = {
    "smile": "😄" ,
    "worried":"😟" , 
} 
for word in words:
 output = "" 
output += emojis.get(word, word) + " " 
print(output) 
 
 
