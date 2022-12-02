# How to use
Open the settings.py file and edit the first to your liking. 

Then run main.py and repeatedly reparse the document while editing the WORD_TYPES and PHONETIC_FALSE_POSITIVES variables.

Use "Review phonetic detections" to search for values you need to put into PHONETIC_FALSE_POSITIVES.

Use "Review incomplete vocabularies" to search for word types you need to put into WORD_TYPES.
Whenever you see a value that is a word type in the generated text file, put it into WORD_TYPES.

Repeat alternately.

# Installation
Clone the repo

`cd parse_wordlist`

Make sure pip is installed. (Try running the pip command) 
If not refer to https://pip.pypa.io/en/stable/installation/

Run `pip install -r requirements.txt`

Everything should be set up
