import os
import argparse

def size_type(path, file, size_info):
    table = {}
    table["Kb"] = os.path.getsize(os.path.join(path,file)) / 1024
    table["Mb"] = os.path.getsize(os.path.join(path,file)) / 1024 / 1024
    table["Gb"] = os.path.getsize(os.path.join(path,file)) / 1024 / 1024 / 1024
    return str(table[size_info]) +" " + size_info

def show_dir(path, size_info):
    global tab_for_lines
    try:
        for file in os.listdir(path):
            if os.path.isdir(os.path.join(path, file)):
                print("    "* tab_for_lines, os.path.basename(file))
                tab_for_lines += 1
                show_dir(os.path.join(path,file), size_info)
                tab_for_lines -= 1
            else:
                try:
                    print("    " * tab_for_lines, os.path.basename(file), ">", size_type(path, file, size_info))
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
    size_info = ""
    size_info += args.s_t
    show_dir(args.PATH, size_info)