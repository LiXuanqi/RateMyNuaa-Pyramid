from pyramid.config import Configurator
from pyramid.renderers import JSON


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('.models')
        config.include('pyramid_jinja2')
        config.include('.routes', route_prefix='/api')
        config.scan()

    return config.make_wsgi_app()

def config_renderer(config):
    json_renderer = JSON()
    # - add adapters bellow.
    # eg: json_renderer.add_adapter(Car, lambda c, _: c.to_dict())
    config.add_renderer('json', json_renderer)