#from jinja2 import nodes
#from jinja2.ext import Extension

import re
from jinja2 import environment, contextfilter, Markup, escape


@contextfilter
def islocaluri(ctx,uri):
    """ filter to check if a uri is local to the current document context"""
    return uri.startswith(ctx.get('uri','XXX'))

def register_filters(env):
    """ convenience method because pylode doesnt reuse environments """
    # env.environment.filters['islocaluri'] = islocaluri
    environment.DEFAULT_FILTERS['islocaluri'] = islocaluri
    return env
