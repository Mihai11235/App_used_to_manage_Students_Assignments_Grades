import unittest

from controller.service_note import ServiceNote
from controller.service_studenti import ServiceStudenti
from controller.service_probleme import ServiceProbleme
from domain.nota import Nota
from domain.student import Student
from domain.problema import ProblemaLab
from errors.exceptions import ValidationError, RepoError
from infrastructure.file_repo_note import FileRepoNote
from infrastructure.file_repo_probleme import FileRepoProbleme
from infrastructure.file_repo_studenti import FileRepoStudenti
from infrastructure.repo_note import RepoNote
from infrastructure.repo_studenti import RepoStudenti
from infrastructure.repo_probleme import RepoProbleme
from validations.validator_nota import ValidareNota
from validations.validator_student import ValidareStudent
from validations.validator_problema import ValidareProblema


class TestDomain(unittest.TestCase):
    # student
    def setUp(self):
        # student
        self.__id = 1
        self.__nume = 'Popescu Vlad'
        self.__grup = 214
        self.__student = Student(self.__id, self.__nume, self.__grup)
        # problema
        self.__nrlab_nrprob = '2_3'
        self.__descriere = 'a'
        self.__deadline = 12
        self.__problema = ProblemaLab(self.__nrlab_nrprob, self.__descriere, self.__deadline)
        #nota
        self.__id_nota = 1
        self.__nota = 10
        self.__nota_lab = Nota(self.__id_nota, self.__student, self.__problema, self.__nota)

    def tearDown(self):
        pass

    def test_domain_student(self):

        self.assertTrue(self.__student.get_id_student() == self.__id)
        self.assertTrue(self.__student.get_nume_student() == self.__nume)
        self.assertTrue(self.__student.get_grup_student() == self.__grup)
        self.__clona = Student(self.__id, None, None)
        self.assertTrue(self.__student == self.__clona)  # apeleaza automat __eq__
        self.assertTrue(self.__student. __eq__(self.__clona))

    def test_domain_problema(self):
        self.assertTrue (self.__problema.get_nrlab_problema() == 2)
        self.assertTrue (self.__problema.get_nrprob_problema() == 3)
        self.assertTrue (self.__problema.get_nrlab_nrprob_problema() == '2_3')
        self.assertTrue (self.__problema.get_descriere_problema() == self.__descriere)
        self.assertTrue (self.__problema.get_deadline_problema() == self.__deadline)
        self.__clona = ProblemaLab(self.__nrlab_nrprob, None, None)
        self.assertTrue (self.__clona == self.__problema)

    def test_domain_nota(self):
        self.assertTrue (self.__nota_lab.get_nota() == self.__nota)
        self.assertTrue (self.__nota_lab.get_student() == self.__student)
        self.assertTrue (self.__nota_lab.get_problema() == self.__problema)
        self.assertTrue (self.__nota_lab.get_id_nota() == self.__id_nota)



class TestValidators(unittest.TestCase):
        def setUp(self):
            #student
            self.__id = 1
            self.__nume = 'Popescu Vlad'
            self.__grup = 214
            self.__student = Student(self.__id, self.__nume, self.__grup)
            self.__student_invalid = Student(-1, '', -2)

            self.__validare_student = ValidareStudent()
            self.__validare_student.valideaza_student(self.__student)
            # problema
            self.__nrlab_nrprob = '2_3'
            self.__descriere = 'a'
            self.__deadline = 12
            self.__problema = ProblemaLab(self.__nrlab_nrprob, self.__descriere, self.__deadline)
            self.__problema_invalida = ProblemaLab('-1_2', "", 33)


            self.__validare_problema = ValidareProblema()
            self.__validare_problema.valideaza_problema(self.__problema)

            # nota
            self.__id_nota = 1
            self.__nota = 10
            self.__nota_lab = Nota(self.__id_nota, self.__student, self.__problema, self.__nota)
            self.__nota_invalida = Nota(-1, self.__student, self.__problema, 11)


            self.validare_nota = ValidareNota()
            self.validare_nota.valideaza_nota(self.__nota_lab)


        def tearDown(self):
            pass

        def testValidatorsStudent(self):
            try:
                self.__validare_student.valideaza_student(self.__student_invalid)
                self.assertTrue(False)
            except ValidationError as ve:
                self.assertTrue (str(ve) == "id invalid!\nnume invalid!\ngrup invalid!\n")

        def testValidatorsProblema(self):
            try:
                self.__validare_problema.valideaza_problema(self.__problema_invalida)
                self.assertTrue(False)
            except ValidationError as ve:
                self.assertTrue(str(ve) == "laborator sau problema invalide!\ndescriere invalida!\ndeadline invalid!\n")

        def testValidatorsNota(self):
            try:
                self.validare_nota.valideaza_nota(self.__nota_invalida)
                self.assertTrue(False)
            except ValidationError as ve:
                self.assertTrue(str(ve) == "id invalid!\nnota invalida!\n")

