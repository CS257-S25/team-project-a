"""This is a Flask App that allows for web based user database interaction"""

from flask import Flask, render_template, request
from ProductionCode.datasource import DataSource

app = Flask(__name__)

@app.route('/')
def homepage():
    """Creates a homepage that has user instructions, returns a HTML page"""
    pages = ["home", "meetings", "data overview", "arrests"]
    return render_template('home_page.html', pages=pages)
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
        "/meeting/count or arrests/low/high eg. arrests/1/3"

@app.errorhandler(500)
def python_bug(e):
    """Makes a page when there is a bug in the underlying python code 
    takes in an error e and displays it, returns a string"""
    return "Eek, a bug: "+str(e)

@app.route("/search", methods=["POST", "GET"], strict_slashes=False)
def display_page_based_on_search():
    """Dynamicaly renders a page based on passed in search parameters,
    returns a HTML page"""
    pages = ["home", "meetings", "data overview", "arrests"]
    if request.method == 'POST':
        response = request.form['search'].replace(" ", "_")
        if response == "meetings":
            data_source = DataSource()
            return render_template(
                "self_help_meeting_page.html", count=data_source.get_ave_meetings_attended(),
                freq=data_source.get_freq_meetings_attended(), pages=pages
            )
        if response == "arrests":
            pages = ["home", "meetings", "data overview", "arrests"]
            data_source = DataSource()
            return render_template('sell_arrest.html', pages=pages)
        if response == "data_overview":
            pages = ["home", "meetings", "data overview", "arrests"]
            data_source = DataSource()
            return render_template('data_overview_page.html', pages=pages)
        if response == "home":
            return render_template("home_page.html", pages=pages)
        return render_template("home_page.html", pages=pages)
    return render_template("home_page.html", pages=pages)

@app.route('/meeting', strict_slashes=False)
def get_meeting():
    """Makes a page that runs when a user request is given for meeting data
    returns an HTML page"""
    pages = ["home", "meetings", "data overview", "arrests"]
    data_source = DataSource()
    return render_template('self_help_meeting_page.html',
                           count=data_source.get_ave_meetings_attended(),
                           freq = data_source.get_freq_meetings_attended(),
                           pages=pages
                           )

@app.route('/sellArrest', strict_slashes=False)
def sell_arrest():
    """Determines the route to the drug arrests page
    which will take in user input, returns a HTML page"""
    pages = ["home", "meetings", "data overview", "arrests"]
    return render_template('sell_arrest.html', pages=pages)

@app.route('/dataOverview', strict_slashes=False)
def get_data_overview():
    """Makes a page that runs when a user request is given for the graphical data
    returns an HTML page"""
    pages = ["home", "meetings", "data overview", "arrests"]
    data_source = DataSource()
    return render_template('data_overview_page.html',
                           pages=pages, data=data_source.get_graph_data())

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

@app.route('/sellArrest/<lower>/<upper>', strict_slashes=False, methods=["POST", "GET"])
def sell_arrest_result(lower, upper):
    """Redirects from the sell arrest page to a page
    that displays a result based on the lower and upper bounds"""
    pages = ["home", "meetings", "data overview", "arrests"]
    data_source = DataSource()
    lower = int(request.args.get('lower'))
    upper = int(request.args.get('upper'))
    result = data_source.get_arrest_ranges(lower, upper)

    return render_template('sell_arrest_result.html', lower=lower, upper=upper,
                            result=result, pages=pages)

if __name__ == '__main__':
    app.run()
