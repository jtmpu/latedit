#!/usr/bin/env python3

import os

from latedit.environment import DocumentEnvironment

def list_files(path):
    """
    Recursively retrieves all files starting from
    the root path
    """
    nodes = os.listdir(path)
    nodes = map(lambda x: os.path.join(path, x), nodes)
    files = filter(lambda x: os.path.isfile(x), nodes)
    dirs = filter(lambda x: os.path.isdir(x), nodes)
    childfiles = map(lambda x: list_files(path, x), dirs)
    flatten = lambda l: [item for sublist in l for item in sublist]
    
    return files.extend(flatten(childfiles))
    


def list_texfiles(docenv):
    """
    Recursively retrieves the path for all texfiles 
    in the document
    """
    if not isinstance(docenv, DocumentEnvironment):
        err = "list_textfiles expected type DocumentEnvironment, received: {}"
        err = err.format(type(docenv))
        raise Exception(err)

    path = docenv.root
    files = list_files(path)
    ret = filter(lambda x: x.endswith(".tex"), files)
    return ret

def list_texfiles_by_path(path):
    """
    Recursively retrieves the path for all texfiles 
    in a path
    """
