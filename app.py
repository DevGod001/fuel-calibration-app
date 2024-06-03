from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

calibrations = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        depth_inches = float(request.form['depth_inches'])
        line_up = request.form['line_up']
        fuel_percentage = int((depth_inches * 100) / 19)
        needed_gallons = (19 - depth_inches) * 248
        needed_gallons = round(needed_gallons, 2)

        calibration = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'line_up': line_up,
            'fuel_percentage': fuel_percentage,
            'needed_gallons': needed_gallons,
            'depth_inches': depth_inches
        }
        calibrations.append(calibration)

        return redirect(url_for('index'))

    return render_template('index.html', calibrations=calibrations)

if __name__ == '__main__':
    app.run(debug=True)