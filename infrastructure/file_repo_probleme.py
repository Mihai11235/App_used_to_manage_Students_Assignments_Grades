from domain.problema import ProblemaLab
from infrastructure.repo_probleme import RepoProbleme


class FileRepoProbleme(RepoProbleme):
    def __init__(self, path_to_file):
        RepoProbleme.__init__(self)
        self.__path_to_file = path_to_file

    def __read_from_file(self):
        with open(self.__path_to_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != '':
                    parts = line.split(',')
                    nrlab_nrprob = parts[0]
                    descriere = parts[1]
                    deadline = int(parts[2])
                    problema = ProblemaLab(nrlab_nrprob, descriere, deadline)
                    self._probleme[nrlab_nrprob] = problema


    def __write_to_file(self):
        with open(self.__path_to_file, 'w') as f:
            for problema in self._probleme.values():
                f.write(str(problema) + '\n')

    def adauga_problema(self, problema):
        self.__read_from_file()
        RepoProbleme.adauga_problema(self, problema)
        self.__write_to_file()

    def modifica_problema(self, problema_noua):
        self.__read_from_file()
        RepoProbleme.modifica_problema(self, problema_noua)
        self.__write_to_file()

    def sterge_problema_dupa_nrlab_nrprob(self, nrlab_nrprob):
        self.__read_from_file()
        RepoProbleme.sterge_problema_dupa_nrlab_nrprob(self, nrlab_nrprob)
        self.__write_to_file()

    def cauta_problema_dupa_nrlab_nrprob(self, nrlab_nrprob):
        self.__read_from_file()
        return RepoProbleme.cauta_problema_dupa_nrlab_nrprob(self, nrlab_nrprob)

    def get_all_probleme(self):
        self.__read_from_file()
        return RepoProbleme.get_all_probleme(self)

    def __len__(self):
        self.__read_from_file()
        return RepoProbleme.__len__(self)