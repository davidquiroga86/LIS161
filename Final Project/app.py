from flask import Flask, request, redirect, url_for, session, render_template
import sqlite3
app = Flask(__name__)

# Configuration for app starts here
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "thisisasecretkey!"
# Configuration ends here

#database helper functions

def connect_db(filename):
    # Connects/opens database with given filename
    conn = sqlite3.connect(filename)
    return conn

def read(tablename):
    # Read all contents of table with given tablename
    conn = connect_db('dayone.db')
    cur = conn.cursor()
    query = '''SELECT * FROM "{}" '''.format(tablename)
    cur.execute(query)
    results = cur.fetchall()
    cur.close()
    # end of database transaction

    return results

def teamread(tablename, teamname):
    #Read only statistics from given table
    conn = connect_db('dayone.db')
    cur = conn.cursor()
    query = '''SELECT * FROM "{}" WHERE team = "{}"'''.format(tablename, teamname)
    cur.execute(query)
    results = cur.fetchall()
    cur.close()
    # end of database transaction

    return results

def tablechecker(team):
    if team == "1994" or team == "2015":
        tablename = "1994vs2015"
    elif team == "2000/18" or team == "2003":
        tablename = "2000/18vs2003"
    elif team == "2002" or team == "2006":
        tablename = "2002vs2006"
    elif team == "2004" or team == "2014":
        tablename = "2004vs2014"
    elif team == "2008" or team == "1990/93/95":
        tablename = "2008vs1990/93/95"
    elif team == "2009" or team == "2010":
        tablename = "2009vs2010"
    elif team == "2012" or team == "1999":
        tablename = "2012vs1999"
    elif team == "2013/19" or team == "1992":
        tablename = "2013/19vs1992"
    return tablename

def sum_stats(results):
    #Given data from a table this function sums up each statistic

    #Create the list that will hold the sums
    total_stats = list()
    i = 3
    while i < 20:
        total_stats.append(0)
        i += 1

    #Loop through statistics and create running total for each statistic in the list
    for result in results:
        i = 3
        j = 0
        while i < 20:
            total_stats[j] += result[i]
            i += 1
            j += 1

    return total_stats

#end of database helper functions

# Routes begin here

#This route is the index page I used to create a landing page
@app.route('/')
def index():
    session["username"] = ""
    return render_template('index.html')

#This route is the home page
@app.route('/home', methods=["GET", "POST"])
def home():
    username = session["username"]
    if request.method == "GET":
        return render_template('home.html', username=username)
    else:
        name = request.form['username']
        password = request.form['password']
        if name == "admin" and password == "admin":
            session["username"] = name
            username = session["username"]
            return render_template('home.html', username=username)
        else:
            return render_template('login.html', username=username, status="invalid")

#This route is the login page
@app.route('/login')
def login():
    username = session["username"]
    return render_template('login.html', username=username)

#This route is the logout page
@app.route('/logout')
def logout():
    session["username"] = ""
    username = session["username"]
    return render_template('logout.html', username=username)

