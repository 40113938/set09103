from flask import Flask, request, render_template, g
import sqlite3
app = Flask(__name__)

def get_db():
  return sqlite3.connect('music.db')

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

@app.route("/artist/", methods=['POST', 'GET'])
def artist():
  band = request.args.get('q', '')
  g.db = get_db()
  if band == '':
    cur = g.db.execute ('SELECT * from artist ORDER BY name')
  else:
    cur = g.db.execute ('SELECT * from artist where name = ?', (band, ))
  artist = [dict(name=row[0],
  yoc=row[1], nationality=row[2], genre=row[3]) for row in cur.fetchall()]
  return render_template('artit.html', band=band, artist=artist)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
