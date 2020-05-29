#!/usr/bin/env python3

from latedit.environment import load_latedit_environment
from latedit.templates import get_jinja_environment

if __name__ == "__main__":
    lenv = load_latedit_environment()
    env = get_jinja_environment(lenv) 
    tmpl = env.get_template("table.tmpl")
    table = [{"name": "asd", "lastname & data":"asdasd"}, {"name": "qwe", "lastname & data":"qweqwe"}]
    output = tmpl.render(table=table)
    print(env)
    print(output)
