from flask import Flask

# Add a flask instance called 'app'
app = Flask(__name__)

#create a root - or starting point
@app.route('/')
def hello_world():
    return 'Hello World'

def practice():
    numbers = [1, 2, 3, 4]
    return 
    for i in numbers:
        if i % 8 == 0:
            print("That works!")
        else:
            print("Womp!")
    

    