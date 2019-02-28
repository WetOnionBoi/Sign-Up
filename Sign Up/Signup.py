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
@view("index")
def index():
    #need this function to attach the decorators above.
    pass

#CheckIn
@route("/check-in")
@view("check-in")
def check_in():
    data = dict (ticket_list = tickets)
    return data

@route('/check-in-success/<ticket_id>')
@view('check-in-success')
def check_in_success(ticket_id):
    #need this function to attach the decorators above.
    ticket_id = int(ticket_id)
    found_ticket = None
    for ticket in tickets:
        if ticket.id == ticket_id:
            found_ticket = ticket
    data = dict (ticket = found_ticket)
    found_ticket.check_in = True
    return data

@route('/sign-up')
@view('sign-up')
def sign_up():
    pass
        
@route('/sign-up-success', method = 'POST')
@view('sign-up-success')
def sign_up_success():
    name = request.forms.get('name')
    date_of_birth = request.forms.get('date_of_birth')
    email = request.forms.get('email')
    
    new_ticket = Ticket(name, email, date_of_birth, False)
    tickets.append(new_ticket)
    

#bottom of code
run(host='0.0.0.0', port = 8080, reloader=True, debug=True)