#!/usr/bin/env python3

import os
import configparser

DEFAULT_ENV_FOLDER = os.path.join(os.path.expanduser("~"), ".latedit")
DEFAULT_CONFIG_PATH = os.path.join(DEFAULT_ENV_FOLDER, "config")

class DocumentEnvironment:

    def __init__(self):
        self.root = "" 
    
    def to_dict(self):
        return { "rootFolder" : self.root }


def load_document_environment():
    """
    Creates a document environment based on
    the configuration in the default location.
    """
    if not config_exists():
        raise ConfigNotFoundException()
    
    config = configparser.ConfigParser()
    config.read(DEFAULT_CONFIG_PATH)

    root = ""
    if "document" in config:
        root = config["document"].get("rootFolder", "")

    ret = DocumentEnvironment()
    ret.root = root
    return ret

def create_default_document_environment():
    """
    Creates a default document environemnt.
    """
    ret = DocumentEnvironment()
    ret.root = os.path.join(DEFAULT_ENV_FOLDER, "example")
    return ret

class LateditEnvironment:

    def __init__(self):
        self.template_folder = ""

    def to_dict(self):
        return { "templateFolder" : self.template_folder }

def load_latedit_environment():
    """
    Creates a latedit environment based on
    the configuration in the default location.
    """
    if not config_exists():
        raise ConfigNotFoundException()

    config = configparser.ConfigParser()
    config.read(DEFAULT_CONFIG_PATH)
    
    template_folder = ""
    if "latedit" in config:
        template_folder = config["latedit"].get("templateFolder", "")

    ret = LateditEnvironment()
    ret.template_folder = template_folder

    return ret

def create_default_latedit_environment():
    ret = LateditEnvironment()
    ret.template_folder = os.path.join(DEFAULT_ENV_FOLDER, "templates")
    return ret

class ConfigNotFoundException(Exception):
    """
    Raised when config file does not exist.
    """
    pass

def config_exists():
    return os.path.exists(DEFAULT_CONFIG_PATH)

def generate_default_config():
    """
    Generates an empty default config, creates the
    necessary folders and the config file and saves
    it.
    """
    if not os.path.exists(DEFAULT_ENV_FOLDER):
        os.mkdir(DEFAULT_ENV_FOLDER)

    config = configparser.ConfigParser()
    config["latedit"]  = create_default_latedit_environment().to_dict()
    config["document"] = create_default_document_environment().to_dict()
    with open(DEFAULT_CONFIG_PATH, "w") as f:
        config.write(f)
