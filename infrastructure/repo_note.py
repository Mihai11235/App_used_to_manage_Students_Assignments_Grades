from errors.exceptions import RepoError


class RepoNote:

    def __init__(self):
        self._note = {}

    def adauga_nota(self, nota):
        """
        adauga nota nota la dictionarul de note
        :param nota: Nota
        :return: -
        """
        if nota.get_id_nota() in self._note:
            raise RepoError("Nota a fost deja asignata!")

        for id_nota in self._note:
            notaa=self._note[id_nota]
            if notaa.get_student() == nota.get_student() and notaa.get_problema() == nota.get_problema():
                raise RepoError("Nota a fost deja asignata!")

        self._note[nota.get_id_nota()] = nota

    def get_all(self):
        note = []
        for id_nota in self._note:
            note.append(self._note[id_nota])
        return note

    def sterge_nota_dupa_id(self, id_nota):
        if id_nota not in self._note:
            raise RepoError("Nota pe care doriti sa o stergeti nu exista!")

        for id_nota in self._note:
            nota=self._note[id_nota]
            if nota.get_id_nota() == id_nota:
                del self._note[id_nota]
                return

    def __len__(self):
        return len(self._note)