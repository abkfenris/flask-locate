#!/usr/bin/env python
import os
COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='flask_locate/*')
    COV.start()

from flask.ext.script import Manager, Shell

from flask_locate import create_app
import config

if os.environ.get('LOCATE_FLASK_ENV') == 'prod':
    app = create_app('production')
else:
    app = create_app('default')

manager = Manager(app)

@manager.command
def listroutes():
    """
    List routes for app
    """
    import urllib

    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint,
                                                        methods,
                                                        rule))
        output.append(line)

    for line in sorted(output):
        print(line)

if __name__ == '__main__':
    manager.run()
