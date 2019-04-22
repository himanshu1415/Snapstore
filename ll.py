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
print('<div style="background-color:lightblue;width:100%;height:17%;font-size:50;">')
print('<marquee behavior="alternate" scrollamount="30" style="margin-left:sem;margin-right:sem;">SNAPSTORE</marquee>')
print('</div>')
print('<div style="background-color:rgba(30, 110, 150, 0.8);width:100%;height:70%;font-size:30;">')
print('<div style="width:25%;height:100%;font-size:30;float:left;">')
print('<br><br><br><br><br><br>')
print('<center><input type="button" name="Back" value="Back" onclick=location.href="admin.py"><center>')
print('</div>')
print('<div style="width:75%;height:100%;font-size:30;float:right;">')
print('<div style="width:65%;height:100%;font-size:30;float:left;">')
print('<table align="center" width="100%" height="310">')
print('<caption style="font-size:30;">CHANGE PASSWORD</caption><br>')
print('<tr><center><td></td></center><td><center></td></center></tr>')
print('<tr><center><td></td></center><td><center></td></center></tr>')
print('<tr><center><td>Username :</td></center><td><center><input type="text" name="uname"></td></center></tr>')
print('<tr><center><td>Original Password :</td></center><td><center><input type="password" name="op"></td></center></tr>')
print('<tr><center><td>Confirm Password :</td></center><td><center><input type="password" name="cp"></td></center></tr>')
print('<tr><center><td>New Password :</td></center><td><center><input type="password" name="np"></td></center></tr>')
print('</table>')
print('</div>')
print('<div style="width:35%;height:100%;font-size:30;float:right">')
print('<br><br><br><br><br><br>')
print('<center><input type="submit" name="register" value="Change_Password"><center>')
#----------
form=cgi.FieldStorage()
count=0
if(form.getvalue("register")):
    uname=form.getvalue('uname')
    op=form.getvalue('op')
    cp=form.getvalue('cp')
    np=form.getvalue('np')
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
            if(i[3]==op):
                if(op==cp):
                    
                    sql2="update data set password=%s where user_name =%s"
                    cur.execute(sql2,[np,uname])
                    db.commit()
                    sql3="update data set confirm_pass=%s where user_name =%s"
                    cur.execute(sql3,[np,uname])
                    db.commit()
                else:
                    print("Confirm password and old password doesnot match")
            else:
                print("Wrong Password...")
        
    finally:
        db.close()
elif(form.getvalue("Back")):
    webrowser.open("http://localhost/Project/admin.py")        
print('</div>')
print('</div>')
print('</div>')
print('<div style="background-color:lightblue;width:100%;height:12%;font-size:20;">')
print('<marquee behavior="left" vspace="1%" scrollamount="10" style="margin-left:sem;margin-right:sem;">Please be aware that this Registration Form, when completed, along with the Guide and the Declaration of Acceptance, is your contract with Snapstore and that in signing you are agreeing to the terms and conditions listed below</marquee>')
print('</div>')
print('</form></body>')
print('</html>')
