#Գրել ծրա գիր որը կկա րդա  ֆա յլի պ ա րունա կությունը եւ կտ պ ի տ ողերի քա նա կը եւ ա մենա երկա ր բա ռը

with open("text1.txt","r") as input_file:
    count = len(input_file.readlines())
print(f"Lines count: {count}")
with open("text1.txt","r") as in_file:
    text = in_file.read()
text_word = text.split() 
max_len = len(text_word[0])
for line in text_word:
    if max_len < len(line):
        max_len = len(line)
        max_str = line
print(f"The longest word is: {max_str}\nCount of the character is: {max_len}")
