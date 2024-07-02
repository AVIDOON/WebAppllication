from flask import Flask, render_template, request, jsonify
from datetime import datetime
from datetime import date
date_format = "%d/%m/%Y"

monthlyROI = 5
annualROI = 12 * monthlyROI
includetoday = False

app = Flask(__name__)


def date_diff_in_days(start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    return abs((end_date - start_date).days)

def calculateInterest(principalAmount, startDate, endDate):
    # startDate = datetime.strptime(input('Enter Starting Date : '), date_format)
    # isEndDateToday = input('Is End Date today? True/False: ')

    # if isEndDateToday == True:
    #     endDate = datetime.today()
    # else:
    #     endDate = datetime.strptime(input('Enter End Date : '), date_format)
    datediff = date_diff_in_days(startDate, endDate)
    if includetoday:
        datediff += 1

    calculatedInterest = (principalAmount * annualROI * datediff) / (36500)
    totalAmount = principalAmount + calculatedInterest

    # print('Principal Amount : ', principalAmount)
    # print('Start Date : ', startDate)
    # print('End Date : ', endDate)
    # print(datediff, "days")
    # print('Interest : ', int(calculatedInterest))
    # print('Total Amount : ', int(totalAmount))
    return calculatedInterest

# Define a route to render the form
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        principalAmount = float(request.form['principal'])
        startDate = request.form['start_date']
        endDate = request.form['end_date']
        simpleInterest = calculateInterest(principalAmount, startDate, endDate)

        return jsonify({'amount': simpleInterest})

    # Render the form template if it's a GET request
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
