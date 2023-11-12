import random

numbr_sentns = 0
strng = ""
dictnri = {}
j = 0


def newmaker(x):
    dictnri[x] = []


nummer = int(input())
text = input()
text = text.split()


for word in text:
    if word not in dictnri:
        newmaker(word)
    if text[j+1] not in dictnri[word]:
        dictnri[word].append(text[j+1])
    j += 1
    if j+1 == len(text):
        newmaker(text[j])
        break

word1 = random.choice(list(dictnri.keys()))
while word1[0].islower():
    word1 = random.choice(list(dictnri.keys()))
strng += word1
if word1[-1] == "." or word1[-1] == "!" or word1[-1] == "?":
    numbr_sentns += 1
while numbr_sentns < nummer:
    if len(dictnri[word1]) > 0:
        word2 = random.choice(dictnri[word1])
        strng += " " + word2
        word1 = word2
    else:
        word1 = random.choice(list(dictnri.keys()))
        while word1[0].islower():
            word1 = random.choice(list(dictnri.keys()))
        strng += " " + word1

    if word1[-1] == "." or word1[-1] == "!" or word1[-1] == "?":
        numbr_sentns += 1

print(strng)
