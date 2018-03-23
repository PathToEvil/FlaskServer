import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

from FlaskServer import models, create_app

env = os.environ.get('BLOG_ENV', 'dev')
app = create_app('FlaskServer.config.%sConfig' % env.capitalize())

manager = Manager(app)
migrate = Migrate(app, models.db)

manager.add_command('server', Server())
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app,
                db=models.db,
                User=models.User,
                Post=models.Post,
                Comment=models.Comment,
                Role=models.Role,
                Tag=models.Tag,
                Server=Server)

if __name__ == '__main__':
    manager.run()
