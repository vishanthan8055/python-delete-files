import os

def delete(sub):
    for i in range(len(lst)):
        s = lst[i]
        ran = len(s) - len(sub)
        for i in range(ran + 1):
            if s[i:i + (len(sub))] == sub:
                fpath = root + '/' + s
                os.remove(fpath)
                print(s)

# driver code
path = input("Enter Path: ")
sub = input("enter substring: ")
print("Deleted Files: ")
for (root,dirs,files) in os.walk(path):
        lst=files
        if len(lst) != 0:
                delete(sub)

