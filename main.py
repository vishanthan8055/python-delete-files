import os

def delete(sub):
    for i in range(len(lst)):
        s = lst[i]
        ran = len(s) - len(sub)
        for i in range(ran + 1):
            if s[i:i + (len(sub))] == sub:
                fpath = path + '/' + s
                os.remove(fpath)
                print(s,"is deleted sucessfully")

path=input("Enter Path: ")
lst = os.listdir(path)
print(lst)
sub= input("enter substring: ")
delete(sub)