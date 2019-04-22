#!\Users\himanshu\AppData\Local\Programs\Python\Python36-32\python.exe
import webbrowser
import cgi,cgitb
import MySQLdb

print('content-type:text/html\r\n\n')
print('<html>')
print('<head>')
print('</head>')
print('<body style="margin:0;">')
print('<form method="post">')
print('<div style="background-color:lightblue;width:100%;height:15%;font-size:50;">')
print('<marquee behavior="alternate" scrollamount="30" style="margin-left:sem;margin-right:sem;">SNAPSTORE</marquee>')
print('</div>')
print('<div style="background-color:rgba(30, 110, 150, 0.8);width:100%;height:70%;font-size:30;">')
print('<center>DISPLAY DATA</center>')
print('<div style="width:15%;height:100%;font-size:30;float:left;">')
print('<br><br><br><br><br><br>')
print('<center><input type="submit" name="Back" value="Back"><center>')
print('</div>')
print('<div style="width:85%;height:100%;font-size:30;float:right;">')
print('<div style="width:80%;height:100%;font-size:30;float:left;">')

form=cgi.FieldStorage()
count=0
if(form.getvalue("show")):
    try:
        db=MySQLdb.connect("localhost","root","root","class")
        cur=db.cursor()
        sql="select * from data"
        cur.execute(sql)
    except Exception:
        print("Not Found")
       
    else:
        lsit1=['ID','Name','Username','password','Confirm pass','Email','M-NO','Gender','state','salary'] 
        res=cur.fetchall()
        print('<table border="1" width="100%">')
        
        for i in res:
            print('<tr>')
            for j in range(0,10):
                print('<td>',i[j],'</td>')
            print('</tr>')
        print("</table>")   
    finally:
        db.close()
elif(form.getvalue("Back")):
    webbrowser.open("http://localhost/Project/Admin.py")
print('</div>')
print('<div style="width:20%;height:100%;font-size:30;float:right">')
print('<br><br><br><br><br><br>')
print('<center><input type="submit" name="show" value="Display"><center>')
print('</div>')
print('</div>')
print('</div>')
print('<div style="background-color:lightblue;width:100%;height:15%;font-size:20;">')
print('<marquee behavior="left" vspace="1%" scrollamount="10" style="margin-left:sem;margin-right:sem;">Please be aware that this Registration Form, when completed, along with the Guide and the Declaration of Acceptance, is your contract with Snapstore and that in signing you are agreeing to the terms and conditions listed below</marquee>')
print('</div>')
print('</form></body>')
print('</html>')




