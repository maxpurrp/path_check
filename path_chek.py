import os
import argparse

def size_type(path, q):
    if args.s_t == "Kb":
        x = os.path.getsize(os.path.join(path,q)) / 1024
        return str(x) + " Kb"
    elif args.s_t == "Mb":
        x = os.path.getsize(os.path.join(path,q)) / 1024 / 1024
        return str(x) + " Mb"
    elif args.s_t == "Gb":
        x = os.path.getsize(os.path.join(path,q)) / 1024 / 1024 / 1024
        return str(x) + " Gb"

def show_dir(path):
    global tab_for_lines
    try:
        for q in os.listdir(path):
            if os.path.isdir(os.path.join(path, q)):
                print("    "* tab_for_lines, os.path.basename(q))
                tab_for_lines += 1
                show_dir(os.path.join(path,q))
                tab_for_lines -= 1
            else:
                try:
                    print("    " * tab_for_lines, os.path.basename(q), ">", size_type(path, q))
                except FileNotFoundError:
                    print("    " * tab_for_lines, os.path.basename(q) ,"FileNotFound")
                except PermissionError:
                    print("    " * tab_for_lines, os.path.basename(q) ,"Access Denied")

    except FileNotFoundError:
        print("    "* tab_for_lines, path, "DirectoryNotFound")
    except PermissionError:
        print("    "* tab_for_lines, path, "Access Denied")
    except OSError:
        pass

if __name__ == "__main__":
    tab_for_lines = 0
    parser = argparse.ArgumentParser()
    parser.add_argument("-path", "--PATH",required=True)
    parser.add_argument("--s_t","--size_type", default = "Mb", choices=["Kb", "Mb", "Gb"])
    args = parser.parse_args()
    show_dir(args.PATH)