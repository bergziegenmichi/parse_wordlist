PDF_FILE = "/home/michael/Desktop/Level C1 Word List.pdf"
STARTING_PAGE = 7
INCLUDE_WORD_TYPES = False
WORD_TYPES = ["NOUN", "VERB", "ADJECTIVE", "ADVERB", "PRONOUN", "PHRASAL VERB", "PREPOSITION", "VERB [T]"]
# needs to have all word types included regardless of INCLUDE_WORD_TYPES option
# you may have to look for yourself if the list is complete
PHONETIC_FALSE_POSITIVES = ["example/illustration/instance"]
# lines with two slashes are counted as lines including a phonetic transcription
# this prevents the script from working correctly
# add all false positives to this list (without the newline at the end)
