def modifyText(text, n):
    newText = ""
    for i in text:
        if i.lower() in "abcdefghijklmnopqrstuvwxyzæøå":
            newLetter = modifyLetter(i, n)
            newText+= newLetter
        else:
            newText += i
    return newText

def modifyLetter(letter, n):
    alphabet = "abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
    position = alphabet.index(letter)
    newPosition = (position + n) % (29 * 2)
    return alphabet[newPosition]

text = "Jeg liker_ støre g<tter99"

print(modifyText(text,3))
