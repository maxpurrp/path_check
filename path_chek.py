import os
import argparse

def show_dir(path):
    global tab_for_words
    try:
        for q in os.listdir(path):
            if os.path.isdir(os.path.join(path, q)):
                if tab_for_words == 0:
                    print("|", "----",  os.path.basename(q))
                    tab_for_words += 1
                    show_dir(os.path.join(path,q))
                    tab_for_words -= 1
                else:
                    print("|", ("     "+ "|")* tab_for_words, "----",  os.path.basename(q))
                    tab_for_words += 1
                    show_dir(os.path.join(path,q))
                    tab_for_words -= 1
            else:
                try:
                    if tab_for_words == 0:
                        print("|", "    "* tab_for_words,  os.path.basename(q), ">", os.path.getsize(os.path.join(path,q)) / 1024 / 1024, "Mb")
                    else:
                        print("|", ("     "+ "|")* tab_for_words,"  ",  os.path.basename(q), ">", os.path.getsize(os.path.join(path,q)) / 1024 / 1024, "Mb")
                except FileNotFoundError:
                        print("|", "   "* tab_for_words,"|",  "----" * tab_for_words, os.path.basename(q), ">", os.path.getsize(os.path.join(path,q)) / 1024 / 1024, "Mb")
                except PermissionError:
                        print("|", "   "* tab_for_words,"|",  "----" * tab_for_words, os.path.basename(q), ">", os.path.getsize(os.path.join(path,q)) / 1024 / 1024, "Mb")

    except FileNotFoundError:
        if tab_for_words == 0:
            print("|", "----", path, "DirectoryNotFound")
        else:
            print("|", ("     "+ "|")* tab_for_words, "----", path, "DirectoryNotFound")
    except PermissionError:
        if tab_for_words == 0:
            print("|", "----", path, "Access Denied")
        else:
            print("|", ("     "+ "|")* tab_for_words, "----", path, "Access Denied")       
    except OSError:
        pass

if __name__ == "__main__":
    tab_for_words = 0
    parser = argparse.ArgumentParser()
    parser.add_argument("-path","--PATH",required=True)
    args = parser.parse_args()
    show_dir(args.PATH)
