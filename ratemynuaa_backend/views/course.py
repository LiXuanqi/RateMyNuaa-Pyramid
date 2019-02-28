import json

from pyramid.view import view_defaults, view_config
from sqlalchemy.orm import joinedload

from .. import models

@view_defaults(route_name='courses')
class CourseViews:
    def __init__(self, request):
        self.request = request
        self.query = self.request.dbsession.query(models.Course).options(
            joinedload(models.Course.teacher),
            joinedload(models.Course.college
        ))
    @view_config(renderer='json')
    def getCourses(self):

        return self.query.all()

    @view_config(request_param="college", renderer='json')
    def getCoursesByCollege(self):

        college = self.request.params['college']
        return self.query.filter(models.Course.college.has(name=college)).all()

    @view_config(request_param="type", renderer='json')
    def getCoursesByType(self):

        type = self.request.params['type']
        return self.query.filter_by(type=type).all()