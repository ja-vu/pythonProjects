import os
import shutil

path = 'C:/Users/james/Downloads'

actions = {
    'zip': ['.zip'],
    'videos': ['.mp4'],
    'photos': ['.jpeg', '.jpg', '.png', '.gif'],
    'docs': ['.pdf', '.doc', '.docx', '.xlsx'],
    'others': ['.exe', '.tmp', '.jar', '.msi']
}


def create_folders():
    for name in actions:
        ext_path = os.path.join(path, name)
        try:
            os.mkdir(ext_path)
        except OSError:
            print("Creation of the directory '%s' failed" % ext_path)
        else:
            print("Successfully created the directory %s " % ext_path)


def move_files():
    files = os.listdir(path)

    for destination, extensions in actions.items():
        for ext in extensions:
            for f in files:
                f_path = os.path.join(path, f)
                if f.endswith(ext):
                    print("Moving......" + f)
                    shutil.move(f_path, os.path.join(path, destination))
                else:
                    continue
    print("No more files to move")


if __name__ == "__main__":
    create_folders()
    move_files()
