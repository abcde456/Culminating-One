import string

translator = str.maketrans('', '', string.punctuation)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def clean_text(text) -> str:
    returnText = text.strip().replace(" ", "").translate(translator).upper()
    return returnText

def chunk5(text):
    x = 0
    z = 0
    y = False
    textToReturn = ""
    for i in text:
        if(x > 4):
            z += 1
            if(z > 7):
                textToReturn += "\n"
                z = 0
                y = True
            else:
                y = False
            x = 0 
            if y == False:
                textToReturn += " "
            textToReturn += i
            y = False
        else:
            textToReturn += i
        x += 1
    
    return textToReturn

def get_key() -> int:
    while True:
        raw = input("Enter a key (1–25): ").strip()

        try:
            # 1) convert to an integer
            k = int(raw)

            # 2) check range
            if k > 0 and k < 25:  # k is between 1 and 25
                # valid: return it
                return k
            else:
                print("Invalid, key must be between 1 and 25.")
                # loop continues

        except ValueError:   # which exception?
            print("Invalid — you may only enter a number.")
            # loop continues

def encode(text: str, key: int) -> str:
    shiftedText = ""

    for ch in text:
        if(ch ==" "):
            shiftedText += " "
            continue
        pos = alphabet.find(ch)

        newLetter = alphabet[(pos + key) % 26]

        shiftedText += newLetter

    return shiftedText

def decode(text: str, key: int) -> str:
    out  = ""

    for ch in text:
        if(ch ==" "):
            out += " "
            continue
        # 1) Map 'A'..'Z' to 0..25
        pos = alphabet.find(ch)

        # 2) Find letter
        dec = alphabet[(pos - key) % 26]

        # 3) Append to output
        out += dec

    return out


def letter_frequency(text: str) -> dict[str, int]:
    letterDict = {}
    for i, char in enumerate(text):
        if not char in letterDict:
            letterDict[char] = 1
        else:
            letterDict[char] += 1

    return letterDict

def most_common_double_letter(text: str) -> tuple[str, int] | None:
    # Start with a counter of how many times this letter occured
    # If another letter appears, set letter counter to 0
    # If the same letter appears, set letter counter to 0, but set double 
    # letter count of that letter to +1

    filteredText = text

    for char in filteredText:
        if char.upper() not in alphabet:
            filteredText = filteredText.replace(char, "")

    currentLetterCounter = 0
    currentLetter = ""
    letterTrackDict = {}
    for i, char in enumerate(filteredText):
        if currentLetter == char:
            currentLetterCounter += 1

            if currentLetterCounter == 2:
                if not char in letterTrackDict:
                    letterTrackDict[char] = 1
                else:
                    letterTrackDict[char] += 1
                
                currentLetterCounter = 0
        else:
            currentLetter = char
            currentLetterCounter = 1
    
    currentHighestNum = 0
    currentHighestChar = ""
    for key, value in letterTrackDict.items():
        if value > currentHighestNum:
            currentHighestNum = value
            currentHighestChar = key
    
    if(currentHighestNum != 0):
        return currentHighestChar + ", " + str(currentHighestNum)
    else:
        return "No double letters"

# Function to filter a text file input by the user into just letters
def filterFile(text: str):
    filteredText = ""
    fileText = ""
    with open(text, 'r') as file:
        fileText = file.read()

    for i, char in enumerate(fileText):
        if char.upper() in alphabet:
            filteredText += char
    return filteredText

# This function will eliminate the impossible combinations of a caeser cipher
def eliminateImpossible(text):
    # The first item in the array is the text, the second is a boolean
    # that tells us if the program is still considering it as possible
    keyDict = {
        0: [text, True],
        1: [encode(text, 1), True],
        2: [encode(text, 2), True],
        3: [encode(text, 3), True],
        4: [encode(text, 4), True],
        5: [encode(text, 5), True],
        6: [encode(text, 6), True],
        7: [encode(text, 7), True],
        8: [encode(text, 8), True],
        9: [encode(text, 9), True],
        10: [encode(text, 10), True],
        11: [encode(text, 11), True],
        12: [encode(text, 12), True],
        13: [encode(text, 13), True],
        14: [encode(text, 14), True],
        15: [encode(text, 15), True],
        16: [encode(text, 16), True],
        17: [encode(text, 17), True],
        18: [encode(text, 18), True],
        19: [encode(text, 19), True],
        20: [encode(text, 20), True],
        21: [encode(text, 21), True],
        22: [encode(text, 22), True],
        23: [encode(text, 23), True],
        24: [encode(text, 24), True],
        25: [encode(text, 25), True]
    }

    impossibleArray = [
        "jb", "jc", "jd", "jf", "jg", "jh", "jk", "jl", "jm", "jn", "jp", "jq", "jr", "js", "jt", "jv", "jw", "jx", "jy", "jz",
        "vb", "vc", "vd", "vf", "vg", "vh", "vj", "vk", "vm", "vn", "vp", "vq", "vt", "vw", "vx", "vz"
    ]
    
    for value in keyDict.values():
        if ("JJ" in value[0] and ("AJ" not in value[0] and "EJ" not in value[0] and "IJ" not in value[0] and "OJ" not in value[0] or "UJ" not in value[0])) and ("VV" in value[0] and ("AV" not in value[0] and "EV" not in value[0] and "IV" not in value[0] and "OV" not in value[0] and "UV" not in value[0])):
            value[1] = False
        
        if value[1] == True:
            for bigram in impossibleArray:
                if bigram.upper() in value[0] and ("AJ" not in value[0] and "EJ" not in value[0] and "IJ" not in value[0] and "OJ" not in value[0] and "UJ" not in value[0] and "AV" not in value[0] and "EV" not in value[0] and "IV" not in value[0] and "OV" not in value[0] and "UV" not in value[0]):
                    value[1] = False

    for value in keyDict.values():
        print(value[1])


def main():
    filteredText = filterFile("test.txt")
    eliminateImpossible(filteredText.upper())

if __name__ == "__main__":
    main()    