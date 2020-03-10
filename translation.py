import dictionary
print(dictionary.d)

text = "I have three children"
translate = " "
words = text.split()
for w in words:
    translate = translate + " " + dictionary.d[w]

print(translate)