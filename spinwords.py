def reverseWord(word):
    return "".join(list(reversed(word)))

def spinWords(words):
    wordsList = words.split(" ")
    outputList = []
    for word in wordsList:
        if len(word) >= 5:
            outputList.append(reverseWord(word))
        else:
            outputList.append(word)
    return " ".join(outputList)