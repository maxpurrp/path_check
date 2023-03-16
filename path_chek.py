import os
import argparse

def show_dir(path):
    global lvl_in
    try:
        for q in os.listdir(path):
            if os.path.isdir(os.path.join(path, q)):
                if lvl_in == 0:
                    print(("|"+ ("     ")* lvl_in) + "----" +  os.path.basename(q))
                else:
                    print(("|"+ "     "* lvl_in) +"|" + "----" +  os.path.basename(q))
                lvl_in += 1
                show_dir(os.path.join(path,q))
                lvl_in -= 1
            else:
                try:
                    if lvl_in == 0:
                        print("|"+ "     "* lvl_in + "----" + os.path.basename(q) + ">", os.path.getsize(os.path.join(path,q)) / 1024 / 1024, "Mb")
                    else:
                        print("|"+ "     "* lvl_in + "|----" + os.path.basename(q) + ">", os.path.getsize(os.path.join(path,q)) / 1024 / 1024, "Mb")
                except FileNotFoundError:
                    print("|"+ "     "* lvl_in + os.path.basename(q) + ">", "fileNotFound")
                except PermissionError:
                    print("|"+ "     "* lvl_in + os.path.basename(q) + ">", "PermissionDenied")

    except FileNotFoundError:
        print(("|"+ "     "* lvl_in) + "----", path, "DirectoryNotFound")
    except PermissionError:
        print(("|"+ "     "* lvl_in) + "----", path, "Access Denied")       
    except OSError:
        pass

if __name__ == "__main__":
    lvl_in = 0
    parser = argparse.ArgumentParser()
    parser.add_argument("-path","--PATH",required=True)
    args = parser.parse_args()
    show_dir(args.PATH)
