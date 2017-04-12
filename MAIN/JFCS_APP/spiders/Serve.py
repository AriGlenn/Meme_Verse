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


#return ids in json file where each id is linked to a name
