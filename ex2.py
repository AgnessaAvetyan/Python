#Գրել ծրա գիր որը կկա րդա  ֆա յլի  7 ա ռա ջին տ ողը եւ կհա շվի բա ռերի քա նա կը

with open("text1.txt", "r") as lines:
     text = [next(lines) for x in range(7)]
text_str = ' '.join(text)
text_str = text_str.split()
count = 0
for i in text_str:
    count += 1
print(f"The first 7 line's word count: {count}")
