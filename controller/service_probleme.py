from domain.problema import ProblemaLab


class ServiceProbleme:

    def __init__(self, repo_probleme, validator_problema):
        """
        Folosind injectia de dependenta, membrul privat __repo_probleme este initializat cu obiectul repo_probleme al clasei RepoProbleme
        Folosind injectia de dependenta, membrul privat __validator_problema este initializat cu obiectul validator_problema al clasei ValidareProblema
        :param repo_probleme: RepoProbleme
        :param validator_problema: ValidareProblema
        """
        self.__repo_probleme = repo_probleme
        self.__validator_problema = validator_problema

    def adauga_problema_service(self, nrlab_nrprob, descriere, deadline):
        """
        creeaza, valideaza si adauga la dictionar problema __problema
        :param nrlab_nrprob: string
        :param descriere: string
        :param deadline: int
        :return: -
        """
        self.__problema = ProblemaLab(nrlab_nrprob, descriere, deadline)
        self.__validator_problema.valideaza_problema(self.__problema)
        self.__repo_probleme.adauga_problema(self.__problema)

    def modifica_problema_service(self, nrlab_nrprob, descriere, deadline):
        """
        creeaza, valideaza si modifica in dictionar problema __problema_noua
        :param nrlab_nrprob: string
        :param descriere: string
        :param deadline: int
        :return: -
        """
        self.__problema_noua = ProblemaLab(nrlab_nrprob, descriere, deadline)
        self.__validator_problema.valideaza_problema(self.__problema_noua)
        self.__repo_probleme.modifica_problema(self.__problema_noua)

    def sterge_problema_dupa_nrlab_nrprob_service(self, nrlab_nrprob):
        """
        sterge problema cu numarul laboratorului nrlab si numarul problemei nrprob
        :param nrlab_nrprob: string
        :return: -
        """
        self.__repo_probleme.sterge_problema_dupa_nrlab_nrprob(nrlab_nrprob)

    def get_all_probleme_service(self):
        """
        :return: returneaza dictionarul de probleme
        """
        return self.__repo_probleme.get_all_probleme()

    def __len__(self):
        """
        :return: returneaza lungimea dictionarului de probleme
        """
        return self.__repo_probleme.__len__()