class ProblemaLab:

    def __init__(self, nrlab_nrprob, descriere, deadline):
        """
        initializeaza atributele obiectului curent cu nrlab_nrprob, descriere, deadline
        :param nrlab_nrprob: int + '_' + int
        :param descriere: string
        :param deadline: int
        """
        self.__nrlab_nrprob = nrlab_nrprob
        self.__descriere = descriere
        self.__deadline = deadline

    def get_nrlab_nrprob_problema(self):
        """
        :return: returneaza nrlab_nrproblema al obiectului curent
        """
        return self.__nrlab_nrprob

    def get_nrlab_problema(self):
        """
        :return: returneaza numarul laboratorului obiectului curent
        """
        return int(self.__nrlab_nrprob.split('_')[0])

    def get_nrprob_problema(self):
        """
        :return: returneaza numarul problemei obiectului curent
        """
        return int(self.__nrlab_nrprob.split('_')[1])

    def get_descriere_problema(self):
        """
        :return: returneaza descrierea descriere a obiectului curent
        """
        return self.__descriere

    def get_deadline_problema(self):
        """
        :return: returneaza deadlineul deadline al obiectului curent
        """
        return self.__deadline

    def set_descriere_problema(self, descriere_noua):
        """
        modifica descrierea obiectului curent la descriere_noua
        :param descriere_noua: string
        :return: -
        """
        self.__descriere = descriere_noua

    def set_deadline_problema(self, deadline_nou):
        """
        seteaza deadlineul obiectului curent la deadline_nou
        :param deadline_nou: int
        :return: -
        """
        self.__deadline = deadline_nou

    def __eq__(self, problema):
        """
        verifica daca atributul nrlab_nrprob al obiectului curent este acelasi cu atributul nrlab_nrprob al obiectului problema
        :param problema: ProblemaLab
        :return: 1, daca se respecta conditia
                 0, altfel
        """
        return self.__nrlab_nrprob == problema.__nrlab_nrprob

    def __str__(self):
        return f"{self.__nrlab_nrprob},{self.__descriere},{self.__deadline}"