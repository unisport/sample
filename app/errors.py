from app import app
from flask import render_template

#Handler for 404 errors.
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404