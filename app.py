import os
import time
class App():

    def __init__(self, dir):
        self.dir = dir

    def sort(self):
        self.files = os.listdir()
        if 'multimediafolder' not in self.files:
            os.mkdir('multimediafolder')

        if 'appsfolder' not in self.files:
            os.mkdir('appsfolder')

        if 'zipsfolder' not in self.files:
            os.mkdir('zipsfolder')

        if 'documentsfolder' not in self.files:
            os.mkdir('documentsfolder')

        if 'instalatorsfolder' not in self.files:
            os.mkdir('instalatorsfolder')

        if 'others' not in self.files:
            os.mkdir('others')

        graphicsformats = ['.jpg', '.png', '.gif', '.mp4', '.mp3', '.jfif', '.tiff', '.jpeg', '.jps', '.bmp', '.flif', '.raw', 'xcf', '.psd', 'xmp']

        for file in self.files:

            if file[-3:] in graphicsformats or file[-4:] in graphicsformats:
                os.rename(file, f'multimediafolder/{file}')

            elif '.exe' in file:
                os.rename(file, f'appsfolder/{file}')


            elif '.pdf' in file or '.docx' in file or '.PDF' in file or '.txt' in file:
                os.rename(file, f'documentsfolder/{file}')


            elif '.msi' in file:
                os.rename(file, f'instalatorsfolder/{file}')


            elif '.zip' in file:
                os.rename(file, f'zipsfolder/{file}')

            else:
                if 'instalatorsfolder' not in file and 'documentsfolder' not in file and 'appsfolder' not in file and 'multimediafolder' not in file and 'others' not in file and 'zipsfolder' not in file and 'duplicates' not in file:
                    os.rename(file, f'others/{file}')



    def deleteDuplicates(self):
        self.files = os.listdir()
        if 'duplicates' not in self.files:
            os.mkdir('duplicates')
        for file in self.files:
            for x in range(10):
                if f'({x})' in file:
                    os.rename(file, f'duplicates/{file}')
                    break
        return True

