from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'Adam'
# Initialize a global dictionary to store user registrations
registered_users = {}

# Define a list of valid organizations
valid_organizations = ["Charlotte Hacks", "Code9", "Alpha Phi Alpha", "OAS", "NAACP"]

@app.route('/')
def home():
    return render_template('index.html', organizations=valid_organizations)

@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    organization = request.form.get('organization')

    if not name or not organization:
        flash('Both name and organization are required', 'error')
        return redirect(url_for('home'))

    if organization not in valid_organizations:
        flash('Invalid organization', 'error')
        return redirect(url_for('home'))

    registered_users[name] = organization
    flash('Registration successful', 'success')
    return redirect(url_for('registered_users_page'))

@app.route('/registered_users')
def registered_users_page():
    return render_template('registered_users.html', users=registered_users)

if __name__ == '__main__':
    app.run(debug=True)