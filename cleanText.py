import string

translator = str.maketrans('', '', string.punctuation)

def clean_text(path: str) -> str:
    # 1. Open and read the file
    fileText = ""

    try:
        with open(path, 'r', encoding='utf-8') as f:
            fileText = f.read()
    except FileNotFoundError:
        return "ERROR: File not found"
    

    # 2. Convert text to uppercase and turn it into plain text
    fileText = fileText.strip().replace(" ", "").translate(translator).upper()

    # 4. Return the cleaned string
    return fileText

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

def main():
    filename = input("Enter filename: ").strip()
    cleaned = clean_text(filename)
    with open("clean.txt", "w") as f:
        f.write(chunk5(cleaned))

    key = get_key()    

    print(encode(chunk5(cleaned), key))

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
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    shiftedText = ""

    for ch in text:
        pos = alphabet.find(ch)

        newLetter = alphabet[(pos + key) % 26]

        shiftedText += newLetter

    return shiftedText

if __name__ == "__main__":
    main()