class Student:

    def __init__(self, id, nume, grup):
        """
        initializeaza atributele obiectului curent cu id, nume, grup
        :param id: int
        :param nume: string
        :param grup: int
        """
        self.__id = id
        self.__nume = nume
        self.__grup = grup

    def get_id_student(self):
        """
        :return: returneaza idul id al obiectului curent
        """
        return self.__id

    def get_nume_student(self):
        """
        :return: returneaza numele string al obiectului curent
        """
        return self.__nume

    def get_grup_student(self):
        """
        :return: returneaza grupul grup al obiectului curent
        """
        return self.__grup

    def set_nume_student(self, nume_nou):
        """
        seteaza numele obiectului curent la nume_nou
        :param nume_nou: string
        :return: -
        """
        self.__nume = nume_nou

    def set_grup_student(self, grup_nou):
        """
        seteaza grupul obiectului curent la grup_nou
        :param grup_nou: int
        :return: -
        """
        self.__grup = grup_nou

    def __eq__(self, student):
        """
        verifica daca obiectul curent si obiectul student au acelasi id
        :param student: Student
        :return: 1, daca conditia este indeplinita
                 0, altfel
        """
        return self.__id == student.__id

    def __str__(self):
        return f"{self.__id},{self.__nume},{self.__grup}"
