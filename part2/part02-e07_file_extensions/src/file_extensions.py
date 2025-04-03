#!/usr/bin/env python3

def file_extensions(filename):

    files_no_ext = []
    ext_dict = {}

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if '.' in line and line.rfind('.') != 0:
                name, ext = line.rsplit('.', 1)
                if ext in ext_dict:
                    ext_dict[ext].append(line)
                else:
                    ext_dict[ext] = [line]
            else:
                files_no_ext.append(line)
    
    return files_no_ext, ext_dict

def main():
    filename = 'src/filenames.txt' # path to file
    files_no_ext, ext_dict = file_extensions(filename) # calling method

    print(f"{len(files_no_ext)} files with no extension")

    for ext in sorted(ext_dict):
        print(f"{ext} {len(ext_dict[ext])}")

if __name__ == "__main__":
    main()
