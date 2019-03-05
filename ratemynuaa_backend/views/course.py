from pyramid.view import view_defaults, view_config
from sqlalchemy.orm import joinedload

from .. import models


@view_defaults(route_name='courses_api', renderer='json')
class CoursesViews:
    def __init__(self, request):
        self.request = request
        self.query = self.request.dbsession.query(models.Course).options(
            joinedload(models.Course.teacher),
            joinedload(models.Course.college
        ))
    @view_config()
    def getCourses(self):

        return self.query.all()

    @view_config(request_param="college")
    def getCoursesByCollege(self):

        college = self.request.params['college']
        return self.query.filter(models.Course.college.has(name=college)).all()

    @view_config(request_param="type")
    def getCoursesByType(self):

        targetType = self.request.params['type']
        return self.query.filter_by(type=targetType).all()


@view_defaults(route_name='course_api', renderer='json')
class CourseViews:
    def __init__(self, request):
        self.request = request

    @view_config()
    def getCourse(self):
        courseId = self.request.matchdict['course_id']
        return self.request.dbsession.query(models.Course).options(
                joinedload(models.Course.teacher),
                joinedload(models.Course.college
            )).filter_by(id=courseId).first()

    @view_config(request_method='POST')
    def addCourse(self):
        pass

    @view_config(request_method='DELETE')
    def deleteCourse(self):
        pass