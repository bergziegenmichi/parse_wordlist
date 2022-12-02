import PyPDF2
import importlib
from string import ascii_letters, ascii_uppercase

import settings

from vocabulary import Vocabulary

settings.STARTING_PAGE -= 1  # python indexes instead of actual page numbers


def read_pdf(print_progress: bool = True) -> str:
    pdffile = open(settings.PDF_FILE, "rb")
    pdfreader = PyPDF2.PdfFileReader(pdffile)

    _text = ""
    num_pages = pdfreader.getNumPages()
    percent = -1
    for page_number in range(settings.STARTING_PAGE, num_pages):
        if print_progress:
            old_percent = percent
            percent = round((page_number / num_pages) * 100)
            if old_percent != percent:
                print("\b" * 10 + f"{percent}%", end="")
        page = pdfreader.getPage(page_number)
        _text += ''.join(
            char for char in page.extractText() if not char.isdigit())
    print("")
    return _text


def parse_document(_text: str) -> tuple[list[Vocabulary], list[str]]:

    _vocabularies: list[Vocabulary] = []

    word = ""
    definition = ""
    word_types = []
    whitelist = set(ascii_letters + " []")

    _found_phonetics = []

    definition_over = False
    for line in _text.split("\n"):
        # print("\n")
        # print(line)
        if line.startswith("Dictionary example"):
            # print("dict example")
            definition_over = True
            if word == "" and definition == "" and len(word_types) == 0:
                continue
            _vocabularies.append(Vocabulary(word, definition, word_types))
            word = ""
            definition = ""
            word_types = []
            continue
        elif definition_over:
            if line.count(
                    "/") < 2 or line.strip() in settings.PHONETIC_FALSE_POSITIVES:
                # print("new word hasnt started yet")
                continue
            else:
                _found_phonetics.append(line.strip())
                definition_over = False
        elif len(line.strip()) == 1:
            # print("single uppercase letter")
            continue

        if word == "":
            # print("added to word")
            word = "".join(filter(whitelist.__contains__, line.split(" /")[0]))
        elif len(word_types) == 0:
            for word_type in line.split("; "):
                word_type = "".join(
                    filter(whitelist.__contains__, word_type.split(" ")[0]))
                if word_type in settings.WORD_TYPES:
                    # print(f"adding {word_type} to word types")
                    word_types.append(word_type)
                # else:
                # print(f"not adding {word_type} to word types")

        else:
            # print("adding to definition")
            if definition != "":
                definition += "\n"
            definition += "".join(filter(whitelist.__contains__, line))

    # print("\n"*3)
    # print("Entire document parsed")
    return _vocabularies, _found_phonetics


print("Reading pdf file...")
text = read_pdf()
print("done\n")
print("Extracting vocabularies...")
vocabularies, found_phonetics = parse_document(text)
print("done")

while True:
    print("\nWhat do you want to do?")
    print("1: Generate csv file")
    print("2: Review phonetic detections")
    print("3: Review incomplete vocabularies")
    print("4: parse document again")
    print("5: reload settings")
    print("6: exit")
    try:
        action = int(input("enter the number: "))
    except ValueError:
        print("thats not a number")
        continue

    if action == 1:
        path = input(
            "enter path to generate csv file (file has to exist and will be overwritten): ")
        with open(path, "w") as f:
            for vocabulary in vocabularies:
                f.write(vocabulary.format_for_csv(settings.INCLUDE_WORD_TYPES))
        print("done")

    elif action == 2:
        path = input(
            "enter path to generate txt file (file has to exist and will be overwritten): ")
        with open(path, "w") as f:
            f.write("\n".join(found_phonetics))
        print("done")

    elif action == 3:
        path = input(
            "enter path to generate txt file (file has to exist and will be overwritten): ")
        with open(path, "w") as f:
            for vocabulary in vocabularies:
                if not vocabulary.is_complete():
                    f.write(str(vocabulary) + "\n" + "-" * 50 + "\n")
        print("done")

    elif action == 4:
        if input(
                "Use cached pdf content instead of reloading it? [Y/n] ").lower() == "n":
            text = read_pdf()
        vocabularies, found_phonetics = parse_document(text)
        print("done")

    elif action == 5:
        importlib.reload(settings)
        print("done")

    elif action == 6:
        break

    else:
        print("invalid number")
