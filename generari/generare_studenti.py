import random

from errors.exceptions import RepoError


class GenerareStudenti:

    def __init__(self, service_studenti):
        self.__service_studenti = service_studenti

    def __genereaza_random(self):
        self.__id = random.randint(0, 100)
        self.__lista_nume = ['Lacusteanu Mihaita', 'Mihaita Tudor', 'Popescu Vasile', 'Popa Radu', 'Ivancu Andrei']
        self.__nume = random.choice(self.__lista_nume)
        self.__grupa = random.randint(211, 218)

        return self.__id, self.__nume, self.__grupa


    def genereaza_studenti(self, nr):
        #nr-=1
        while nr:
            id, nume, grupa = self.__genereaza_random()
            try:
                self.__service_studenti.adauga_student_service(id, nume, grupa)
            except RepoError:
                nr += 1
            nr -= 1