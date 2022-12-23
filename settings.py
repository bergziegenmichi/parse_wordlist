PDF_FILE = "/home/michael/Desktop/Level C1 Word List.pdf"
STARTING_PAGE = 7
ENDING_PAGE = -1  # parse entire document if smaller than STARTING_PAGE
INCLUDE_WORD_TYPES = False
FILTER_ALL_CAPS_IN_DEFINITION = True
WORD_TYPES = ["NOUN", "VERB", "ADJECTIVE", "ADVERB", "PRONOUN", "PHRASAL VERB", "PREPOSITION", "VERB [T]"]
# needs to have all word types included regardless of INCLUDE_WORD_TYPES option
# you may have to look for yourself if the list is complete
PHONETIC_FALSE_POSITIVES = [
    "example/illustration/instance",
    "affluent families/nations/neighbourhoods",
    "direct sth against/at/towards, etc. sb/sth",
    "racial/sex/sexual discrimination",
    "I'm sorry, the job/position/post/vacancy  has already been filled.",
    "fulfil an ambition/dream/goal, etc.",
    "fulfil a function/need/role, etc.",
    "fulfil criteria/requirements/qualifications, etc.",
    "gather speed/strength/support, etc.",
    "hold an opinion/belief/view",
    "The accident was the inevitable consequence/result/outcome  of carelessness.",
    "I/you/we, etc. will just have to do sth",
    "certainly/definitely/hopefully not",
    "a sad/serious/positive  note",
    "the same old arguments/face/story, etc.",
    "an external/internal/reproductive  organ",
    "She felt an overwhelming urge/desire/need to tell someone about what had happened.",
    "race along/down/over, etc.",
    "random checks/tests/attacks",
    "senior/high/junior/low  rank",
    "a rational argument/debate/explanation",
    "At school, they laid/put/placed great stress on academic achievement.",
    "the building/catering/tourist  trade",
    "an unsolved mystery/murder/crime",

]
# lines with two slashes are counted as lines including a phonetic transcription
# this prevents the script from working correctly
# add all false positives to this list (without the newline at the end)
