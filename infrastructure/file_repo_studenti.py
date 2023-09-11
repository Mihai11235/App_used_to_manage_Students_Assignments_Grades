from domain.student import Student
from infrastructure.repo_studenti import RepoStudenti


class FileRepoStudenti(RepoStudenti):
    def __init__(self, path_to_file):
        RepoStudenti.__init__(self)
        self.__path_to_file = path_to_file

    def __read_all_from_file_recursiv(self, lines, i):
        if i == len(lines):
            return

        line = lines[i]
        line = line.strip()
        if line != "":
            parts = line.split(",")
            id_student = int(parts[0])
            nume_student = parts[1]
            grupa_student = int(parts[2])
            student = Student(id_student, nume_student, grupa_student)
            self._studenti[id_student] = student
        self.__read_all_from_file_recursiv(lines, i+1)

    def __read_all_from_file(self):
        with open(self.__path_to_file, "r") as f:
            lines = f.readlines()
            self._studenti.clear()
            self.__read_all_from_file_recursiv(lines, 0)


    def __write_all_to_file(self):
        with open(self.__path_to_file, "w") as f:
            for student in self._studenti.values():
                f.write(str(student)+"\n")

    def adauga_student(self, student):
        self.__read_all_from_file()
        RepoStudenti.adauga_student(self, student)
        self.__write_all_to_file()

    def modifica_student(self, student_nou):
        self.__read_all_from_file()
        RepoStudenti.modifica_student(self, student_nou)
        self.__write_all_to_file()

    def sterge_student_dupa_id(self, id_student):
        self.__read_all_from_file()
        RepoStudenti.sterge_student_dupa_id(self, id_student)
        self.__write_all_to_file()

    def cauta_student_dupa_id(self, id_student):
        self.__read_all_from_file()
        return RepoStudenti.cauta_student_dupa_id(self, id_student)

    def get_all_studenti(self):
        self.__read_all_from_file()
        return RepoStudenti.get_all_studenti(self)

    def __len__(self):
        self.__read_all_from_file()
        return RepoStudenti.__len__(self)
