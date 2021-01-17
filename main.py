from __init__ import App, dir

if __name__ == '__main__':
    choice = '1'
    while choice == '1' or choice == '2':
        choice = input('1.Delete duplicates \n 2. Sort files \n 3. Exit \n[1/2/3]:')

        if choice == '1':
            App.deleteDuplicates()
        elif choice == '2':
            App.sort()
        elif choice == '3':
            break
        else:
            break
