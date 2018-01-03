#15-4
import sqlite3 as dbapi
def run_query(db,*query):
    con = dbapi.connect(db)
    cur = con.cursor()
    if len(query) == 1:
        cur.execute(query[0])
    else:
        cur.execute(query[0],(query[1]))

    data= cur.fetchall()
    cur.close()
    con.close()
    return data


if __name__ == '__main__':

    con = dbapi.connect('xy.db')
    cur = con.cursor()
    cur.execute('DROP TABLE Density')
    cur.execute('CREATE TABLE Density(Region TEXT,Population INEGER) ')

    Regions_data = [("Nova",908007),("NEW Brunswick",729498),
                        ("Ontario",11410046),("Nunavnt",26745)]
    for value in Regions_data:
        cur.execute("INSERT INTO Density VALUES (?, ?)",(value[0],value[1]))

    con.commit()
    cur.close()
    con.close()

    print run_query ('xy.db','SELECT * FROM Density')
    print run_query ('xy.db','SELECT * FROM Density WHERE Density.Region =(?) AND Density.Population = (?) ',("Nova",908007))
