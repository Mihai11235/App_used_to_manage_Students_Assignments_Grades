from errors.exceptions import RepoError


class RepoProbleme:

    def __init__(self):
        """
        creeaza dictionarul de probleme cu cheia nrlab_nrprob si valoarea obiectul problema
        """
        self._probleme = {}

    def adauga_problema(self, problema):
        """
        adauga problema problema la dictionarul de probleme
        :param problema: ProblemaLab
        :return: -
        :raises: RepoError daca problema se afla deja in dictionar
        """
        if problema.get_nrlab_nrprob_problema() in self._probleme:
            raise RepoError('problema existenta')
        self._probleme[problema.get_nrlab_nrprob_problema()] = problema

    def modifica_problema(self, problema_noua):
        """
        modifica problema cu numarul laboratorului nrlab si numarul problemei nrprob ale problemei noi la problema_noua
        :param problema_noua: ProblemaLab
        :return: -
        :raises: RepoError daca nu exista nicio problema cu numarul laboratorului nrlab si numarul problemei nrprob
        """
        if problema_noua.get_nrlab_nrprob_problema() not in self._probleme:
            raise RepoError("Problema pe care vreti sa o modificati nu exista!")
        self._probleme[problema_noua.get_nrlab_nrprob_problema()] = problema_noua

    def sterge_problema_dupa_nrlab_nrprob(self, nrlab_nrprob):
        """
        sterge problema cu numarul laboratorului nrlab si numarul problemei nrprob
        :param nrlab_nrprob: string
        :return: -
        :raises: RepoError daca nu exista nicio problema cu numarul laboratorului nrlab si numarul problemei nrprob
        """
        if nrlab_nrprob not in self._probleme:
            raise RepoError("Problema pe care vreti sa o stergeti nu exista!")
        del self._probleme[nrlab_nrprob]

    def cauta_problema_dupa_nrlab_nrprob(self, nrlab_nrprob):
        """
        cauta problema cu numarul laboratorului nrlab si numarul problemei nrprob
        :param nrlab_nrprob: string
        :return: -
        :raises: RepoError daca nu exista nicio problema cu numarul laboratorului nrlab si numarul problemei nrprob
        """
        if nrlab_nrprob not in self._probleme:
            raise RepoError("Problema pe care o cautati nu exista in lista")
        return self._probleme[nrlab_nrprob]

    def get_all_probleme(self):
        """
        :return: returneaza dictionarul de probleme
        """
        probleme = {}

        for nrlab_nrprob in self._probleme:
            problema = self._probleme[nrlab_nrprob]
            probleme[nrlab_nrprob] = [problema.get_descriere_problema(), problema.get_deadline_problema()]

        return probleme

    def __len__(self):
        """
        :return: returneaza numarul de probleme din dictionar
        """
        return len(self._probleme)
