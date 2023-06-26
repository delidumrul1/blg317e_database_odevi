import sqlite3
from flask import *

app=Flask(__name__)
app.config['SECRET_KEY'] = 'Ahmet'

def get_db_con():
    con=sqlite3.connect('education.db')
    con.row_factory=sqlite3.Row
    return con


def get_data(id):
    con=get_db_con()
    data=con.execute('SELECT * FROM Education WHERE id=?', (id,) ).fetchone()
    con.close()
    if data is None:
        abort(404)
    return data    


@app.route('/')
def index():
    con=get_db_con()
    rows=con.execute('SELECT * FROM Education ORDER BY id DESC').fetchall()
    con.close()
    return render_template('index.html',rows=rows)

@app.route('/enter/', methods=('GET','POST'))
def enter():
    if request.method=='POST':
        cona=request.form['cona']
        coco=request.form['coco']
        clefu=request.form['clefu']
        elru=request.form['elru']
        elur=request.form['elur']
        scra=request.form['scra']
        date=request.form['date']
        if cona not in ['Brazil','China','India','Russian Federation','Russia','China']:
            flash('Your data should be about 5 countries.')    
        elif (cona=='Brazil' and coco!='BRA') or (cona=='China' and coco!='CHN') or (cona=='India' and coco!='IND') or ( (cona=='Russia' or cona=='Russian Federation') and coco!='RUS') or (cona=='South Africa' and coco!='ZAF'):
            flash('Please match your country name and country code.')
        else:
            con=get_db_con()
            con.execute("INSERT into Education (country_name, country_code, clean_fuel, elec_rural, elec_urban, school_enroll, date) values (?,?,?,?,?,?,?)"
            ,(cona,coco,clefu,elru,elur,scra,date))   
            con.commit()
            con.close()
            return redirect(url_for('index'))
    return render_template('enter.html')

@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    data=get_data(id)
    if request.method=='POST':
        cona=request.form['cona']
        coco=request.form['coco']
        clefu=request.form['clefu']
        elru=request.form['elru']
        elur=request.form['elur']
        scra=request.form['scra']
        date=request.form['date']
        if cona not in ['Brazil','China','India','Russian Federation','Russia','South Africa']:
            flash('Your data should be about 5 countries.')    
        elif (cona=='Brazil' and coco!='BRA') or (cona=='China' and coco!='CHN') or (cona=='India' and coco!='IND') or ( (cona=='Russia' or cona=='Russian Federation') and coco!='RUS') or (cona=='South Africa' and coco!='ZAF'):
            flash('Please match your country name and country code.')
        else:
            con=get_db_con()
            con.execute("UPDATE Education SET country_name = ?, country_code = ?, clean_fuel = ?, elec_rural = ?, elec_urban = ?, school_enroll = ?, date = ? WHERE id = ?" ,(cona,coco,clefu,elru,elur,scra,date,id ) )   
            con.commit()
            con.close()
            return redirect(url_for('index'))
    return render_template('edit.html',data=data)

@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    data=get_data(id)
    con=get_db_con()
    con.execute('DELETE FROM Education WHERE id = ?',(id,))
    con.commit()
    con.close()
    flash("Data is deleted, are you happy now?")
    return redirect(url_for('index'))








if __name__=="__main__":
    app.run(debug=True)


#get_flashed_messages(): Pulls all flashed messages from the session and returns them.


"""

.: ⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉

"""