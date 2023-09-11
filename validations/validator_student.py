from errors.exceptions import ValidationError


class ValidareStudent:

    def valideaza_student(self, student):
        """
        valideaza studentul student
        daca idul studentului student este < 0, se concateneaza la erori mesajul id invalid!\n
        daca numele studentului student este '', se concateneaza la erori mesajul nume invalid!\n
        daca grupul studentului student este < 0, se concateneaza la erori mesajul grup invalid!\n
        :param student: Student
        :return: -
        raises ValidationError daca erori != ''
        """
        erori = ""
        if student.get_id_student() < 0:
            erori += "id invalid!\n"
        if student.get_nume_student() == '':
            erori += "nume invalid!\n"
        if student.get_grup_student() < 0:
            erori += "grup invalid!\n"

        if len(erori) > 0:
            raise ValidationError(erori)
