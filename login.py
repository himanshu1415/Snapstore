#!\Users\himanshu\AppData\Local\Programs\Python\Python36-32\python.exe
print('content-type:text/html\r\n\n')
import webbrowser,MySQLdb
print('<html>')
print('<head>')
print('</head>')
print('<body style="margin:80;">')
print('<form method="post">')
print('<table width="40%" height="70%" align="center" bgcolor="white">')
print('<tr>')
print('<td colspan="2" align="center">')
print('<img src="1.jpg" alt="SnapStore_Icon">')
print('</td>')
print('</tr>')
print('<tr>')
print('<td>')
print('USERNAME:')
print('</td>')
print('<td>')
print('<input type="text" name="id">')
print('</td>')
print('</tr>')
print('<tr>')
print('<td>')
print('PASSWORD:')
print('</td>')
print('<td>')
print('<input type="text" name="pa">')
print('</td>')
print('</tr>')
print('<tr>')
print('<td colspan=2>')
print('<center>')
print('<input type="submit" name="submit" value="SIGN IN">')
print('</center>')
print('</td>')
print('</tr>')
print('<tr>')
print('<td>')
print('<input type="submit" name="Sign_Up" value="Register">')
print('</td>')
print('<td align="right">')
print('<input type="submit" name="Fp" value="Forget Password?">')
print('</td>')
print('</tr>')
print('</table>')
print('</form>')
import cgi,cgitb
form=cgi.FieldStorage()
count=0
try:
    db=MySQLdb.connect("localhost","root","root","class")
    cur=db.cursor()
    sql="select * from data"
    cur.execute(sql)
except Exception:
    print("Not Found")
else:
    result=cur.fetchall()
    if(form.getvalue("submit")):
        id=form.getvalue("id")
        p=form.getvalue("pa")
        for i in result:
            if(id=="admin" and p=="admin"):
                webbrowser.open('http://localhost/Project/admin.py')
                count=count+1
                break
            elif(id==i[2] and p==i[3]):
                webbrowser.open('http://www.thesnapstoreapp.com/')
                count=count+1
                break
        if(count==0):
                print('<center>USERNAME OR PASSWORD INCORRECT</center>')
    elif(form.getvalue("Sign_Up")):
        webbrowser.open('http://localhost/Project/index.py')
    elif(form.getvalue("Fp")):
        webbrowser.open('http://localhost/Project/ll.py')
finally:
    db.close()
print('</body>')
print('</html>')
