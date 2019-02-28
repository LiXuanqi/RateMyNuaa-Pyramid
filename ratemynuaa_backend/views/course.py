import json

from pyramid.view import view_defaults, view_config

from .. import models

@view_defaults(route_name='courses')
class CourseViews:
    def __init__(self, request):
        self.request = request

    @view_config(renderer='json')
    def getCourses(self):

        query = self.request.dbsession.query(models.Course)
        one = query.all()

        return [1,2,3]