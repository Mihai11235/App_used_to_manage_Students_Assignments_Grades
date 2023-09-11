from errors.exceptions import RepoError


class RepoStudenti:

    def __init__(self):
        """
        creeaza dictionarul de studenti care are cheia idul studentului si valoarea obiectul student
        """
        self._studenti = {}

    def adauga_student(self, student):
        """
        adauga studentul student in dictionarul de studenti
        :param student: Student
        :return: -
        :raises: RepoError daca exista deja un student cu idul studentului nou
        """
        if student.get_id_student() in self._studenti:
            raise RepoError("Student existent")
        self._studenti[student.get_id_student()] = student

    def modifica_student(self, student_nou):
        """
        modifica studentul cu idul studentului nou la student_nou
        :param student_nou: Student
        :return: -
        :raises: RepoError daca nu exista niciun student cu idul studentului nou
        """
        if student_nou.get_id_student() not in self._studenti:
            raise RepoError("Studentul pe care vreti sa il modificati nu exista!")
        self._studenti[student_nou.get_id_student()] = student_nou

    def sterge_student_dupa_id(self, id_student):
        """
        sterge studentul cu idul id_student din dictionarul de studenti
        :param id_student: int
        :return: -
        :raises: RepoError daca nu exista niciun student cu idul id_student
        """
        if id_student not in self._studenti:
            raise RepoError("Studentul pe care doriti sa-l stergeti nu exista!")
        del self._studenti[id_student]

    def cauta_student_dupa_id(self, id_student):
        """
        cauta studentul cu idul id_student in dictionarul de studenti
        :param id_student: int
        :return: -
        :raises: RepoError daca nu exista niciun student cu idul id_student
        """
        if id_student not in self._studenti:
            raise RepoError("Studentul pe care il cautati nu exista in lista")
        return self._studenti[id_student]


    def get_all_studenti(self):
        """
        :return: returneaza dictionarul de studenti
        """
        studenti = {}
        for id in self._studenti:
            student = self._studenti[id]
            studenti[student.get_id_student()] = [student.get_nume_student(), student.get_grup_student()]

        return studenti

    def __len__(self):
        """
        :return: returneaza numarul de studenti din dictionar
        """
        return len(self._studenti)
