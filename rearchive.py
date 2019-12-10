import subprocess
import glob
import os


root_dir = 'ROOT_DIR'
tempdir = 'TEMP_DIR'


def main():
    listArch = []

    for directory, subdirectories, files in os.walk(root_dir):
        for file in files:
            listArch.append(os.path.join(directory, file))

    for arch in listArch:
        if arch[-4:] == '.zip':
            recreate(arch)


def recreate(path):
    pathNew = path.partition('.')[0]
    command = 'tar -xf ' + path + ' -C ' + tempdir +'; cd ' + tempdir + '; tar -cpf ' + pathNew + '.7z *; rm -rf ' + tempdir + '*; rm ' + path
    subprocess.call(command, shell=True)


if __name__ == "__main__":
    main()
