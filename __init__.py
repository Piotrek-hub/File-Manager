from app import App
import os
maindir = str(input('Enter the path to the folder: '))
os.chdir(rf'{maindir}')
dir = os.getcwd()
files = os.listdir()

App = App(dir)
