import os
#os.system('open -a notes')
#os.system('open -a Calculator')
#os.system('mkdir Ram')
#os.system('rmdir Ram')
'''for i in range (1,11):
    path = "/Users/aryanyadav/Documents/demo pp/"
    folder_name='Shyam'+str(i)
    t=(path+folder_name)
    create_folder='mkdir '+t
    os.system(create_folder)

path = "/Users/aryanyadav/Docum
for i in range(, 11):
    folder_name = "Shyam" + str(i)
    os.mkdir(path + folder_name)
'''
# to see the current working directory
print(os.getcwd())
os.chdir('/Users/aryanyadav/Documents/demo pp')
print(os.getcwd())

x = (os.listdir())
for item in x:
    print(item)

lst=os.walk('/Users/aryanyadav/Documents/demo pp')
for root_path,dir,files in lst:
    print('root_path=',root_path)
    print('directories=',dir)
    print('files=',files)
    print()