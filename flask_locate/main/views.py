"""
The main public routes to view the site
"""

from flask import (render_template,
                   current_app)
from . import main

@main.route('/')
def index():
    """
    Index page for the site
    """
    current_app.logger.debug('Index page')
    return render_template('index.html')
