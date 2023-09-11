class Nota:

    def __init__(self, id_nota, student, problema, nota):
        """
        initializeaza atributele obiectului curent cu id_nota, student, ptoblema, nota
        :param id_nota: int
        :param student: Student
        :param problema: Problema
        :param nota: int
        """
        self.__id_nota = id_nota
        self.__student = student
        self.__problema = problema
        self.__nota = nota

    def get_nota(self):
        """
        :return: returneaza valoarea notei
        """
        return self.__nota

    def get_student(self):
        """
        :return: returneaza atributul student de tip Student
        """
        return self.__student

    def get_problema(self):
        """
        :return: returneaza atributul problema de tip Problema
        """
        return self.__problema

    def get_id_nota(self):
        """
        :return: returneaza idul notei
        """
        return self.__id_nota

    def __str__(self):
        return f"{self.__student.get_id_student()},{self.__problema.get_nrlab_nrprob_problema()}," \
               f"{self.__id_nota},{self.__nota}"