#This route is the team statistics page
@app.route('/team', defaults={"name":"Default"})
@app.route('/team/<name>')
def team(name):
    username = session["username"]
    if name == "Default":
        return render_template('team_default.html', username=username)
    else:
       if name == "19909395":
           results = teamread('2008vs1990/93/95', '1990/93/95')
           stats = sum_stats(results)
           return render_template('team.html', results=results, stats=stats, username=username)
       elif name == "2008":
           results = teamread('2008vs1990/93/95', '2008')
           stats = sum_stats(results)
           return render_template('team.html', results=results, stats=stats, username=username)
       elif name == "200018":
           results = teamread('2000/18vs2003', '2000/18')
           stats = sum_stats(results)
           return render_template('team.html', results=results, stats=stats, username=username)
       elif name == "2003":
           results = teamread('2000/18vs2003', '2003')
           stats = sum_stats(results)
           return render_template('team.html', results=results, stats=stats, username=username)
       elif name == "201319":
           results = teamread('2013/19vs1992', '2013/19')
           stats = sum_stats(results)
           return render_template('team.html', results=results, stats=stats, username=username)
       elif name == "1992":
           results = teamread('2013/19vs1992', '1992')
           stats = sum_stats(results)
           return render_template('team.html', results=results, stats=stats, username=username)
       elif name == "1994":
           results = teamread('1994vs2015', '1994')
           stats = sum_stats(results)
           return render_template('team.html', results=results, stats=stats, username=username)
       elif name == "2015":
           results = teamread('1994vs2015', '2015')
           stats = sum_stats(results)
           return render_template('team.html', results=results, stats=stats, username=username)
       elif name == "2002":
           results = teamread('2002vs2006', '2002')
           stats = sum_stats(results)
           return render_template('team.html', results=results, stats=stats, username=username)
       elif name == "2006":
           results = teamread('2002vs2006', '2006')
           stats = sum_stats(results)
           return render_template('team.html', results=results, stats=stats, username=username)
       elif name == "2004":
           results = teamread('2004vs2014', '2004')
           stats = sum_stats(results)
           return render_template('team.html', results=results, stats=stats, username=username)
       elif name == "2014":
           results = teamread('2004vs2014', '2014')
           stats = sum_stats(results)
           return render_template('team.html', results=results, stats=stats, username=username)
       elif name == "2009":
           results = teamread('2009vs2010', '2009')
           stats = sum_stats(results)
           return render_template('team.html', results=results, stats=stats, username=username)
       elif name == "2010":
           results = teamread('2009vs2010', '2010')
           stats = sum_stats(results)
           return render_template('team.html', results=results, stats=stats, username=username)
       elif name == "2012":
           results = teamread('2012vs1999', '2012')
           stats = sum_stats(results)
           return render_template('team.html', results=results, stats=stats, username=username)
       elif name == "1999":
           results = teamread('2012vs1999', '1999')
           stats = sum_stats(results)
           return render_template('team.html', results=results, stats=stats, username=username)
       else:
           return render_template('team_error.html', name=name, username=username)

#This route is the add page
@app.route('/add', methods=["GET", "POST"])
def add():
    username = session["username"]
    if request.method == "GET":
        edit_team = request.args.get('team')

        return render_template('add.html', username=username, team=edit_team)
    else:
        edit_team = request.form['team']
        new_name = request.form['name']
        new_fgm = request.form['fgm']
        new_fga = request.form['fga']
        new_2pm = request.form['2pm']
        new_2pa = request.form['2pa']
        new_3pm = request.form['3pm']
        new_3pa = request.form['3pa']
        new_ftm = request.form['ftm']
        new_fta = request.form['fta']
        new_orb = request.form['orb']
        new_drb = request.form['drb']
        new_trb = request.form['trb']
        new_ast = request.form['ast']
        new_stl = request.form['stl']
        new_blk = request.form['blk']
        new_to = request.form['to']
        new_pf = request.form['pf']
        new_pts = request.form['pts']
        table_name = tablechecker(edit_team)

        #Add record
        conn = connect_db('dayone.db')
        cur = conn.cursor()
        query = '''INSERT INTO "{}" (name, team, fgm, fga, "2pm", "2pa", "3pm", "3pa", ftm, fta, orb, drb, trb, ast, stl, blk, "to", pf, pts) VALUES ("{}", "{}", {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}) '''.format(table_name, new_name, edit_team, new_fgm, new_fga, new_2pm, new_2pa, new_3pm, new_3pa, new_ftm, new_fta, new_orb, new_drb, new_trb, new_ast, new_stl, new_blk, new_to, new_pf, new_pts)
        cur.execute(query)
        conn.commit()
        cur.close()

        if edit_team == "1990/93/95":
            edit_team = "19909395"
        elif edit_team == "2000/18":
            edit_team = "200018"
        elif edit_team == "2013/19":
            edit_team = "201319"

        return redirect(url_for('team', name=edit_team))



