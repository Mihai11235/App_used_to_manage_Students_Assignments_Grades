import random

from errors.exceptions import RepoError


class GenerareProbleme:

    def __init__(self, service_probleme):
        self.__service_probleme = service_probleme


    def __genereaza_random(self):
        self.__nrlab = random.randint(1, 20)
        self.__nrprob = random.randint(1, 10)

        self.__nrlab_nrprob = str(self.__nrlab) + '_' + str(self.__nrprob)

        self.__lista_descrieri = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        self.__descriere = random.choice(self.__lista_descrieri)
        self.__deadline = random.randint(1, 31)

        return self.__nrlab_nrprob, self.__descriere, self.__deadline

    def genereaza_probleme(self, nr):
        #nr -= 1
        while nr:
            nrlab_nrprob, descriere, deadline = self.__genereaza_random()
            try:
                self.__service_probleme.adauga_problema_service(nrlab_nrprob, descriere, deadline)
            except RepoError:
                nr += 1
            nr -= 1
