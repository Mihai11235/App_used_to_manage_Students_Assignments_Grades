from errors.exceptions import RepoError, ValidationError


class UI:

    def __init__(self, service_studenti, service_probleme, service_note, generare_studenti, generare_probleme):
        self.__service_studenti = service_studenti
        self.__service_probleme = service_probleme
        self.__service_note = service_note
        self.__generare_studenti = generare_studenti
        self.__generare_probleme = generare_probleme

        self.__comenzi = {
            "1" : self.__adauga_student_ui,
            "2" : self.__adauga_problema_ui,
            "3" : self.__modifica_student_ui,
            "4" : self.__modifica_problema_ui,
            "5" : self.__sterge_student_si_notele_lui_ui,
            "6" : self.__sterge_problema_dupa_nrlab_nrprob_ui,
            "7" : self.__asigneaza_si_noteaza_problema_laborator,
            "8" : self.__genereaza_studenti_random_ui,
            "9" : self.__genereaza_probleme_random_ui,
            "10": self.__lista_studenti_note_la_prob_ordonat_dupa_nume_nota_ui,
            "11": self.__lista_studenti_media_sub_5_ui,
            "12": self.__sorteaza_lab_12
        }


    @staticmethod
    def __menu():
        print(" 1: Adauga student in lista de studenti")
        print(" 2: Adauga problema in lista de probleme")
        print(" 3: Modifica student")
        print(" 4: Modifica problema")
        print(" 5: Sterge student si notele lui dupa id")
        print(" 6: Sterge problema dupa numar laborator si numar problema")
        print(" 7. Asigneaza si noteaza problema laborator")
        print(" 8: Genereaza studenti random")
        print(" 9. Genereaza probleme random")
        print("10. Lista de studenți și notele lor la o problema de laborator dat")
        print("11. Lista de studenti cu media notelor de laborator mai mica decat 5")

    def __adauga_student_ui(self):
        id, nume, grup = input("Introduceti id-ul, numele si grupul studentului pe care doriti sa-l adaugati, "
                               "separate prin cate un spatiu: ").split(maxsplit=3)
        try:
            id = int(id)
        except ValueError:
            print("Id-ul trebuie sa fie un numar intreg!")
            return

        if nume.isalpha() == False:
            print("Numele trebuie sa fie de tip string!")
            return

        try:
            grup = int(grup)
        except ValueError:
            print("Grupul trebuie sa fie un numar intreg!")
            return

        self.__service_studenti.adauga_student_service(id, nume, grup)

    def __adauga_problema_ui(self):
        try:
            nrlab_nrprob, descriere, deadline = input("Introduceti NumarLab si NumarProblema de tip int separate prin '_', "
                                                  "urmate de descrierea problemei si deadline-ul problemei, "
                                                  "separate prin cate un spatiu: ").split(maxsplit=3)
        except ValueError:
            print("Numar parametrii invalid!")
            return

        if '_' not in nrlab_nrprob:
            print("Trebuie sa fie separate prin '_' !")
            return
        try:
            nr_lab = int(nrlab_nrprob.split('_')[0])
            nrprob = int(nrlab_nrprob.split('_')[1])
        except ValueError:
            print("NumarLab si NumarProblema trebuie sa fie de tip int!")
            return

        try:
            deadline = int(deadline)
        except ValueError:
            print("Deadline-ul trebuie sa fie de tip int! ")
            return

        self.__service_probleme.adauga_problema_service(nrlab_nrprob, descriere, deadline)

    def __modifica_student_ui(self):
        id, nume, grup = input("Introduceti id-ul studentului pe care doriti sa-l modificati, urmat de numele si grupul "
                               "studentului nou, separate prin cate un spatiu: ").split(maxsplit=3)
        try:
            id = int(id)
        except ValueError:
            print("Id-ul trebuie sa fie un numar intreg!")
            return

        if nume.isalpha() == False:
            print("Numele trebuie sa fie de tip string!")
            return

        try:
            grup = int(grup)
        except ValueError:
            print("Grupul trebuie sa fie un numar intreg!")
            return

        self.__service_studenti.modifica_student_service(id, nume, grup)

    def __modifica_problema_ui(self):
        nrlab_nrprob, descriere, deadline = input("Introduceti NumarLab si NumarProblema de tip int separate prin '_', "
                                                  "urmate de descrierea problemei si deadline-ul problemei, "
                                                  "separate prin cate un spatiu: ").split(maxsplit=3)
        if '_' not in nrlab_nrprob:
            print("Trebuie sa fie separate prin '_' !")
            return
        try:
            nr_lab = int(nrlab_nrprob.split('_')[0])
            nrprob = int(nrlab_nrprob.split('_')[1])
        except ValueError:
            print("NumarLab si NumarProblema trebuie sa fie de tip int!")
            return

        try:
            deadline = int(deadline)
        except ValueError:
            print("Deadline-ul trebuie sa fie de tip int! ")
            return

        self.__service_probleme.modifica_problema_service(nrlab_nrprob, descriere, deadline)

    def __sterge_student_si_notele_lui_ui(self):
        try:
            id = int(input("Introduceti id-ul studentului pe care doriti sa-l stergeti: "))
        except ValueError:
            print("Id-ul trebuie sa fie un numar intreg!")
            return
        self.__service_note.sterge_student_si_notele_lui_service(id)


    def __sterge_problema_dupa_nrlab_nrprob_ui(self):
        nrlab_nrprob = input("Introduceti NumarLab si NumarProblema de tip int separate prin '_': ")
        if '_' not in nrlab_nrprob:
            print("Trebuie sa fie separate prin '_' !")
            return
        try:
            nr_lab = int(nrlab_nrprob.split('_')[0])
            nrprob = int(nrlab_nrprob.split('_')[1])
        except ValueError:
            print("NumarLab si NumarProblema trebuie sa fie de tip int!")
            return

        self.__service_probleme.sterge_problema_dupa_nrlab_nrprob_service(nrlab_nrprob)

    def __asigneaza_si_noteaza_problema_laborator(self):
        try:
            id_student, nrlab_nrprob, id_nota, nota = input("Introduceti id-ul studentului caruia vreti sa-i asignati laboratorul, "
                                                        "NumarLab si NumarProblema de tip int separate prin '_', "
                                                        "id-ul notei si nota, separate prin cate un spatiu: ").split(maxsplit=4)
        except ValueError:
            print("Numar parametrii invalid!")
            return
        try:
            id_student = int(id_student)
        except ValueError:
            print("Id-ul trebuie sa fie un numar intreg!")
            return

        if '_' not in nrlab_nrprob:
            print("Trebuie sa fie separate prin '_' !")
            return
        try:
            nr_lab = int(nrlab_nrprob.split('_')[0])
            nrprob = int(nrlab_nrprob.split('_')[1])
        except ValueError:
            print("NumarLab si NumarProblema trebuie sa fie de tip int!")
            return

        try:
            id_nota = int(id_nota)
        except ValueError:
            print("Id-ul trebuie sa fie un numar intreg!")
            return

        try:
            nota = int(nota)
        except ValueError:
            print("Nota trebuie sa fie de tip int!")
            return

        self.__service_note.adauga_nota_service(id_nota, id_student, nrlab_nrprob, nota)


    def __printeaza_studenti(self):
        studenti = self.__service_studenti.get_all_studenti_service()
        if studenti:
            print("Lista de studenti:\n", studenti)

    def __printeaza_problema(self):
        probleme = self.__service_probleme.get_all_probleme_service()
        if probleme:
            print("Lista de probleme:\n", probleme)

    def __printeaza_note(self, note, i):
        if i==len(note):
            return

        self.__printeaza_note(note, i+1)
        print(note[i])

    def __genereaza_studenti_random_ui(self):
        try:
            nr = int(input("Introduceti numarul de studenti care doriti sa fie generat: "))
        except ValueError:
            print("Numarul trebuie sa fie de tip int!")
            return
        self.__generare_studenti.genereaza_studenti(nr)

    def __genereaza_probleme_random_ui(self):
        try:
            nr = int(input("Introduceti numarul de probleme care doriti sa fie generate: "))
        except ValueError:
            print("Numarul trebuie sa fie de tip int!")
            return
        self.__generare_probleme.genereaza_probleme(nr)

    def __lista_studenti_note_la_prob_ordonat_dupa_nume_nota_ui(self):
        nrlab_nrprob = input("Introduceti NumarLab si NumarProblema de tip int separate prin '_': ")
        if '_' not in nrlab_nrprob:
            print("Trebuie sa fie separate prin '_' !")
            return
        try:
            nr_lab = int(nrlab_nrprob.split('_')[0])
            nrprob = int(nrlab_nrprob.split('_')[1])
        except ValueError:
            print("NumarLab si NumarProblema trebuie sa fie de tip int!")
            return

        lista_ordonata = self.__service_note.lista_studenti_note_la_prob_ordonat_dupa_nume_nota_service(nrlab_nrprob)
        if lista_ordonata:
            print(f"Lista de studenți și notele lor la o problema {nrprob} de la laboratorul {nr_lab}")
        for element in lista_ordonata:
            print(element)


    def __lista_studenti_media_sub_5_ui(self):
        lista = self.__service_note.lista_studenti_media_sub_5_service()
        print("Lista studentilor cu media sub 5:")
        for element in lista:
            print(element)




    def run(self):
        while True:

            self.__printeaza_studenti()
            self.__printeaza_problema()


            note = self.__service_note.get_all_note_service()
            note.reverse()
            self.__printeaza_note(note, 0)

            UI.__menu()

            self.__comanda = input("Introduceti varianta dorita: ")
            self.__comanda = self.__comanda.strip()

            if self.__comanda == '':
                continue
            if self.__comanda == 'exit':
                return

            if self.__comanda in self.__comenzi:
                try:
                    self.__comenzi[self.__comanda]()
                except ValueError as ve:
                    print(str(ve))
                except RepoError as re:
                    print(str(re))
                except ValidationError as ve:
                    print(str(ve))
            else:
                print('comanda invalida')

    def __sorteaza_lab_12(self):
        nrlab_nrprob = input("Introduceti NumarLab si NumarProblema de tip int separate prin '_': ")
        if '_' not in nrlab_nrprob:
            print("Trebuie sa fie separate prin '_' !")
            return
        try:
            nr_lab = int(nrlab_nrprob.split('_')[0])
            nrprob = int(nrlab_nrprob.split('_')[1])
        except ValueError:
            print("NumarLab si NumarProblema trebuie sa fie de tip int!")
            return

        lista_ordonata = self.__service_note.sorteaza_lab_12_service(nrlab_nrprob)
        if lista_ordonata:
            print(f"Lista de studenți și notele lor la o problema {nrprob} de la laboratorul {nr_lab}")
        for element in lista_ordonata:
            print(element)





