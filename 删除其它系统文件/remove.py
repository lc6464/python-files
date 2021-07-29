from os import walk as _w
from os import remove as _rm
from os.path import join as _j


def remove(filename='.DS_Store', root='.'):
    for root, _, files in _w(root):
        for file in files:
            if file == filename:
                _rm(_j(root, file))