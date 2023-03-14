import os
import argparse

def show_dir(path):
    global tab_for_files, tab_for_dir
    try:
        for q in os.listdir(path):
            if os.path.isdir(os.path.join(path, q)):
                tab_for_dir += 1
                print("    "* tab_for_dir, os.path.basename(q))
                tab_for_files += 1
                show_dir(os.path.join(path,q))
                tab_for_files -= 1
                tab_for_dir -= 1
            else:
                try:
                    print("    " * tab_for_files, os.path.basename(q), ">", os.path.getsize(os.path.join(path,q)) / 1024 / 1024, "Mb")
                except FileNotFoundError:
                    print("    " * tab_for_files, os.path.basename(q) ,"FileNotFound")
                except PermissionError:
                    print("    " * tab_for_files, os.path.basename(q) ,"Access Denied")

    except FileNotFoundError:
        print("    "* tab_for_dir, path, "DirectoryNotFound")
    except PermissionError:
        print("    "* tab_for_dir, path, "Access Denied")
    except OSError:
        pass

if __name__ == "__main__":
    tab_for_files = 1
    tab_for_dir = 0
    parser = argparse.ArgumentParser()
    parser.add_argument("-path","--PATH",required=True)
    args = parser.parse_args()
    show_dir(args.PATH)