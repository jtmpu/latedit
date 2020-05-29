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

