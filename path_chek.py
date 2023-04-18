import os
import argparse

class MyPrefix(list):
    def __repr__(self) -> str:
        res = ""
        for i in range(len(self)):
            res += str(self.__getitem__(i))
        return res
    def __str__(self) -> str:
        res = ""
        for i in range(len(self)):
            res += str(self.__getitem__(i))
        return res
    
line_to_obj = "|----"
empty_line =  "     "
slash_line =  "|    "

def show_dir(path,prefix):
    try:
        dirlist = os.listdir(path)
        for file in range (len(dirlist)):
            if os.path.isdir(os.path.join(path, dirlist[file])):   
                    prefix.append(line_to_obj)
                    print(str(prefix) + os.path.basename(dirlist[file]))
                    prefix.pop()                  
                    if file == len(dirlist) - 1:
                        prefix.append(empty_line)
                    else:
                        prefix.append(slash_line)
                    show_dir(os.path.join(path,dirlist[file]),prefix)
                    prefix.pop()

            else:
                prefix.append(line_to_obj)
                try:                    
                    print(str(prefix) +  os.path.basename(dirlist[file]) + "  " + str(os.path.getsize(os.path.join(path,dirlist[file])) / 1024 / 1024), "Mb")
                except FileNotFoundError:
                    print(str(prefix) + os.path.basename(dirlist[file]) +" FileNotFound")
                except PermissionError:
                    print(str(prefix) + os.path.basename(dirlist[file]) + " PermissionDenied")
                prefix.pop()

    except FileNotFoundError:
        print(str(prefix) + path, "DirectoryNotFound")
    except PermissionError:
        print(str(prefix) + path, "Access Denied")       
    except OSError:
        pass
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-path","--PATH",required=True)
    args = parser.parse_args()
    print(args.PATH)
    show_dir(args.PATH, MyPrefix())