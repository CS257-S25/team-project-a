"""This is a Flask App that allows for web based user database interaction"""

from flask import Flask, render_template, request
from ProductionCode.datasource import DataSource

app = Flask(__name__)

@app.route('/')
def homepage():
    """Creates a homepage that has user instructions returns a string"""
    return render_template('home_page.html')
    # return 'Hello! Welcome to our website with the amazingly' \
    #     'curated title: Analyzing Criminal Drug Abuse Treatment in Females' \
    #     '\nAlso known as drug_abuse_treatment.py' \
    #     '\n' \
    #     '\n' \
    #     'Here are the main directories of our program for your research/interests: ' \
    #     '\nFor frequencies or counts of meeting attendance: (url)/meeting/[frequency], [count]' \
    #     '\nFor drug sale arrests amount: \
    #      (url)/drug-sale-arrests/lowerBoundCount/upperBoundCount' \

@app.errorhandler(404)
def page_not_found(e):
    """Makes a page for the user when an incorrect url is given 
    takes in an error e and displays it, returns a string"""
    return str(e)+" Sorry, wrong format, do this instead /meeting/frequency or " \
        "/meeting/count or arrests/low/high"

@app.errorhandler(500)
def python_bug(e):
    """Makes a page when there is a bug in the underlying python code 
    takes in an error e and displays it, returns a string"""
    return "Eek, a bug: "+str(e)

@app.route('/meeting', strict_slashes=False)
def get_meeting():
    """Makes a page that runs when a user request is given for meeting data
    returns an HTML page"""
    data_source = DataSource()
    return render_template('self_help_meeting_page.html',
                           count=data_source.get_ave_meetings_attended(),
                           freq = data_source.get_freq_meetings_attended())

@app.route('/sellArrest', strict_slashes=False)
def sell_arrest():
    """Determines the route to the drug arrests page
    which will take in user input"""
    data_source = DataSource()
    return render_template('sellArrest.html')

@app.route('/dataOverview', strict_slashes=False)
def get_data_overview():
    """Makes a page that runs when a user request is given for the graphical data
    returns an HTML page"""
    data_source = DataSource()
    return render_template('data_overview_page.html')

@app.route('/meeting/frequency', strict_slashes=False)
def get_meeting_freq():
    """Makes a page that runs when a user request is given for meeting data
    returns a string"""
    data_source = DataSource()
    freq = data_source.get_freq_meetings_attended()
    return "The average percentage of self-help meetings attended is "+str(freq)+"%"

@app.route('/meeting/count', strict_slashes=False)
def get_meeting_count():
    """Makes a page that runs when a user request is given for meeting data
    returns a string"""
    data_source = DataSource()
    count = data_source.get_ave_meetings_attended()
    return "The average number of self-help meetings attended is "+str(count)

@app.route('/sellArrest/<lower>/<upper>', strict_slashes=False)
def sell_arrest_spec(lower, upper):
    """Calls the get_arrest_ranges function from the core.py file
    to display some dummy information"""
    data_source = DataSource()
    lower = int(request.args.get('lower'))
    upper = int(request.args.get('upper'))
    result = data_source.get_arrest_ranges(lower, upper)

    return render_template('sellArrestSpec.html', lower=lower, upper=upper, result=result)

if __name__ == '__main__':
    app.run()
