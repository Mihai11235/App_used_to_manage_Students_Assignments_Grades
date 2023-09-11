from domain.nota import Nota
from infrastructure.repo_note import RepoNote

class FileRepoNote(RepoNote):
    def __init__(self, path_to_file, repo_studenti, repo_probleme):
        self.__repo_studenti = repo_studenti
        self.__repo_probleme = repo_probleme
        RepoNote.__init__(self)
        self.__path_to_file = path_to_file

    def __read_from_file(self):
        with open(self.__path_to_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != '':
                    parts = line.split(',')
                    id_student = int(parts[0])
                    nrlab_nrprob = parts[1]
                    id_nota = int(parts[2])
                    valoare_nota = int(parts[3])
                    student = self.__repo_studenti.cauta_student_dupa_id(id_student)
                    problema = self.__repo_probleme.cauta_problema_dupa_nrlab_nrprob(nrlab_nrprob)
                    nota = Nota(id_nota, student, problema, valoare_nota)
                    self._note[id_nota] = nota

    def __write_to_file(self):
        with open(self.__path_to_file, 'w') as f:
            for nota in self._note.values():
                f.write(str(nota) + '\n')

    def adauga_nota(self, nota):
        self.__read_from_file()
        RepoNote.adauga_nota(self, nota)
        self.__write_to_file()

    def get_all(self):
        self.__read_from_file()
        return RepoNote.get_all(self)

    def sterge_nota_dupa_id(self, id_nota):
        self.__read_from_file()
        RepoNote.sterge_nota_dupa_id(self, id_nota)
        self.__write_to_file()

    def __len__(self):
        self.__read_from_file()
        return RepoNote.__len__(self)