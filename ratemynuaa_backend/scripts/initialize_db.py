import argparse
import sys

from pyramid.paster import bootstrap, setup_logging
from sqlalchemy.exc import OperationalError

from .. import models


def setup_models(dbsession):
    """
    Add or update models / fixtures in the database.

    """
    college1 = models.college.College(id=1, name='航空宇航学院')
    college2 = models.college.College(id=2, name='能源与动力学院')
    college3 = models.college.College(id=3, name='自动化学院')
    dbsession.add(college1)
    dbsession.add(college2)
    dbsession.add(college3)

    teacher1 = models.teacher.Teacher(name='大李', college=college2)
    teacher2 = models.teacher.Teacher(name='大王', college=college2)
    dbsession.add(teacher1)
    dbsession.add(teacher2)

    course1 = models.course.Course(name="航空航天概论", course_number="N32413", type="optional", college=college1, teacher=teacher1)
    course2 = models.course.Course(name="航空发动机原理", course_number="N32433", type="compulsory", college=college2, teacher=teacher2)
    course3 = models.course.Course(name="自动控制原理", course_number="N32253", type="compulsory", college=college3, teacher=teacher2)
    course4 = models.course.Course(name="西方经济学", course_number="N42253", type="optional", college=college2, teacher=teacher1)

    dbsession.add(course1)
    dbsession.add(course2)
    dbsession.add(course3)
    dbsession.add(course4)

def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'config_uri',
        help='Configuration file, e.g., development.ini',
    )
    return parser.parse_args(argv[1:])


def main(argv=sys.argv):
    args = parse_args(argv)
    setup_logging(args.config_uri)
    env = bootstrap(args.config_uri)

    try:
        with env['request'].tm:
            dbsession = env['request'].dbsession
            setup_models(dbsession)
    except OperationalError:
        print('''
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for description and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.
            ''')
