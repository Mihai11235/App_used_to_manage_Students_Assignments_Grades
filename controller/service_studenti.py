from domain.student import Student


class ServiceStudenti:

    def __init__(self, repo_studenti, validator_student):
        """
        Folosind injectia de dependenta, membrul privat __repo_studenti este initializat cu obiectul repo_studenti al clasei RepoStudenti
        Folosind injectia de dependenta, membrul privat __validator_student este initializat cu obiectul validator_student al clasei ValidareStudent
        :param repo_studenti: RepoStudenti
        :param validator_student: ValidareStudent
        """
        self.__repo_studenti = repo_studenti
        self.__validator_student = validator_student

    def adauga_student_service(self, id, nume, grup):
        """
        creeaza, valideaza si adauga in dictionar studentul __student
        :param id: int
        :param nume: string
        :param grup: int
        :return: -
        """
        self.__student = Student(id, nume, grup)
        self.__validator_student.valideaza_student(self.__student)
        self.__repo_studenti.adauga_student(self.__student)

    def modifica_student_service(self, id, nume, grup):
        """
        creeaza, valideaza si modifica in dictionar studentul __student_nou
        :param id: int
        :param nume: string
        :param grup: int
        :return: -
        """
        self.__student_nou = Student(id, nume, grup)
        self.__validator_student.valideaza_student(self.__student_nou)
        self.__repo_studenti.modifica_student(self.__student_nou)

    def sterge_student_dupa_id_service(self, id):
        """
        sterge studentul cu idul id din dictionar
        :param id: int
        :return: -
        """
        self.__repo_studenti.sterge_student_dupa_id(id)

    def get_all_studenti_service(self):
        """
        :return: returneaza dictionarul de studenti
        """
        return self.__repo_studenti.get_all_studenti()

    def __len__(self):
        """
        :return: returneaza lungimea dictionarului de studenti
        """
        return self.__repo_studenti.__len__()
