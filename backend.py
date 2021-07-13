import mysql.connector as mysql
from mysql.connector import Error

def getConnection():
    try:                  
        mydb = mysql.connect(
        host="localhost",
        user="root",
        password="",
        database='db_license')       
    except Error as e:
        print(e)
    finally:
        if mydb.is_connected():
            print('db closed')  
            return mydb

def create():    
    mydb = getConnection()
    #mycursor.execute("CREATE DATABASE db_license")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE document_detail(branch VARCHAR(255), name VARCHAR(255),documentNumber VARCHAR(255),offence TEXT, fine INT, date DATE)")
    mycursor.close()

def insert(branch, tname,docType, documentNumber,owner,offence,fine,date,count,vType):    
    mydb = getConnection()
    try:        
        mycursor = mydb.cursor()
        sql = 'SELECT count,flag,fine FROM document_detail WHERE docNumber = %s '%documentNumber
        mycursor.execute(sql)
        result = mycursor.fetchone()              
        print(result)
        if result is not None:
            count = result[0]
            flag = result[1]
            if flag == 1:
                fine = result[2]+int(fine)
            count +=1
            flag=1
            print(branch,offence,fine,date,count,flag)
            
            val = (branch,tname,offence,fine,date,count,flag,documentNumber)

            sql = 'UPDATE document_detail SET  branch=%s ,trafficName=%s, offence= %s,fine= %s,date=%s,count=%s,flag=%s where docNumber =%s'
            mycursor.execute(sql,val)
            mydb.commit()
            
            print("Data updated ")
            
        else:
            val = (branch, tname,docType, documentNumber,owner,offence,fine,date,count,vType)
            sql = "INSERT INTO document_detail( branch, trafficName,documenType, docNumber,ownerName, offence,fine,date,count,vehicleType) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(sql,val)
            mydb.commit()
            print("new data added ")
    except Error as e:
        print('ERROR')
        print(e)
    finally:
        mydb.close()

    

def fetch():
    mydb = getConnection()
    mycursor = mydb.cursor()    
    mycursor.execute("SELECT  branch,documenType, docNumber, offence,fine,date,count FROM document_detail order by date")
    result = mycursor.fetchall()
    mycursor.close()
    return result


def search(documentNumber):    
    mydb = getConnection()
    mycursor = mydb.cursor()  
    sql = 'SELECT * FROM document_detail WHERE docNumber = %s '%documentNumber    
    mycursor.execute(sql)
    result = mycursor.fetchone()
    mycursor.close()
    return result


def delete(id):
    mydb = getConnection()
    mycursor = mydb.cursor()  
    sql = 'DELETE FROM document_detail WHERE id = %d '%id    
    mycursor.execute(sql)
    mycursor.close()

def update(id,branch, name,documentNumber,offence,fine,date):
    mydb = getConnection()
    mycursor = mydb.cursor()
    sql = 'UPDATE document_detail SET branch, name,documentNumber,offence,fine,date) values (%s,%s,%s,%s,%d,%s) WHERE id=%s'%(branch, name,documentNumber,offence,fine,date,id)
    mycursor.execute(sql)
    mycursor.close()


#insert message 
def insertMsg(title,msg,desc,loc,date):    
    mydb = getConnection()
    try:        
        mycursor = mydb.cursor()
        val = (title,msg,desc,loc,date)
        sql = "INSERT INTO message(title,msg,descrip,loc,date) values (%s,%s,%s,%s,%s)"
        mycursor.execute(sql,val)
        mydb.commit()
        print("new data added ")
    except Error as e:
        print('ERROR')
        print(e)
    finally:
        mydb.close()

#retrive all message
def fetchMsg():
    mydb = getConnection()
    mycursor = mydb.cursor()    
    mycursor.execute("SELECT date,title,msg,descrip,loc FROM message ORDER BY date")
    result = mycursor.fetchall()
    mycursor.close()
    return result

#collecting data for bar 
def bar():
    mydb = getConnection()
    mycursor = mydb.cursor()    
    mycursor.execute("SELECT branch, sum(count) FROM document_detail group by branch")
    count = mycursor.fetchall()
    mycursor.close()
    return count

#collecting data for line 
def line():
    mydb = getConnection()   
    mycursor = mydb.cursor()  
    mycursor.execute("SELECT date, sum(count) FROM document_detail group by date ")
    result = mycursor.fetchall()
    mycursor.close()
    return result

#Calculate total fine colledted 
def fund():
    mydb = getConnection()   
    mycursor = mydb.cursor()  
    mycursor.execute("SELECT sum(totalFine) FROM payment")
    result = mycursor.fetchall()
    mycursor.close()    
    for x in result:
        text = x[0]        
    return text

def insert_payment(data):
    mydb = getConnection()
    try:        
        mycursor = mydb.cursor()
        val = (data[0],data[1],data[2])
        sql = "INSERT INTO payment(doc_id,voucher,bill) values (%s,%s,%s)"
        mycursor.execute(sql,val)
        sql = 'UPDATE document_detail SET upload = 1 where docNumber = %s'%data[0]
        mycursor.execute(sql)

        mydb.commit()
    except Error as e:
        print('ERROR')
        print(e)
    finally:
        mydb.close()

def fetch_payment():    
    mydb = getConnection()   
    mycursor = mydb.cursor()  
    mycursor.execute("SELECT * FROM payment where isVarified = 0")
    result = mycursor.fetchall()
    mycursor.close()  
    return result

#Update document detail once payment is verified 
def verified(flag,key):
    mydb = getConnection()
    mycursor = mydb.cursor()
    sql = 'UPDATE document_detail SET flag = {0} where docNumber = {1}'.format(flag, key)
    mycursor.execute(sql)
    mydb.commit()
    mycursor.close()
    print('flag updated ')

def verifyPayment(key,fine):    
    mydb = getConnection()
    mycursor = mydb.cursor()
    print(key)
    mycursor.execute('select totalFine from payment where doc_id = %s'%key)
    totalfine = mycursor.fetchone()   
    #if(totalfine[0] == None):
    #    totalfine[0] = 0;  
    print(fine)
    print(totalfine[0])

    totalfine = fine+totalfine[0];      
 
    sql = 'update payment set isVarified = 1,totalFine =%s where doc_id = %s'%(totalfine,key)
    mycursor.execute(sql)    
    mydb.commit()
    print('number of rows deleted', mycursor.rowcount)
    mycursor.close()







'''
add bill no 
add count variable in dba 
'''

if __name__ == "__main__":
    #getConnection()
    #insert('ktm','ramen','license','9999','me', 'killed me', 100,'2020-03-12',0,'bike')
    #branch, tname,docType, documentNumber,owner,offence,fine,date,count,vType
    #print(fetch())

    #print('thois is text'+str(fund()))\\
    #insert_payment(123, "file path", "file path ")
    #deletePayment(123)
    #verified(0, 1234)\
    print(search(1234))