class TestRepo(unittest.TestCase):
    def setUp(self):
        # student
        self.__repo_studenti = RepoStudenti()
        self.__student = Student(1, 'Vlad', 5)
        self.__repo_studenti.adauga_student(self.__student)
        self.__student_nou = Student(1, 'Cosmin', 10)
        self.__student_inexistent = Student(2, "Alex", 4)

        # problema
        self.__repo_probleme = RepoProbleme()
        self.__problema = ProblemaLab('1_1', 'pb1', 23)
        self.__repo_probleme.adauga_problema(self.__problema)
        self.__problema_noua = ProblemaLab('1_1', "Alta_Pb", 24)
        self.__problema_inexistenta = ProblemaLab('1_2', "a", 1)

        #nota
        self.__repo_note = RepoNote()
        self.__nota = Nota(1, self.__student, self.__problema, 10)
        self.__repo_note.adauga_nota(self.__nota)

    def tearDown(self):
        pass

    def test_adaugare_student(self):
        self.assertTrue (self.__repo_studenti.__len__() == 1)

    def test_modificare_student(self):
        self.__repo_studenti.modifica_student(self.__student_nou)
        self.assertTrue (self.__repo_studenti.__len__() == 1)

        try:
            self.__repo_studenti.modifica_student(self.__student_inexistent)
            self.assertTrue(False)
        except RepoError as re:
            self.assertTrue (str(re) == 'Studentul pe care vreti sa il modificati nu exista!')

    def test_cautare_student(self):
        try:
            self.__repo_studenti.cauta_student_dupa_id(2)
            self.assertTrue(False)
        except RepoError as re:
            self.assertTrue (str(re) == "Studentul pe care il cautati nu exista in lista")

        self.__s = self.__repo_studenti.cauta_student_dupa_id(1)
        self.assertTrue(self.__s == self.__student)

    def test_stergere_student(self):
        try:
            self.__repo_studenti.sterge_student_dupa_id(2)
            self.assertTrue(False)
        except RepoError as re:
            self.assertTrue(str(re) == 'Studentul pe care doriti sa-l stergeti nu exista!')

        self.__repo_studenti.sterge_student_dupa_id(1)
        self.assertTrue(self.__repo_studenti.__len__() == 0)

    def test_adaugare_problema(self):
        self.assertTrue(self.__repo_probleme.__len__() == 1)

    def test_modificare_problema(self):
        self.__repo_probleme.modifica_problema(self.__problema_noua)
        self.assertTrue(self.__repo_probleme.__len__() == 1)

        try:
            self.__repo_probleme.modifica_problema(self.__problema_inexistenta)
            self.assertTrue(False)
        except RepoError as re:
            self.assertTrue(str(re) == 'Problema pe care vreti sa o modificati nu exista!')

    def test_cautare_problema(self):
        try:
            self.__repo_probleme.cauta_problema_dupa_nrlab_nrprob('1_2')
            self.assertTrue(False)
        except RepoError as re:
            self.assertTrue (str(re) == "Problema pe care o cautati nu exista in lista")

        self.__p = self.__repo_probleme.cauta_problema_dupa_nrlab_nrprob('1_1')
        self.assertTrue (self.__p == self.__problema)

    def test_stergere_problema(self):
        try:
            self.__repo_probleme.sterge_problema_dupa_nrlab_nrprob('1_2')
            self.assertTrue(False)
        except RepoError as re:
            self.assertTrue(str(re) == 'Problema pe care vreti sa o stergeti nu exista!')

        self.__repo_probleme.sterge_problema_dupa_nrlab_nrprob('1_1')
        self.assertTrue(self.__repo_probleme.__len__() == 0)

    def test_adaugare_nota(self):
        self.assertTrue(self.__repo_note.__len__() == 1)

    def test_stergere_nota(self):
        try:
            self.__repo_note.sterge_nota_dupa_id(2)
            self.assertTrue(False)
        except RepoError as re:
            self.assertTrue(str(re) == "Nota pe care doriti sa o stergeti nu exista!")

        self.__repo_note.sterge_nota_dupa_id(1)
        self.assertTrue(self.__repo_note.__len__() == 0)



#-------------------------------------test file------------------------------------------


