# -*- coding -*-: utf-8
import os

from flask.ext.script import Manager
from naming import parse_name
from naming.web.app import app

@Manager
def manager(config=None):
    config = os.path.abspath(config)
    app.config.from_pyfile(config)
    print app.config
    return app


@manager.option('--name', '-n', dest='name')
def run(name):
    print name
    for e, p in parse_name(name):
        print '%s - %.2f' % (e, p * 100)


manager.add_option('-c', '--config', dest='config', required=True)


def run_manager():
    manager.run()


if __name__ == '__main__':
    run_manager()
