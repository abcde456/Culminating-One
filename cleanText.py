import string

translator = str.maketrans('', '', string.punctuation)

def clean_text(path: str) -> str:
    # 1. Open and read the file
    fileText = ""

    try:
        with open(path) as f:
            fileText = f.read()
    except FileNotFoundError:
        return "ERROR: File not found"
    

    # 2. Convert text to uppercase and turn it into plain text
    fileText = fileText.strip().replace(" ", "").translate(translator).upper()

    # 4. Return the cleaned string
    return fileText

def blockText(text):
    x = 0
    textToReturn = ""
    for i in text:
        if(x > 4):
            x = 0
            textToReturn += " "
            textToReturn += i
        else:
            textToReturn += i
        x += 1
    
    return textToReturn

def main():
    filename = input("Enter filename: ").strip()
    cleaned = clean_text(filename)
    print("Cleaned text:")
    print(cleaned)

    with open("clean.txt", "w") as f:
        f.write(blockText(cleaned))

if __name__ == "__main__":
    main()