class TestFileRepo(unittest.TestCase):

    def setUp(self):

        self.__file_studenti = "student_test.txt"
        self.__file_probleme = "problema_test.txt"
        self.__file_note = "nota_test.txt"


        # student
        self.__repo_studenti = FileRepoStudenti(self.__file_studenti)
        self.__student = Student(1, 'Vlad', 5)
        self.__repo_studenti.adauga_student(self.__student)
        self.__student_nou = Student(1, 'Cosmin', 10)
        self.__student_inexistent = Student(3, "Alex", 4)

        # problema
        self.__repo_probleme = FileRepoProbleme(self.__file_probleme)
        self.__problema = ProblemaLab('1_1', 'pb1', 23)
        self.__repo_probleme.adauga_problema(self.__problema)
        self.__problema_noua = ProblemaLab('1_1', "Alta_Pb", 24)
        self.__problema_inexistenta = ProblemaLab('1_2', "a", 1)

        #nota
        self.__repo_note = FileRepoNote(self.__file_note, self.__repo_studenti, self.__repo_probleme)
        self.__nota = Nota(1, self.__student, self.__problema, 10)
        self.__repo_note.adauga_nota(self.__nota)

    def tearDown(self):
        with open(self.__file_studenti, 'w') as f:
            pass
        with open(self.__file_probleme, 'w') as f:
            pass
        with open(self.__file_note, 'w') as f:
            pass

    def test_adaugare_student(self):
        self.assertTrue (self.__repo_studenti.__len__() == 1)

    def test_modificare_student(self):
        self.__repo_studenti.modifica_student(self.__student_nou)
        self.assertTrue (self.__repo_studenti.__len__() == 1)

        try:
            self.__repo_studenti.modifica_student(self.__student_inexistent)
            self.assertTrue(False)
        except RepoError as re:
            self.assertTrue (str(re) == 'Studentul pe care vreti sa il modificati nu exista!')

    def test_cautare_student(self):
        try:
            self.__repo_studenti.cauta_student_dupa_id(2)
            self.assertTrue(False)
        except RepoError as re:
            self.assertTrue (str(re) == "Studentul pe care il cautati nu exista in lista")

        self.__s = self.__repo_studenti.cauta_student_dupa_id(1)
        self.assertTrue(self.__s == self.__student)

    def test_stergere_student(self):
        try:
            self.__repo_studenti.sterge_student_dupa_id(2)
            self.assertTrue(False)
        except RepoError as re:
            self.assertTrue(str(re) == 'Studentul pe care doriti sa-l stergeti nu exista!')

        self.__repo_studenti.sterge_student_dupa_id(1)
        self.assertTrue(self.__repo_studenti.__len__() == 0)

    def test_adaugare_problema(self):
        self.assertTrue(self.__repo_probleme.__len__() == 1)

    def test_modificare_problema(self):
        self.__repo_probleme.modifica_problema(self.__problema_noua)
        self.assertTrue(self.__repo_probleme.__len__() == 1)

        try:
            self.__repo_probleme.modifica_problema(self.__problema_inexistenta)
            self.assertTrue(False)
        except RepoError as re:
            self.assertTrue(str(re) == 'Problema pe care vreti sa o modificati nu exista!')

    def test_cautare_problema(self):
        try:
            self.__repo_probleme.cauta_problema_dupa_nrlab_nrprob('1_2')
            self.assertTrue(False)
        except RepoError as re:
            self.assertTrue (str(re) == "Problema pe care o cautati nu exista in lista")

        self.__p = self.__repo_probleme.cauta_problema_dupa_nrlab_nrprob('1_1')
        self.assertTrue (self.__p == self.__problema)

    def test_stergere_problema(self):
        try:
            self.__repo_probleme.sterge_problema_dupa_nrlab_nrprob('1_2')
            self.assertTrue(False)
        except RepoError as re:
            self.assertTrue(str(re) == 'Problema pe care vreti sa o stergeti nu exista!')

        self.__repo_probleme.sterge_problema_dupa_nrlab_nrprob('1_1')
        self.assertTrue(self.__repo_probleme.__len__() == 0)

    def test_adaugare_nota(self):
        self.assertTrue(self.__repo_note.__len__() == 1)

    def test_stergere_nota(self):
        try:
            self.__repo_note.sterge_nota_dupa_id(2)
            self.assertTrue(False)
        except RepoError as re:
            self.assertTrue(str(re) == "Nota pe care doriti sa o stergeti nu exista!")

        self.__repo_note.sterge_nota_dupa_id(1)
        self.assertTrue(self.__repo_note.__len__() == 0)


#------------------------------service-------------------------------------



