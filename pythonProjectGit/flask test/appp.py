from flask import Flask, request, render_template
appp = Flask(__name__)

@appp.route('/' , methods=['GET' , 'POST'])
def number_checker():
    result = None
    if request.method == 'POST':
        number = request.form.get('number')
        number = int(number)
        #checks for an even by moduling by 2 to get to 0
        if number % 2 == 0:
            result = 'even'
        else:
            result = 'odd'
    #returns number and updates the value
    return render_template('index.html', result=result)




if __name__ == '__main__':
    appp.run(debug=True)