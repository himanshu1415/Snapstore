#!\Users\himanshu\AppData\Local\Programs\Python\Python36-32\python.exe
import cgi,cgitb
import MySQLdb
print('content-type:text/html\r\n\n')
import webbrowser
print('<html>')
print('<head>')
print('</head>')
print('<body style="margin:0;">')
print('<form method="post">')
print('<div style="background-color:lightblue;width:100%;height:15%;font-size:50;">')
print('<marquee behavior="alternate" scrollamount="30" style="margin-left:sem;margin-right:sem;">SNAPSTORE</marquee>')
print('</div>')
print('<div style="background-color:rgba(30, 110, 150, 0.8);width:100%;height:70%;font-size:30;">')
print('<div style="width:15%;height:100%;font-size:30;float:left;">')
print('<br><br><br><br><br><br>')
print('<center><input type="submit" name="back" value="Back"><center>')
print('</div>')
print('<div style="width:85%;height:100%;font-size:30;float:right;">')
print('<div style="width:80%;height:100%;font-size:30;float:left;">')
print("<center>Enter User id : <input type='text' name='id'></center>")
import cgi,cgitb,MySQLdb
form=cgi.FieldStorage()
if(form.getvalue("submit")):
     iid=int(form.getvalue("id"))
     db=MySQLdb.connect("localhost","root","root","class")
     cur=db.cursor()
     try:
        sql="Delete from data where id='%s'"
        cur.execute(sql,[iid])
        db.commit()
        print('<center>Data Deleted</center>')
     except:
        db.rollback()
     finally:
        db.close()
elif(form.getvalue("back")):
    webbrowser.open('http://localhost/Project/admin.py')
print('</div>')
print('<div style="width:20%;height:100%;font-size:30;float:right">')
print('<br><br><br><br><br><br>')
print('<center><input type="submit" name="submit" value="Delete"><center>')
print('</div>')
print('</div>')
print('</div>')
print('<div style="background-color:lightblue;width:100%;height:15%;font-size:30;">')
print('<marquee behavior="left" vpace="1%" scrollamount="10" style="margin-left:sem;margin-right:sem;">Please be aware that this Registration Form, when completed, along with the Guide and the Declaration of Acceptance, is your contract with Snapstore and that in signing you are agreeing to the terms and conditions listed below</marquee>')
print('</div>')

print('</form></body>')
print('</html>')
