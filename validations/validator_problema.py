from errors.exceptions import ValidationError


class ValidareProblema:

    def valideaza_problema(self, problema):
        """
                valideaza problema problema
                daca nr_lab al problemei problema este < 0, se concateneaza la erori mesajul laborator sau problema invalide!\n
                daca nr_prob al problemei problema este < 0, se concateneaza la erori mesajul laborator sau problema invalide!\n
                daca descrierea problemei problema este '', se concateneaza la erori mesajul descriere invalida!\n
                daca deadlineul problemei problema este < 0 sau > 31, se concateneaza la erori mesajul deadline invalid!\n
                :param problema: ProblemaLab
                :return: -
                raises ValidationError daca erori != ''
                """
        erori = ""
        if problema.get_nrlab_problema() < 0 or problema.get_nrprob_problema() < 0:
            erori += "laborator sau problema invalide!\n"
        if problema.get_descriere_problema() == '':
            erori += "descriere invalida!\n"
        if problema.get_deadline_problema() < 1 or problema.get_deadline_problema() > 31:
            erori += "deadline invalid!\n"

        if len(erori) > 0:
            raise ValidationError(erori)
