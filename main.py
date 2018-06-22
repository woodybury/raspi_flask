from flask import Flask, render_template, redirect
from flask_basicauth import BasicAuth
import datetime
app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'bill'
app.config['BASIC_AUTH_PASSWORD'] = 'chicken'

basic_auth = BasicAuth(app)

gate = 0
message = None

@app.route("/")
@basic_auth.required
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO BILL!',
      'time': timeString,
      'gate' : gate,
      'message' : message
      }
   return render_template('main.html', **templateData)

@app.route("/gate/<int:gate_action>")
@basic_auth.required
def action(gate_action):

   global gate, message

   if gate_action == 1:
      print (action, "Let the chickens loose!")
      message = "Chickens are loose!"
      gate = 1

   elif gate_action == 0:
      print (action, "close the hatch")
      message = "The coop is shut!"
      gate = 0

   else:
      print ("hacker alert!")
      message = "You can't do that!"

   return redirect('/')


if __name__ == "__main__":
   app.run(host='localhost', port=3000, debug=True)
