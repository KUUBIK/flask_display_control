
from flask import Flask, render_template, session, request, json, jsonify, url_for, Markup
from flask_pymongo import PyMongo
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/youdatabase"
mongo = PyMongo(app)
user = mongo.db.users

# user.insert([{
#   "_id": 3,
#   "title": "Новые клиенты за сегодня",
#   "img": "static/img/bg.jpg",
#   "img-src": "static/img/bg.jpg",
#   "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit, at!",
#   "video": "static/video/vid.mp4",
#     "token": 3
#     }])

#          # {"_id": 2 ,'car2' : '/home/robert/androidflask/flaskled/tumblelog/photos/car2.png'},
#          # {"_id": 3 ,'car3': '/home/robert/androidflask/flaskled/tumblelog/photos/car3.png'}])
#     for men in user.find({"_id": 1}):
#         print (men)
#     with open('test/json/dat.json', 'w') as dat:
#        jsn = json.dump(men, dat, indent=2, ensure_ascii=False )
#     print(jsn)
#     return jsonify(men)
#
@app.route('/pc')
def add_pc():
    user2 = mongo.db.users
    for mep in user2.find({"_id": 2}): #ищет по Id
        print (mep)
    with open('static/data.json', 'w') as dat: # открывает json файл "W"- это команда на запись (write, read)
       jsn = json.dump(mep, dat, indent=2, ensure_ascii=False ) # mep это значение которому присвоено наше json значение из монги
    print(jsn)
    return render_template ('zip.html')


@app.route('/pd')
def add_pd():
    user2 = mongo.db.users
    for mem in user2.find({"_id": 3}):
        print (mem)
    with open('static/data.json', 'w') as dat:
       jsn = json.dump(mem, dat, indent=2, ensure_ascii=False )
    print(jsn)
    return render_template ('zip.html')


@app.route('/pp')
def add_pp():
    user2 = mongo.db.users
    for men in user2.find({"_id": 1}):
        print (men)
    with open('static/data.json', 'w') as dat:
       jsn = json.dump(men, dat, indent=2, ensure_ascii=False )
    print(jsn)
    return render_template ('zip.html')


@app.route('/')
def add_db():
    user = mongo.db.users
    path = "192.168.8.100"
    return render_template ('main.html', **locals())


@app.route('/pr')
def add_pr():
    return render_template ('zip.html')




if __name__ == '__main__':
    app.run(host='192.168.8.100', port=8888,debug=True)
    # server = pywsgi.WSGIServer(('192.168.8.100', 8888), app, handler_class=WebSocketHandler)
    # server.serve_forever()

