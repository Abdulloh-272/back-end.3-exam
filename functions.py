import os

def students(**kw):
    counter = 0
    with open(file='students.txt',mode='a') as file:
        for x,y in kw.items():
            counter +=1
            if counter ==3:
                file.write(f'{x}: {y}\n')
                file.write('\n')
                counter = 0
            else:
                file.write(f'{x}: {y}\n')

def read_students():
    with open(file='students.txt',mode='r') as file:
        st_read = file.read()
        print(st_read)

def delate_file():
    with open(file='students.txt',mode='w') as file:
        file.write('')