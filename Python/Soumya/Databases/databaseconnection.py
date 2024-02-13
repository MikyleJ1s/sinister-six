import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", passwd="Mikyle123", database="airticket")
print(myconn)
cur = myconn.cursor()
try:
    # step 1: create the table ...
    #dbs = cur.execute("create table staff(name varchar(20) not null, id int(20) not null primary key, salary float, department int)")
    # step 2: insert into the table ...
    #cur.execute("insert into staff values ('Bob', 1, 15000, 1), ('Tom', 2, 34000, 2),('Meg', 3, 32000, 1)")
    # step 3: read from the table ...
    print("After insertion: ")
    query = "select * from staff"
    '''
    
    '''
    cur.execute(query)
    myresult = cur.fetchall()
    for x in myresult:
        print(x)
    # step 4: delete from the table ...
    cur.execute("delete from staff where id = 2")
    print("After deletion: ")
    query = "select * from staff"
    cur.execute(query)
    myresult = cur.fetchall()
    for x in myresult:
        print(x)
    
    print("Trigger Things: ")    
    #cur.execute("create trigger deduct before insert on staff for each row set new.salary = new.salary+1;")
    cur.execute("insert into staff values ('Tom', 2, 12000, 3)") 
    query = "select * from staff"
    cur.execute(query)
    myresult = cur.fetchall()
    for x in myresult:
        print(x)
                
    print("Call Procedure: ")
    cur.callproc('get_info')
    for result in cur.stored_results():
        print(result.fetchall())
except:
    myconn.rollback()

myconn.close()

