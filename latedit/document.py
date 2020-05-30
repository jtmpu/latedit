#!/usr/bin/env python3

import os
from os.path import join

from latedit.environment import DocumentEnvironment

class LatexDocument:

    def __init__(self, env):
        """
        Creates a new LatexDocument abstraction for the document
        specified by either a DocumentEnvironment or a filepath.

        Throws an exception if the argument 'env' is of invalid type,
        or if the targeted directory doesn't exist.
        """
        self.folder = ""
        if isinstance(env, str):
            self.folder = env
        elif isinstance(env, DocumentEnvironment):
            self.folder = env.root
        else:
            raise Exception(
                "LatexDocument expected type DocumentEnvironment "
                "or string. Got '{}'."
                .format(type(env)))

        if not os.path.exists(self.folder):
            raise Exception(
                "Folder does not exist '{}'"
                .format(self.folder))
    
    def get_all_texfiles(self):
        """
        Returns a list of TextFile objects for
        all identified tex-files in the document
        """ 
        files = list_files(self.folder)
        found = []
        for f in files:
            _, ext = os.path.splitext(f)
            if ext == ".tex":
                found.append(TexFile(f))
        return found

    def create_new_file(self, name, folder=""):
        """
        Creates a new tex-file for the document.
        If the folder argument is not specified, the file
        will be created in './generated'.
        
        Arguments
        name -- name of the file (.tex will be added if it's not already specified)
        folder -- a custom folder to place the file in, relative to the document root.
        """
        pass

class TexFile:
    
    def __init__(self, path):
        """
        Creates a wrapper around a tex-file,
        throws an exception if the file path does
        not exist
        """
        self.path = path
        if not os.path.exists(self.path):
            raise Exception(
                "Filepath for tex-file does not exist. '{}'"
                .format(self.path))

    def get_contents(self):
        with open(self.path, "r") as f:
            data = f.read()
        return data

def list_files(path):
    """
    Recursively retrieves all files starting from
    the root path
    """

    found = []
    for root, dirs, files in os.walk(path):
        for f in files:
            found.append(join(root, f))
    return found
