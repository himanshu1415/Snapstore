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
print('<div style="width:25%;height:100%;font-size:30;float:left;">')
print('<br><br><br><br><br><br>')
print('<center><input type="submit" name="Back" value="Back"><center>')
print('</div>')
print('<div style="width:75%;height:100%;font-size:30;float:right;">')
print('<div style="width:65%;height:100%;font-size:30;float:left;">')
print('<table align="center" width="100%" height="310">')
print('<caption style="font-size:30;">FORGET PASSWORD</caption><br>')
print('<tr><center><td></td></center><td><center></td></center></tr>')
print('<tr><center><td></td></center><td><center></td></center></tr>')
print('<tr><center><td>Username :</td></center><td><center><input type="text" name="nam"></td></center></tr>')
print('<tr><center><td>Email Id :</td></center><td><center><input type="text" name="un"></td></center></tr>')
print('<tr><center><td>Mobile No. :</td></center><td><center><input type="text" name="pas"></td></center></tr>')
print('</table>')
print('</div>')
print('<div style="width:35%;height:100%;font-size:30;float:right">')
print('<br><br><br><br><br><br>')
print('<center><input type="submit" name="register" value="SHOW"><center>')

form=cgi.FieldStorage()
count=0
if(form.getvalue("register")):
    uname=form.getvalue('nam')
    eid=form.getvalue('un')
    mno=int(form.getvalue('pas'))
    try:
        db=MySQLdb.connect("localhost","root","root","class")
        cur=db.cursor()
        sql="select * from data where user_name=%s"
        cur.execute(sql,[uname])
    except Exception:
        print("Not Found")
    else:
        res=cur.fetchall()
        for i in res:
            if(i[5]==eid and i[6]==mno):
                    
                sql2="select password from data where user_name=%s"
                cur.execute(sql2,[uname])
                res2=cur.fetchall()
                print('<br><br>')
                print("<center>Password:<input type='text' name='id' value=",i[3],"></center>")
            else:
                print("Either email or mobile no is wrong...")
    finally:
        db.close()
elif(form.getvalue("Back")):
    webbrowser.open('http://localhost/Project/admin.py')
print('</div>')
print('</div>')
print('</div>')
print('<div style="background-color:lightblue;width:100%;height:14%;font-size:20;">')
print('<marquee behavior="left" vspace="1%" scrollamount="10" style="margin-left:sem;margin-right:sem;">Please be aware that this Registration Form, when completed, along with the Guide and the Declaration of Acceptance, is your contract with Snapstore and that in signing you are agreeing to the terms and conditions listed below</marquee>')
print('</div>')
print('</form></body>')
print('</html>')




