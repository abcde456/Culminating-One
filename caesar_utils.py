import string

IMPOSSIBLE_DOUBLE_LETTER_CONSTANT = 1
IMPOSSIBLE_BIGRAM_CONSTANT = 1
LETTER_FREQUENCY_CONSTANT = 1

FIRST_PLACE_CONSTANT = 1.2
SECOND_PLACE_CONSTANT = 0.5
THIRD_PLACE_CONSTANT = 0.25
FOURTH_PLACE_CONSTANT = 0.125
FIFTH_PLACE_CONSTANT = 0.0675

letterPointDict = {'A': 7.8, 'B': 2.0, 'C': 4.0, 'D': 3.8, 'E': 11.0, 'F': 1.4, 'G': 3.0, 'H': 2.3, 'I': 8.6, 'J': 0.25, 'K': 0.97, 'L': 5.3, 'M': 2.7, 'N': 7.2, 'O': 6.1, 'P': 2.8, 'Q': 0.19, 'R': 7.3, 'S': 8.7, 'T': 6.7, 'U': 3.3, 'V': 3.3, 'W': 1.0, 'X': 0.27, 'Y': 1.6, 'Z': 0.44}

# As of right now, can only be a maximum of 5
LEADERBOARD_CUTOFF_POS = 5

NO_COMMON_WORDS_PUNISHMENT = 25

MOST_COMMON_WORDS = []

with open("words.txt", 'r') as file:
    MOST_COMMON_WORDS = file.read().splitlines()

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
def uncipher(text):
    # The first item in the array is the text, the second is a boolean
    # that tells us if the program is still considering it as possible
    keyDict = {
        0: [text, 0],
        1: [encode(text, 1), 0],
        2: [encode(text, 2), 0],
        3: [encode(text, 3), 0],
        4: [encode(text, 4), 0],
        5: [encode(text, 5), 0],
        6: [encode(text, 6), 0],
        7: [encode(text, 7), 0],
        8: [encode(text, 8), 0],
        9: [encode(text, 9), 0],
        10: [encode(text, 10), 0],
        11: [encode(text, 11), 0],
        12: [encode(text, 12), 0],
        13: [encode(text, 13), 0],
        14: [encode(text, 14), 0],
        15: [encode(text, 15), 0],
        16: [encode(text, 16), 0],
        17: [encode(text, 17), 0],
        18: [encode(text, 18), 0],
        19: [encode(text, 19), 0],
        20: [encode(text, 20), 0],
        21: [encode(text, 21), 0],
        22: [encode(text, 22), 0],
        23: [encode(text, 23), 0],
        24: [encode(text, 24), 0],
        25: [encode(text, 25), 0]
    }

    impossibleArray = [
        "jb", "jc", "jd", "jf", "jg", "jh", "jk", "jl", "jm", "jn", "jp", "jq", "jr", "js", "jt", "jv", "jw", "jx", "jy", "jz",
        "vb", "vc", "vd", "vf", "vg", "vh", "vj", "vk", "vm", "vn", "vp", "vq", "vt", "vw", "vx", "vz"
    ]
    
    for value in keyDict.values():
        if ("JJ" in value[0] or "VV" in value[0]):
            value[1] -= IMPOSSIBLE_DOUBLE_LETTER_CONSTANT
        
        for bigram in impossibleArray:
            if bigram.upper() in value[0]:
                value[1] -= IMPOSSIBLE_BIGRAM_CONSTANT

        foundAnyCommonWord = False
        for i in MOST_COMMON_WORDS:
            if i.strip() in value[0]:
                foundAnyCommonWord = True

        if foundAnyCommonWord == False:            
            value[1] -= NO_COMMON_WORDS_PUNISHMENT

        frequency = letter_frequency(value[0])

        leaderboard = (sorted(frequency, key=frequency.get, reverse=True))

        del leaderboard[LEADERBOARD_CUTOFF_POS:]

        for index, i in enumerate(leaderboard):
            valOfLetter = letterPointDict.get(i)

            if(index == 0):
                value[1] += valOfLetter * FIRST_PLACE_CONSTANT
            elif index == 1:
                value[1] += valOfLetter * SECOND_PLACE_CONSTANT
            elif index == 2:
                value[1] += valOfLetter * THIRD_PLACE_CONSTANT
            elif index == 3:
                value[1] += valOfLetter * FOURTH_PLACE_CONSTANT
            elif index == 4:
                value[1] += valOfLetter * FIFTH_PLACE_CONSTANT
    
    best_key = -1
    highest_score = -999999999999999
    for key, value in keyDict.items():
        current_score = value[1]
        
        if current_score > highest_score:
            highest_score = current_score
            best_key = key
    
    if best_key != -1:
        best_text = keyDict[best_key][0]
        print(best_text)



def main():
    filteredText = filterFile("test.txt")
    uncipher(filteredText)

if __name__ == "__main__":
    main()    