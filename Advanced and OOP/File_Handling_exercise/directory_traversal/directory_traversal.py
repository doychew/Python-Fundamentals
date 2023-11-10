import os

files = {}
directory = input()


def get_files(folder):

    for element in os.listdir(folder):
        f = os.path.join(folder, element)
        if os.path.isfile(f):
            extension = element.split(".")[-1]
            if extension not in files:
                files[extension] = []
            files[extension].append(element)
        else:
            get_files(f)


get_files(directory)

with open(os.path.join(directory, 'report.txt'), 'w') as output_file:
    for ext, f_names in sorted(files.items()):
        output_file.write(f".{ext}\n")
        for f_name in sorted(f_names):
            output_file.write(f"- - - {f_name}\n")
