"""This is a Flask App that allows for web based user database interaction"""

from flask import Flask
from ProductionCode import data_processor

app = Flask(__name__)

@app.route('/')
def homepage():
    """Creates a home page that has user instructions"""
    return "Hello, this is the homepage. " \
    "To find the frequency of meeting attended please do (url)/meeting/[frequency, count]"

@app.errorhandler(404)
def page_not_found(e):
    """Makes a page for the user when an incorrect url is given"""
    return str(e)+" Sorry, wrong format, do this instead (url)/meeting/[frequency, count]"

@app.errorhandler(500)
def python_bug(e):
    """Makes a page when there is a bug in the underlying python code"""
    return "Eek, a bug: "+str(e)

@app.route('/meeting/frequency', strict_slashes=False)
def get_meeting_freq():
    """Makes a page that runs when a user request is given for meeting data"""
    freq = data_processor.meeting_frequency()
    return "The average percentage of meetings attended is "+str(freq)+"%"

@app.route('/meeting/count', strict_slashes=False)
def get_meeting_count():
    """Makes a page that runs when a user request is given for meeting data"""
    count = data_processor.meeting_count()
    return "The average number of meetings attended is "+str(count)

if __name__ == '__main__':
    app.run()
