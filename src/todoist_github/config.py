from os import path

import toml

_FILE = path.expanduser(path.join("~", ".config", "todoist-github"))


def create(**kwargs):
    with open(_FILE, 'w') as f:
        toml.dump(kwargs, f)


def load():
    with open(_FILE, 'r') as f:
        config = toml.load(f)

    return config


def edit(**kwargs):
    cfg = load()
    for k, v in kwargs.items():
        if k not in cfg:
            raise ValueError("Key {} is not valid!".format(k))
        else:
            cfg[k] = v

    create(**cfg)
