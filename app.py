"""This is a Flask App that allows for web based user database interaction"""

from flask import Flask, render_template
from ProductionCode.datasource import DataSource

app = Flask(__name__)

@app.route('/')
def homepage():
    """Creates a home page that has user instructions"""
    return 'Hello! Welcome to our website with the amazingly' \
        'curated title: Analyzing Criminal Drug Abuse Treatment in Females' \
        '\nAlso known as drug_abuse_treatment.py' \
        '\n' \
        '\n' \
        'Here are the main directories of our program for your research/interests: ' \
        '\nFor frequencies or counts of meeting attendance: (url)/meeting/[frequency], [count]' \
        '\nFor drug sale arrests amount: (url)/drug-sale-arrests/lowerBoundCount/upperBoundCount' \

@app.errorhandler(404)
def page_not_found(e):
    """Makes a page for the user when an incorrect url is given"""
    return str(e)+" Sorry, wrong format, do this instead " \
    "(url)/meeting/[frequency, count] or " \
    "(url)/drug-sale-arrests/lowerBoundCount/upperBoundCount"

# @app.errorhandler(500)
# def python_bug(e):
#     """Makes a page when there is a bug in the underlying python code"""
#     return "Eek, a bug: "+str(e)

@app.route('/meeting', strict_slashes=False)
def get_meeting():
    """Makes a page that runs when a user request is given for meeting data"""
    data_source = DataSource()
    return render_template('self_help_meeting_page.html', count=data_source.get_ave_meetings_attended(), freq = data_source.get_freq_meetings_attended())

@app.route('/meeting/frequency', strict_slashes=False)
def get_meeting_freq():
    """Makes a page that runs when a user request is given for meeting data"""
    data_source = DataSource()
    freq = data_source.get_freq_meetings_attended()
    return "The average percentage of meetings attended is "+str(freq)+"%"

@app.route('/meeting/count', strict_slashes=False)
def get_meeting_count():
    """Makes a page that runs when a user request is given for meeting data"""
    data_source = DataSource()
    count = data_source.get_ave_meetings_attended()
    return "The average number of meetings attended is "+str(count)

@app.route('/drug-sale-arrests/<lower>/<upper>', strict_slashes=False)
def drug_sale(lower, upper):
    """Determines the route to the drug sale arrests page"""
    data_source = DataSource()
    return str(data_source.get_arrest_ranges(int(lower), int(upper))) + " people"

if __name__ == '__main__':
    app.run()
