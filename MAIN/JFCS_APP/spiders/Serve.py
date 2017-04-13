from flask import Flask, jsonify
import sqlite3 as lite
import pickle
app = Flask(__name__)


@app.route("/")
def mainPg():
    return "Get List:  /getlist/MAX"


@app.route('/getlist/<int:Max>')
def getList(Max):
    listIDs = []
    dictIDs = {}

    con = lite.connect('test47.db')
    cursor = con.execute("SELECT rowid, Name, DatePosted, URL, MAINURL from MemesTest1 limit %s" % Max)
    for x in cursor:
        listIDs.append(x[0])
        dictMEMEs = {}
        dictMEMEs['Name'] = x[1]
        dictMEMEs['DatePosted'] = x[2]
        dictMEMEs['MainUrl'] = x[4]
        dictMEMEs['MemeUrls'] = pickle.loads(x[3])

        dictIDs[x[0]] = dictMEMEs

    con.close()
    return jsonify(dictIDs)

@app.route('/getall')
def getall():
    listIDs = []
    dictIDs = {}

    con = lite.connect('test47.db')
    cursor = con.execute("SELECT rowid, Name, DatePosted, URL, MAINURL from MemesTest1")
    for row in cursor:
        listIDs.append(row[0])
        dictMEMEs = {}
        dictMEMEs['Name'] = row[1]
        dictMEMEs['DatePosted'] = row[2]
        dictMEMEs['MainUrl'] = row[4]
        dictMEMEs['MemeUrls'] = pickle.loads(row[3])

        dictIDs[row[0]] = dictMEMEs

    con.close()
    return jsonify(dictIDs)

if __name__ == '__main__':
    app.run(host='my_ip_addr',port=5000)
