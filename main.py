from flask import Flask, render_template
import math
import pymysql

conn = None
cur = None
list = []
cnt = 0

conn = pymysql.connect(host='192.168.0.50', port=3307, user='root', password='chrhtn12345', db='erp', charset='utf8')
cur = conn.cursor()

tilt01x = []
tilt01y = []
tilt02x = []
tilt02y = []
tilt03x = []
tilt03y = []
tilt04x = []
tilt04y = []
tilt05x = []
tilt05y = []
tilt06x = []
tilt06y = []
tilt07x = []
tilt07y = []

li = []
sql = "SELECT `opdatetime` from tiltmeter WHERE `opdatetime` LIKE '% 0:00%'"
cur.execute(sql)
row = cur.fetchall()
for i in row:
    print(str(i[0]).split()[0])
    li.append(str(i[0]).split()[0])


lis = ["tilt-01-x", "tilt-01-y", "tilt-02-x", "tilt-02-y", "tilt-03-x", "tilt-03-y", "tilt-04-x", "tilt-04-y", "tilt-05-x", "tilt-05-y", "tilt-06-x", "tilt-06-y", "tilt-07-x", "tilt-07-y"]
cnt = 0
for i in lis:
    sql = "SELECT `" + lis[cnt] + "` FROM tiltmeter WHERE `opdatetime` LIKE '% 0:00%'"
    cur.execute(sql)
    row = cur.fetchall()
    
    if(cnt == 0):
        for j in row:
            tilt01x.append(j)
    elif(cnt == 1):
        for j in row:
            tilt01y.append(j)
    elif(cnt == 2):
        for j in row:
            tilt02x.append(j)
    elif(cnt == 3):
        for j in row:
            tilt02y.append(j)
    elif(cnt == 4):
        for j in row:
            tilt03x.append(j)
    elif(cnt == 5):
        for j in row:
            tilt03y.append(j)
    elif(cnt == 6):
        for j in row:
            tilt04x.append(j)
    elif(cnt == 7):
        for j in row:
            tilt04y.append(j)
    elif(cnt == 8):
        for j in row:
            tilt05x.append(j)
    elif(cnt == 9):
        for j in row:
            tilt05y.append(j)
    elif(cnt == 10):
        for j in row:
            tilt06x.append(j)
    elif(cnt == 11):
        for j in row:
            tilt06y.append(j)
    elif(cnt == 12):
        for j in row:
            tilt07x.append(j)
    elif(cnt == 13):
        for j in row:
            tilt07y.append(j)
    cnt += 1


def rand(x, y):
    count = 0
    li = []
    for i in x:
        if(y[count][0]):
            li.append(math.atan2(float(x[count][0]), float(y[count][0])) * 180 / math.pi)
        count += 1
    return li



app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', lab = li ,tilt01 = rand(tilt01x, tilt01y), tilt02 = rand(tilt02x, tilt02y), tilt03 = rand(tilt03x, tilt03y), tilt04 = rand(tilt04x, tilt04y), tilt05 = rand(tilt05x, tilt05y), tilt06 = rand(tilt06x, tilt06y), tilt07 = rand(tilt07x, tilt07y))

if __name__ == "__main__":
    app.run(host="192.168.0.50", port="5000", debug=True)