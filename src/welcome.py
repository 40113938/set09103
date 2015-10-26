from flask import Flask, request
app = Flask(__name__)

@app.route("/welcome/", methods=['POST', 'GET'])
def welcome():
  if request.method == 'POST':
    print request.form
    search = request.form['search']
    return "You searched for %s" % search
  else:
    page='''
    <html><body>
      <form action = "" method="post" search="form">
        <h1> Music Database </h1>
        <label for="search">Search:</label>
        <input type="text" name="search" id="search"/>
        <input type="submit" name="submit" id="submit"/>
      </form>
      <h3> Richard Cook - 40113938 </h3>
      </body><html>'''

    return page

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
