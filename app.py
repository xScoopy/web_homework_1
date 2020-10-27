from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/penguins')
def penguins():
    """shows that penguins are cute"""
    return 'Penguins are cute!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal"""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Display message showing favorite dessert"""
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs_page(adjective, noun):
    """display story using user input adj and noun"""
    return f'the quick brown fox jumped over the {adjective} {noun}.'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1,number2):
    """Multiplies 2 numbers"""
    if number1.isdigit() == False or number2.isdigit() == False:
        return f'invalid inputs. Please try again by entering 2 numbers!'
    else:
        return f'{number1} times {number2} is {(int(number1) * int(number2))}.'

if __name__ == '__main__':
    app.run(debug=True)