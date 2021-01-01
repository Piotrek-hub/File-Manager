from program import Program
import os
maindir = str(input('Podaj ścieżkę do pliku: '))
os.chdir(rf'{maindir}')
dir = os.getcwd()
files = os.listdir()

App = Program(dir, files)
