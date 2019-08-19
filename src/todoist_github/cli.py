"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mtodoist_github` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``todoist_github.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``todoist_github.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
from collections import defaultdict

import click

from .config import create, edit, _FILE
from .integrate import Integrator

main = click.Group()


@main.command()
@click.option('--github-login', default=None, type=str)
@click.option('--github-password', default=None, type=str)
@click.option('--github-token', default=None, type=str)
@click.option("--todoist-token", default=None, type=str)
def init(github_login, github_password, github_token, todoist_token):
    if (github_login is None or github_password is None) and github_token is None:
        raise ValueError(
            "You need to supply either a github login and password, or a github token!")

    if todoist_token is None:
        raise ValueError("You need to supply a todoist token!")

    if github_login:
        github = {"login": github_login, "password": github_password}
    else:
        github = {"token": github_token}

    create(github=github, todoist={"token": todoist_token})
    print("Created config file in ", _FILE)


@main.command()
@click.option('--github-login', default=None, type=str)
@click.option('--github-password', default=None, type=str)
@click.option('--github-token', default=None, type=str)
@click.option("--todoist-token", default=None, type=str)
def config(github_login, github_password, github_token, todoist_token):
    dct = defaultdict(dict)

    if github_login:
        dct['github']['login'] = github_login
    if github_password:
        dct['github']['password'] = github_password
    if github_token:
        dct['github']['token'] = github_token
    if todoist_token:
        dct['todoist']['token'] = todoist_token

    edit(**dct)
    print(f"Added {dct} to {_FILE}")


@main.command()
@click.option('-v/-V', '--verbose/--quiet', default=False)
def run(verbose):
    intg = Integrator(verbose=verbose)
    intg.sync_all()


@main.command()
@click.option("-l/-L", '--label/--no-label', default=True)
def test(label):
    """Send a small test task to todoist"""
    intg = Integrator()
    intg.test(label)
