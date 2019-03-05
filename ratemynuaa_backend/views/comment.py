from pyramid.view import view_defaults, view_config
from sqlalchemy.orm import joinedload

from .. import models


@view_defaults(route_name='comments_api')
class CommentsViews:
    def __init__(self, request):
        self.request = request
    @view_config(renderer='json')
    def getCommentsByCourseId(self):
        courseId = self.request.matchdict.get('course_id')
        # return self.query.filter(models.Course.college.has(name=college)).all()
        course = self.request.dbsession.query(models.Course).filter_by(id=courseId).first()
        return course.comments


