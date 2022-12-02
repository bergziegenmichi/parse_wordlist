# How to use
Open the settings.py file and edit the first three variables. Their meaning should be obvious.

Then run main.py and repeatedly reparse the document while editing the `WORD_TYPES` and `PHONETIC_FALSE_POSITIVES` variables.
Do not forget to reload the settings (option 5).

Use "Review phonetic detections" (option 2) to search for values you need to put into `PHONETIC_FALSE_POSITIVES`.

Use "Review incomplete vocabularies" (option 3) to search for word types you need to put into `WORD_TYPES`.
Whenever you see a value that is a word type in the generated text file, put it into `WORD_TYPES`.

Repeat alternately.

When you are done, use "Generate csv file" (option 1). 

# Installation
Clone the repo

`cd parse_wordlist`

Make sure pip is installed. (Try running the pip command) 
If not refer to https://pip.pypa.io/en/stable/installation/

Run `pip install -r requirements.txt`

Everything should be set up
