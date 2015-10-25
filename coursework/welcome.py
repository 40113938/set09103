from flask import Flask, request
app = Flask(__name__)

@app.route("/welcome/", methods=['POST', 'GET'])
def welcome():
  if request.method == 'POST':
    print request.form
    name = request.form['name']
    return "Hello %s" % name
    print request.form
    password=requrest.form['password']
  else:
    page='''
    <html><body>
      <form action = "" method="post" name="form">
        <h1> Music Database </h1>
        <label for="name">Name:</label>
        <input type="text" name="name" id="name"/>
        <label for="password">Password::</label>
        <input type="password" name="password" id="password"/>
        <input type="submit" name="submit" id="submit"/>        
      </form>
      <h3> Richard Cook - 40113938 </h3>
      </body><html>'''

    return page

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
