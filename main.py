import os

path=input("Enter Path: ")
lst = os.listdir(path)

sub= input("enter substring: ")
print(lst)

for i in range(len(lst)):
    s = lst[i]
    ran = len(s) - len(sub)
    for i in range(ran + 1):
        if s[i:i + (len(sub))] == sub:
            print(s)
            fpath = path + '/' + s
            os.remove(fpath)
