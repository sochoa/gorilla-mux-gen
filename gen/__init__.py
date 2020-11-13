import argparse
import jinja2
import os
import gen.filters as gen_filters

class Resource:
    def __init__(self, n):
        self.name = n
        self.members = []


class Member:
    def __init__(self, n, t):
        self.name = n
        self.type = t


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("member", nargs="*")
    args = parser.parse_args()
    loader = jinja2.FileSystemLoader(os.getcwd())
    env = jinja2.Environment(autoescape=True, loader=loader)
    env.filters.update(gen_filters.filters)
    r = Resource(args.name)
    for m in args.member:
        n, t = m.split(':')
        r.members.append(Member(n, t))

    tmpl = env.get_template('templates/resource.go.jinja2')
    print(tmpl.render(resource=r))

