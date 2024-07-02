from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

date_format1 = "%d/%m/%Y"
date_format2 = '%Y-%m-%d'
rupeeSymbol = '\u20B9'


app = Flask(__name__)

def date_diff_calculator(start_date, end_date):
    # Calculate difference in days
    delta = end_date - start_date
    delta_days = delta.days
    
    # Calculate difference in months and remaining days
    end_year = end_date.year
    end_month = end_date.month
    end_day = end_date.day
    
    start_year = start_date.year
    start_month = start_date.month
    start_day = start_date.day
    
    # Calculate total months difference and remaining days
    total_months = (end_year - start_year) * 12 + (end_month - start_month)
    remaining_days = end_day - start_day

    # Adjust remaining days if negative (move to previous month)
    if remaining_days < 0:
        total_months -= 1
        last_month = datetime(end_year, end_month, 1)
        remaining_days += (end_date - last_month).days + 1

    # Calculate years and remaining months
    years = total_months // 12
    remaining_months = total_months % 12

    return [delta_days, years, remaining_months, remaining_days]

    return {
        'days': delta_days,
        'months_days': f"{years} year(s), {remaining_months} month(s), {remaining_days} day(s)",
        'years_months_days': f"{years} year(s), {remaining_months} month(s), {remaining_days} day(s)"
    }

def date_diff_in_days(start_date, end_date):
    return end_date - start_date


@app.route('/calculate', methods=['GET', 'POST'])
def calculateInterest():
    if request.method == 'POST':
        principalAmount = round(float(request.form['principal']),2)
        startDate = request.form['start_date']
        endDate = request.form['end_date']
        monthlyROI = int(request.form['rate'])
        includetoday = request.form.get('includeToday')

        start_Date =  datetime.strptime(startDate, date_format2).date()
        end_Date =  datetime.strptime(endDate, date_format2).date()

        delta_days, years, remaining_months, remaining_days = date_diff_calculator(start_Date, end_Date)

        datediffValue = date_diff_in_days(start_Date, end_Date)
        datediff = abs(datediffValue).days
        if includetoday:
            datediff += 1

        calculatedInterest = round((principalAmount * 12 * monthlyROI * datediff) / (36500),2)
        totalAmount = round((principalAmount + calculatedInterest), 2)

        datediffVal= str(delta_days) + ' days'
        if years > 0:
            datediffVal = str(years) + ' years ' + str(remaining_months) + ' months ' + str(remaining_days) + ' days'
        elif remaining_months > 0:
            datediffVal = str(remaining_months) + ' months ' + str(remaining_days) + ' days'


        calculation_details = {
            'principal': rupeeSymbol + str(principalAmount),
            'start_date': start_Date,
            'end_date': end_Date,
            'days_diff' : datediffVal,
            'simple_interest' : calculatedInterest,
            'amount': totalAmount,
            'today_included' : includetoday
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
    app.run(debug=False, host='0.0.0.0', port=5000)
