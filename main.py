import random

numbr_sentns = 0
strng = ""
dictnri = {}
j = 0

nummer = int(input())
text = input()
text = text.split()


def appender(x, y):
    if y not in x:
        x.append(y)


def newmaker(x):
    dictnri[x] = []


for word in text:
    if word in dictnri:
        appender(dictnri[word], text[j+1])
    else:
        newmaker(word)
        appender(dictnri[word], text[j+1])
    j += 1
    if j+1 == len(text):
        newmaker(text[j])
        break

word1 = random.choice(list(dictnri.keys()))
strng += word1
if word1[-1] == ".":
    numbr_sentns += 1
while numbr_sentns < nummer:
    if len(dictnri[word1]) > 0:
        word2 = random.choice(dictnri[word1])
        strng += " " + word2
        word1 = word2
    else:
        word1 = random.choice(list(dictnri.keys()))
        strng += " " + word1
    if word1[-1] == ".":
        numbr_sentns += 1

print(strng)