#This route is the edit page
@app.route('/edit', methods=["GET", "POST"])
def edit():
    username = session["username"]
    if request.method == "GET":
        edit_id = request.args.get('id')
        edit_team = request.args.get('team')
        table_name = tablechecker(edit_team)

        #Retrieve the record
        conn = connect_db('dayone.db')
        cur = conn.cursor()
        query ='''SELECT * FROM "{}" WHERE id = {} '''.format(table_name, edit_id)
        cur.execute(query)
        result = cur.fetchone()
        cur.close()
        #Record retrieved

        return render_template('edit.html', username=username, result=result)
    else:
        edit_id = request.form['id']
        edit_team = request.form['team']
        new_name = request.form['name']
        new_fgm = request.form['fgm']
        new_fga = request.form['fga']
        new_2pm = request.form['2pm']
        new_2pa = request.form['2pa']
        new_3pm = request.form['3pm']
        new_3pa = request.form['3pa']
        new_ftm = request.form['ftm']
        new_fta = request.form['fta']
        new_orb = request.form['orb']
        new_drb = request.form['drb']
        new_trb = request.form['trb']
        new_ast = request.form['ast']
        new_stl = request.form['stl']
        new_blk = request.form['blk']
        new_to = request.form['to']
        new_pf = request.form['pf']
        new_pts = request.form['pts']
        table_name = tablechecker(edit_team)
        if request.form['edit'] == 'update':
            #Update the record
            conn = connect_db('dayone.db')
            cur = conn.cursor()
            query = '''UPDATE "{}" SET name = "{}" WHERE id = {};'''.format(table_name, new_name, edit_id)
            cur.execute(query)
            query = ''' UPDATE "{}" SET fgm = {} WHERE id = {} '''.format(table_name, new_fgm, edit_id)
            cur.execute(query)
            query = ''' UPDATE "{}" SET fga = {} WHERE id = {} '''.format(table_name, new_fga, edit_id)
            cur.execute(query)
            query = ''' UPDATE "{}" SET "2pm" = {} WHERE id = {} '''.format(table_name, new_2pm, edit_id)
            cur.execute(query)
            query = ''' UPDATE "{}" SET "2pa" = {} WHERE id = {} '''.format(table_name, new_2pa, edit_id)
            cur.execute(query)
            query = ''' UPDATE "{}" SET "3pm" = {} WHERE id = {} '''.format(table_name, new_3pm, edit_id)
            cur.execute(query)
            query = ''' UPDATE "{}" SET "3pa" = {} WHERE id = {} '''.format(table_name, new_3pa, edit_id)
            cur.execute(query)
            query = ''' UPDATE "{}" SET ftm = {} WHERE id = {} '''.format(table_name, new_ftm, edit_id)
            cur.execute(query)
            query = ''' UPDATE "{}" SET fta = {} WHERE id = {} '''.format(table_name, new_fta, edit_id)
            cur.execute(query)
            query = ''' UPDATE "{}" SET orb = {} WHERE id = {} '''.format(table_name, new_orb, edit_id)
            cur.execute(query)
            query = ''' UPDATE "{}" SET drb = {} WHERE id = {} '''.format(table_name, new_drb, edit_id)
            cur.execute(query)
            query = ''' UPDATE "{}" SET trb = {} WHERE id = {} '''.format(table_name, new_trb, edit_id)
            cur.execute(query)
            query = ''' UPDATE "{}" SET ast = {} WHERE id = {} '''.format(table_name, new_ast, edit_id)
            cur.execute(query)
            query = ''' UPDATE "{}" SET stl = {} WHERE id = {} '''.format(table_name, new_stl, edit_id)
            cur.execute(query)
            query = ''' UPDATE "{}" SET blk = {} WHERE id = {} '''.format(table_name, new_blk, edit_id)
            cur.execute(query)
            query = ''' UPDATE "{}" SET "to" = {} WHERE id = {} '''.format(table_name, new_to, edit_id)
            cur.execute(query)
            query = ''' UPDATE "{}" SET pf = {} WHERE id = {} '''.format(table_name, new_pf, edit_id)
            cur.execute(query)
            query = ''' UPDATE "{}" SET pts = {} WHERE id = {} '''.format(table_name, new_pts, edit_id)
            cur.execute(query)
            conn.commit()
            cur.close()

        elif request.form['edit'] == 'delete':
            #Delete the record
            conn = connect_db('dayone.db')
            cur = conn.cursor()
            query = '''DELETE FROM "{}" WHERE id = {} '''.format(table_name, edit_id)
            cur.execute(query)
            conn.commit()
            cur.close()

        #some operations since variables need to be cleaned for usage in target route
        if edit_team == "1990/93/95":
            edit_team = "19909395"
        elif edit_team == "2000/18":
            edit_team = "200018"
        elif edit_team == "2013/19":
            edit_team = "201319"

        return redirect(url_for('team', name=edit_team))


if __name__ == "__main__":
    app.run()