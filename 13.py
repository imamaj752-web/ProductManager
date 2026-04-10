class Note:
    def __init__(self, text, eva):
        self.text = text
        self.author = eva

    def __str__(self):
        return f"Автор: {self.author}\nТекст: {self.text}"


class Notebook:
    def __init__(self):
        self.__notes = []

    def add_note(self, note):
        self.__notes.append(note)

    def search(self, keyword):
        result = []
        for note in self.__notes:
            if keyword in note.text or keyword in note.author:
                result.append(note)
        return result

    def notes_by(self, author):
        result = []
        for note in self.__notes:
            if note.author == author:
                result.append(note)
        return result

    def __str__(self):
        if not self.__notes:
            return "Нотатник порожній"

        output = ["Нотатник"]
        for i, note in enumerate(self.__notes, 1):
            output.append(f"{i}. ({note.author}) {note.text}")
        return "\n".join(output)