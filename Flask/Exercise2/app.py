from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        result = check_number(user_input)
        return render_template('result.html', result=result)
    return render_template('index.html')

def check_number(user_input):
    try:
        number = int(user_input)
        if number % 2 == 0:
            return f"{number} is even."
        else:
            return f"{number} is odd."
    except ValueError:
        return "Is not an integer!"

if __name__ == '__main__':
    app.run(debug=True)
