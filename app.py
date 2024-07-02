from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from datetime import date
date_format1 = "%d/%m/%Y"
date_format2 = '%Y-%m-%d'

monthlyROI = 5
annualROI = 12 * monthlyROI
todayIncluded = 'No'

app = Flask(__name__)


def date_diff_in_days(start_date, end_date):
    return abs((end_date - start_date).days)


@app.route('/calculate', methods=['GET', 'POST'])
def calculateInterest():
    if request.method == 'POST':
        principalAmount = float(request.form['principal'])
        startDate = request.form['start_date']
        endDate = request.form['end_date']
        includetoday = request.form.get('includeToday')

        start_Date =  datetime.strptime(startDate, date_format2).date()
        end_Date =  datetime.strptime(endDate, date_format2).date()

        datediff = date_diff_in_days(start_Date, end_Date)
        if includetoday:
            datediff += 1
            todayIncluded = 'Yes'

        calculatedInterest = round((principalAmount * annualROI * datediff) / (36500),2)
        totalAmount = round((principalAmount + calculatedInterest), 2)

        calculation_details = {
            'principal': principalAmount,
            'start_date': start_Date,
            'end_date': end_Date,
            'simple_interest' : calculatedInterest,
            'amount': totalAmount,
            'today_included' : todayIncluded
        }

        return render_template('details.html', details=calculation_details)
    else:
        return redirect(url_for('index'))


# Define a route to render the form
@app.route('/', methods=['GET', 'POST'])
def index():
    # Render the form template if it's a GET request
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
