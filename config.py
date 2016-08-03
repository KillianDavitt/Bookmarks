WTF_CSRF_ENABLED = True
SECRET_KEY = "RbsajdfdsfurhbRyminugtT£5rk5t5f;ERFERWE"

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'marks.sqlite')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
