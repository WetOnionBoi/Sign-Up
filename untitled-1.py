        #Ver 1.1 Created test data for ticket variable
        #Ver 1.2 Adding server functionality to our code
        
from bottle import run, route, view, get, post, request
from itertools import count


class Ticket:
    
    #signifies a private variable. not to be used outside of this class.
    _ids = count (0)
    
    def __init__(self, name, email, date_of_birth, check_in):
        #not passing ID as we want it to create it.
        self.id = next(self._ids)
        self.name = name
        self.email =  email
        self.dob = date_of_birth
        self.check_in = check_in
        



    #Test Data
tickets = [
          Ticket("Captain America", "America@gmail.com", "02.11.2015", False),
          Ticket("John Wick", "Yespapa@gmail.com", "01.01.2001", False),
          Ticket("Bat Man", "Battery@gmail.com", "30.07.1990", False),
          Ticket("Spider Man", "Spidey@gmail.com", "14.02.1920", False)
          ]

#Pages

#index page
@route("/")
@view("Index")
def index():
    #need this function to attach the decorators above.
    pass


#bottom of code
run(host='0.0.0.0', port = 8080, reloader=True, debug=True)