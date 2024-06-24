import shelve
from pathlib import Path
import sys
import os

CURRENT_DIR = Path(sys.argv[0]).parent
FILE = os.path.join(CURRENT_DIR, 'resources', 'generated', 'shelf_file')

if __name__ == '__main__':
    shelf_file = shelve.open(FILE)
    shelf_file['names'] = ['Max', 'Tomas', 'Rocky']
    shelf_file.close()

    shelf_file = shelve.open(FILE)

    for name in shelf_file['names']:
        print(name)

    shelf_file.close()