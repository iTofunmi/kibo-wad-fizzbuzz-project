from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to the homepage. <a href='/fizzbuzz/'>Go to FizzBuzz</a>"

@app.route('/fizzbuzz/')
def fizzbuzz():
    unordered_list = []
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
