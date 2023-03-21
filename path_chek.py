import os
import argparse

def get_filesize(size_at_bite, size_measure):
    table = {"Kb" : 1024,
             "Mb" : 1024**2,
             "Gb" : 1024**3
             }
    size = size_at_bite / table[size_measure]
    return str(size) + " " + size_measure

def show_dir(path, size_measure):
    global tab_for_lines
    try:
        for file in os.listdir(path):
            if os.path.isdir(os.path.join(path, file)):
                print("    "* tab_for_lines, os.path.basename(file))
                tab_for_lines += 1
                show_dir(os.path.join(path,file), size_measure)
                tab_for_lines -= 1
            else:
                try:
                    print("    " * tab_for_lines, os.path.basename(file), ">", get_filesize(os.path.getsize(os.path.join(path,file)), size_measure))
                except FileNotFoundError:
                    print("    " * tab_for_lines, os.path.basename(file) ,"FileNotFound")
                except PermissionError:
                    print("    " * tab_for_lines, os.path.basename(file) ,"Access Denied")

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
    show_dir(args.PATH, args.s_t)