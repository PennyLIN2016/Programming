

#15-1/2

import sqlite3 as dbapi

if __name__ == '__main__':
    con = dbapi.connect('census.db')
    cur = con.cursor()
    try:

        cur.execute('DROP TABLE Density')
        cur.execute('CREATE TABLE Density(Region TEXT,Population INEGER, Area REAL) ')

        Regions_data = [("Nova",908007,52917.43),("NEW Brunswick",729498,71355.67),
                        ("Ontario",11410046,907655.59),("Nunavnt",26745,1925460.18)]
        #print 'The Rgions_data is  ',Regions_data
        for value in Regions_data:
            cur.execute("INSERT INTO Density VALUES (?, ?, ?)",(value[0],value[1],value[2]))

        con.commit()

        cur.execute('SELECT * FROM Density')
        #print 'The Density : ',cur.fetchall()

        sqlstr = 'DROP TABLE Capitals'
        cur.execute(sqlstr)
        sqlstr = 'CREATE TABLE Capitals(District TEXT, Captial TEXT, Population INEGER )'
        cur.execute(sqlstr)
        con.commit()

        cap_data= [('Nova','Halifax',359183),('NEW Brunswick','Fredericton',81346),
                   ('Ontario','Toronto',4682897),('Nunavnt','Iqalult',5236)]
        print 'The original data is  ',cap_data
        for value in cap_data:
            cur.execute('INSERT INTO Capitals VALUES(?, ?, ?)',(value[0],value[1],value[2]))
            con.commit()

        sqlstr = 'SELECT * FROM Capitals '
        cur.execute(sqlstr)
        print 'THE Capitals is ',cur.fetchall()

        cur.execute('''SELECT Density.Population , Capitals.Population 
                    FROM Density , Capitals 
                    WHERE (Density.Region = Capitals.District) ''')
        print 'THE region and captial population : ',cur.fetchall()

        cur.execute('''SELECT Density.Area 
                    FROM Density , Capitals 
                    WHERE (Density.Region = Capitals.District 
                    AND  Capitals.Population > 100000) ''')
        print 'THE area where the population is more than 1 million : ',cur.fetchall()

        cur.execute('''SELECT Density.Population 
                    FROM Density, Capitals
                    WHERE (Density.Region = Capitals.District 
                    AND  Capitals.Population > 100000
                    AND  (Density.Population /Density.Area)>15 ) ''')
        print 'THE population of d : ',cur.fetchall()

        cur.execute('SELECT SUM(Density.Area) FROM Density')
        print 'THE area of e : ',cur.fetchall()

        cur.execute('SELECT AVG(Capitals.Population) FROM Capitals')
        print 'THE result of f : ',cur.fetchall()

        cur.execute('SELECT MIN(Capitals.Population) FROM Capitals')
        print 'THE result of g : ',cur.fetchall()

        cur.execute('SELECT MAX(Density.Population) FROM Density')
        print 'THE area of h : ',cur.fetchall()

        cur.execute('''SELECT A.Region,B.Region 
                    FROM Density A INNER JOIN Density B
                    WHERE (ABS(A.Population/A.Area -B.Population/B.Area) < 5)
                    AND A.Region < B.Region ''')
        print 'THE area of i : ',cur.fetchall()

        #delete all data
        #cur.execute('DROP TABLE Density')

        #sqlstr = 'DROP TABLE Capitals'
        #cur.execute(sqlstr)
        #con.commit()

        cur.close()
        con.close()

    except:
        print 'ERROR!!!'
        con.rollback()
        cur.close()
        con.close()



