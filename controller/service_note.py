from domain.nota import Nota
from sortare.sortari import sortare, compara


class ServiceNote:

    def __init__(self, repo_note, validator_nota, repo_studenti, repo_probleme):
        """
        Folosind injectia de dependenta, membrul privat __repo_probleme este initializat cu obiectul repo_probleme al
        clasei RepoProbleme
        Folosind injectia de dependenta, membrul privat __repo_studenti este initializat cu obiectul
        repo_studenti al clasei RepoStudenti
        Folosind injectia de dependenta, membrul privat __repo_note este initializat cu obiectul
        repo_note al clasei RepoNote
        Folosind injectia de dependenta, membrul privat __validator_nota este initializat cu obiectul
        validator_nota al clasei ValidareNota
        :param repo_note: RepoNote
        :param validator_nota: ValidatorNota
        :param repo_studenti: RepoStudenti
        :param repo_probleme: RepoProbleme
        """
        self.__repo_note = repo_note
        self.__validator_nota = validator_nota
        self.__repo_studenti = repo_studenti
        self.__repo_probleme = repo_probleme

    def adauga_nota_service(self, id_nota, id_student, nrlab_nrprob, nota):
        """

        :param id_nota:
        :param id_student:
        :param nrlab_nrprob:
        :param nota:
        :return:
        """
        student = self.__repo_studenti.cauta_student_dupa_id(id_student)
        problema = self.__repo_probleme.cauta_problema_dupa_nrlab_nrprob(nrlab_nrprob)

        self.__nota = Nota(id_nota, student, problema, nota)
        self.__validator_nota.valideaza_nota(self.__nota)
        self.__repo_note.adauga_nota(self.__nota)

    def sterge_student_si_notele_lui_service(self, id_student):
        note = self.__repo_note.get_all()
        for nota in note:
            if nota.get_student().get_id_student() == id_student:
                self.__repo_note.sterge_nota_dupa_id(nota.get_id_nota())
        self.__repo_studenti.sterge_student_dupa_id(id_student)

    def lista_studenti_note_la_prob_ordonat_dupa_nume_nota_service(self, nrlab_nrprob):
        lista = []
        note = self.__repo_note.get_all()
        for nota in note:
            if nota.get_problema().get_nrlab_nrprob_problema() == nrlab_nrprob:
                student = nota.get_student()
                valoare_nota = nota.get_nota()
                lista.append([student.get_nume_student(), valoare_nota])

        #lista.sort(key = lambda x:(x[0], x[1]))
        lista = sortare(lista, 'shell_sort', key = lambda x:(x[0], x[1]))
        #(x[0], x[1]) e un tuplu pe care l returnez, si compara primele elemente, dupa care trece la urmatoarele
        return lista

    def get_all_note_service(self):
        note2=[]
        note = self.__repo_note.get_all()
        for nota in note:
            student = nota.get_student()
            problema = nota.get_problema()
            nota_obtinuta = nota.get_nota()
            note2.append(f"Studentul cu id-ul {student.get_id_student()}, numele {student.get_nume_student()}, "
                        f"din grupa {student.get_grup_student()} a obtinut nota {nota_obtinuta} "
                        f"la problema {problema.get_nrprob_problema()} de la laboratorul {problema.get_nrlab_problema()}, "
                        f"cu descrierea '{problema.get_descriere_problema()}' si deadline-ul {problema.get_deadline_problema()}")
        return note2



    def lista_studenti_media_sub_5_service(self):
        studenti = {}
        note = self.__repo_note.get_all()

        for nota in note:
            student = nota.get_student()
            if student.get_id_student() not in studenti:
                studenti[student.get_id_student()] = []
            studenti[student.get_id_student()].append(nota.get_nota())

        lista = []
        for id_student in studenti:
            medie = sum(studenti[id_student])/len(studenti[id_student])
            if medie < 5:
                student = self.__repo_studenti.cauta_student_dupa_id(id_student)
                lista.append([student.get_nume_student(), medie])

        return lista

    def __len__(self):
        return self.__repo_note.__len__()

    def sorteaza_lab_12_service(self, nrlab_nrprob):
        lista = []
        note = self.__repo_note.get_all()
        for nota in note:
            if nota.get_problema().get_nrlab_nrprob_problema() == nrlab_nrprob:
                student = nota.get_student()
                valoare_nota = nota.get_nota()
                lista.append([student.get_nume_student(), valoare_nota])


        lista = sortare(lista, 'bubble_sort', key=lambda x: (x[1], x[0]), cmp = compara)
        return lista
