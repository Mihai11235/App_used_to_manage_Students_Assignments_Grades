import unittest

from controller.service_studenti import ServiceStudenti
from controller.service_probleme import ServiceProbleme
from controller.service_note import ServiceNote
from generari.generare_probleme import GenerareProbleme
from generari.generare_studenti import GenerareStudenti
from infrastructure.file_repo_note import FileRepoNote
from infrastructure.file_repo_probleme import FileRepoProbleme
from infrastructure.file_repo_studenti import FileRepoStudenti
from infrastructure.repo_studenti import RepoStudenti
from infrastructure.repo_probleme import RepoProbleme
from infrastructure.repo_note import RepoNote
from presentation.ui import UI
from testing.test_ import TestDomain
from validations.validator_student import ValidareStudent
from validations.validator_problema import ValidareProblema
from validations.validator_nota import ValidareNota


def main():
    # teste = Teste()
    # teste.ruleaza_toate_testele()
    # teste=TestDomain()
    # teste.ruleaza_teste_domain()

    validator_student = ValidareStudent()
    validator_problema = ValidareProblema()
    validator_nota = ValidareNota()

    file_studenti = 'studenti.txt'
    repo_studenti = FileRepoStudenti(file_studenti)
    file_probleme = 'probleme.txt'
    repo_probleme = FileRepoProbleme(file_probleme)
    file_note = 'note.txt'
    repo_note = FileRepoNote(file_note, repo_studenti, repo_probleme)

    service_studenti = ServiceStudenti(repo_studenti, validator_student)
    service_probleme = ServiceProbleme(repo_probleme, validator_problema)
    service_note = ServiceNote(repo_note, validator_nota, repo_studenti, repo_probleme)

    generare_studenti = GenerareStudenti(service_studenti)
    generare_probleme = GenerareProbleme(service_probleme)

    consola = UI(service_studenti, service_probleme, service_note, generare_studenti, generare_probleme)
    consola.run()

main()