class TestServices(unittest.TestCase):

    def setUp(self):

        self.__file_studenti = "student_test.txt"
        self.__file_probleme = "problema_test.txt"
        self.__file_note = "nota_test.txt"

        self.__repo_studenti = FileRepoStudenti(self.__file_studenti)
        self.__repo_probleme = FileRepoProbleme(self.__file_probleme)
        self.__repo_note = FileRepoNote(self.__file_note, self.__repo_studenti, self.__repo_probleme)
        self.__validare_problema = ValidareProblema()
        self.__validare_student = ValidareStudent()
        self.__validare_nota = ValidareNota()
        # student
        self.__service_studenti = ServiceStudenti(self.__repo_studenti, self.__validare_student)
        self.__service_studenti.adauga_student_service(1, 'Vlad', 5)
        self.__service_studenti.adauga_student_service(2, 'Florin', 4)

        # problema
        self.__service_probleme = ServiceProbleme(self.__repo_probleme, self.__validare_problema)
        self.__service_probleme.adauga_problema_service('1_1', 'pb1', 23)
        self.__service_probleme.adauga_problema_service('1_2', 'pb2', 24)
        # note
        self.service_note = ServiceNote(self.__repo_note, self.__validare_nota, self.__repo_studenti,self.__repo_probleme)
        self.service_note.adauga_nota_service(1, 1, '1_1', 4)
        self.service_note.adauga_nota_service(2, 2, '1_1', 6)

    def tearDown(self):
        with open(self.__file_studenti, 'w') as f:
            pass
        with open(self.__file_probleme, 'w') as f:
            pass
        with open(self.__file_note, 'w') as f:
            pass

    def test_adaugare_student(self):
        self.assertTrue (self.__service_studenti.__len__() == 2)

    def test_modificare_student(self):
        self.__service_studenti.modifica_student_service(1, 'Cosmin', 10)
        self.assertTrue (self.__service_studenti.__len__() == 2)

        try:
            self.assertFalse(self.__service_studenti.modifica_student_service(2, "Alex", 4))
        except RepoError as re:
            self.assertTrue (str(re) == 'Studentul pe care vreti sa il modificati nu exista!')

    def test_stergere_student(self):
        try:
            self.assertFalse(self.__service_studenti.sterge_student_dupa_id_service(2))
        except RepoError as re:
            self.assertTrue (str(re) == 'Studentul pe care doriti sa-l stergeti nu exista!')

        self.__service_studenti.sterge_student_dupa_id_service(1)
        self.assertTrue (self.__service_studenti.__len__() == 0)

    def test_adaugare_problema(self):
        self.assertTrue (self.__service_probleme.__len__() == 2)

    def test_modificare_problema(self):
        self.__service_probleme.modifica_problema_service('1_1', "Alta_Pb", 24)
        self.assertTrue (self.__service_probleme.__len__() == 2)

        try:
            self.assertFalse(self.__service_probleme.modifica_problema_service('1_2', "a", 1))
        except RepoError as re:
            self.assertTrue (str(re) == 'Problema pe care vreti sa o modificati nu exista!')

    def test_stergere_problema(self):
        try:
            self.assertFalse(self.__service_probleme.sterge_problema_dupa_nrlab_nrprob_service('1_2'))
        except RepoError as re:
            self.assertTrue (str(re) == 'Problema pe care vreti sa o stergeti nu exista!')

        self.__service_probleme.sterge_problema_dupa_nrlab_nrprob_service('1_1')
        self.assertTrue (self.__service_probleme.__len__() == 0)

    def test_adauga_nota(self):
        assert (self.service_note.__len__() == 2)

    def test_stergere_student_si_note(self):
        self.service_note.sterge_student_si_notele_lui_service(1)
        assert (self.service_note.__len__() == 1)
        self.service_note.sterge_student_si_notele_lui_service(2)
        assert (self.service_note.__len__() == 0)
        #
        # # lista studenti note la prob ordonat dupa nume nota
        # self.__service_studenti.adauga_student_service(3, 'Vlad', 5)
        # self.__service_studenti.adauga_student_service(4, 'Florin', 4)
        # self.__service_probleme.adauga_problema_service('1_4', 'pb2', 24)
        #
        # self.service_note.adauga_nota_service(1, 3, '1_4', 4)
        # self.service_note.adauga_nota_service(2, 4, '1_4', 6)
        #
        # lista = self.service_note.lista_studenti_note_la_prob_ordonat_dupa_nume_nota_service("1_4")
        # assert(lista == [["Florin", 6], ["Vlad", 4]])
        #
        # #lista studenti cu media < 5
        # lista = self.service_note.lista_studenti_media_sub_5_service()
        # assert(lista == [["Vlad", 4]])




