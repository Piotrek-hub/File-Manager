from program import Program
import os
os.chdir(r'C:\Users\viral\Downloads')
dir = os.getcwd()
files = os.listdir()

App = Program(dir, files)
