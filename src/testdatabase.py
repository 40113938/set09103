from flask import Flask, request, app, g
import sqlite3
app = Flask(__name__)

@app.before_request
def before_request():
  g.db = sqlite3.connect("music.db")

@app.teardown_request
def teardown_request(exception):
  if hasattr(g, 'db'):
    g.db.close()

@app.route('/artist')
def artist():
  artist = g.db.execute("SELECT name FRIM artist").fetchall()
  return render_template('artist.html', artist = artist)

db.execute('SELECT * FROM artist').fetchall()

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

