from flask import Flask, render_template

# Create an instance of the Flask class, which will be our web application
app = Flask(__name__)

# Define a route for the root URL ("/") and the associated view function
@app.route('/fizzbuzz')
def fizzbuzz():
    unordered_list=[]
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            unordered_list.append('FizzBuzz')
        elif number % 3 == 0:
            unordered_list.append('Fizz')
        elif number % 5 == 0:
            unordered_list.append('Buzz')
        else:
            unordered_list.append(number)
    return render_template('fizzbuzz.html', unordered_list=unordered_list)

if __name__ == '__main__':
    app.run(debug=True)