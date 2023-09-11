from errors.exceptions import ValidationError


class ValidareNota:

    def valideaza_nota(self, nota):
        """
        valideaza nota nota
        daca id_nota < 0 se concateneaza la stringul de erori mesajul "id invalid!\n"
        daca nota < 1 sau nota > 10 se concateneaza la stringul de erori "nota invalida!\n"
        :param nota: Nota
        :return:
        raises ValidationError daca erori != ''
        """

        erori=''

        if nota.get_id_nota() < 0:
            erori += 'id invalid!\n'
        if nota.get_nota() < 1 or nota.get_nota() > 10:
            erori += 'nota invalida!\n'

        if erori != '':
            raise ValidationError(erori)