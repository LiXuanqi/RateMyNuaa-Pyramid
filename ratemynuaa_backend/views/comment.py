from pyramid.view import view_defaults, view_config
from sqlalchemy.orm import joinedload

from .. import models


@view_defaults(route_name='comments_api', renderer='json')
class CommentsViews:
    def __init__(self, request):
        self.request = request

    @view_config()
    def getCommentsByCourseId(self):
        courseId = self.request.matchdict.get('course_id')
        course = self.request.dbsession.query(models.Course).filter_by(id=courseId).first()
        return course.comments

    @view_config(request_method='POST')
    def addComment(self):
        pass

