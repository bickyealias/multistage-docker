import psycopg2
import psycopg2.extras
import os 

from flask import Flask, render_template, request
app = Flask(__name__)


def connectToDB():
  #connectionString = 'dbname=music user=docker password=docker host=' + os.environ['POSTGRES_PORT_5432_TCP_ADDR']
  connectionString = 'dbname=music user=docker password=docker host=postgres'
  print connectionString
  try:
    return psycopg2.connect(connectionString)
  except Exception as e:
    print("Can't connect to database")
    print(str(e))

@app.route('/music')
def showChart():
  """rows returned from postgres are just an ordered list"""
  
  conn = connectToDB()
  cur = conn.cursor()
  try:
    cur.execute("select artist, name from albums")
  except:
    print("Error executing select")
  
  results = cur.fetchall()
  return str(results)
  #return "welcome to my flask"


if __name__=="__main__":
   app.debug=True
   app.run(host='0.0.0.0')
