from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        number = request.form.get('number')
        if number.isdigit():
            number = int(number)
            if number % 2 == 0:
                result = 'even'
            else:
                result = 'odd'
        else:
            result = 'Invalid input. Please enter a valid number.'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
