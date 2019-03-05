def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('courses_api', '/courses')
    config.add_route('course_api', '/courses/{course_id}')
    config.add_route('comments_api', '/courses/{course_id}/comments')