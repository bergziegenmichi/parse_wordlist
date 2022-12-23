class Vocabulary:
    word: str
    definition: str
    word_types: list[str]

    def __init__(self, word: str, definition: str, word_types: list[str] = []):
        self.word = word
        self.definition = definition
        self.word_types = word_types

    def format_for_csv(self, include_word_types: bool = True) -> str:
        res = f"{self.word}\t{self.definition}" \
               f"{'; '.join(self.word_types) if include_word_types else ''}\n"
        print(res)
        print("-"*50)
        return res

    def __str__(self):
        return f"word:        {self.word}\n" \
               f"definition:  {self.definition}\n" \
               f"word_types:  {self.word_types}"

    def is_complete(self, include_word_types: bool = True) -> bool:
        return (
                self.word != "" and
                self.definition != "" and
                (len(self.word_types) != 0 or not include_word_types)
        )
