#!/usr/bin/env python3

import os
from jinja2 import Environment, FileSystemLoader

from latedit.encode import latex_encode
from latedit.environment import LateditEnvironment

def get_jinja_environment(env):
    """
    Creates a jinja template loading environment
    from the specified latedit environment or
    a path to the template folder
    
    Arguments
    env -- Instance of LateditEnvironment or a filepath to the template folder
    """

    target = ""
    if isinstance(env, LateditEnvironment):
        target = env.template_folder
    elif isinstance(env, str):
        target = env
    else:
        raise Exception(
            "Expected type LateditEnvironment or String, got {}"
            .format(type(env)))

    if not os.path.exists(target) or not os.path.isdir(target):
        raise Exception(
            "Template folder does not exist, target: {}"
            .format(target))
        
    file_loader = FileSystemLoader(target)
    jinjaenv = Environment(loader=file_loader)
    jinjaenv.filters["latexencode"] = latex_encode
    return jinjaenv


def list_templates(env):
    """
    List the available templates in the specified environment.
    The environment can either by a LateditEnvironment or a string

    This are simple wrappers around the functions exposed by the 
    jinja environment
    """
    j = get_jinja_environment(env)
    return j.list_templates()

def get_template(env, name):
    """
    Gets a specified template from the specified environment.
    The environment can either by a LateditEnvironment or a string
    Throws an exception if it doesn't exist.

    This are simple wrappers around the functions exposed by the 
    jinja environment
    """
    j = get_jinja_environment(env)
    if name not in j.list_templates():
        raise Exception("Tempalte '{}' not found.".format(name))

    return j.get_template(name)
