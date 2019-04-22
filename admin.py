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
print('<marquee behavior="alternate" scrollamount="30" style="margin-left:sem;margin-right:sem;">SNAPSTORE </marquee>')
print('</div>')
print('<div style="background-color:rgba(30, 110, 150, 0.8);width:100%;height:70%;font-size:30;">')
print('<center>ADMIN LOGIN</center>')
print('<table  width="30%" height="70%" align="center">')
print('<center>')
print('<tr>')
print('<td >')
print('<input type="submit" name="cp" value=Change_Password>')
print('</td>')
print('<td>')
print('<input type="submit" name="sct" value=Show_Complete_table>')
print('</td>')
print('</tr>')
print('<tr>')
print('<td>')
print('<input type="submit" name="st" value=Display_Data_by_id>')
print('</td>')
print('<td>')
print('<input type="submit" name="up" value=Update >')
print('</td>')
print('</tr>')
print('<tr>')
print('<td>')
print('<input type="submit" name="dp" value=Delete>')
print('</td>')
print('<td>')
print('<input type="submit" name="Fp" value="Forget Password?">')
print('</td>')
print('</tr>')
print('</center>')
print('</table>')
form=cgi.FieldStorage()
if(form.getvalue("Fp")):
    webbrowser.open('http://localhost/Project/forgetpass.py')
elif(form.getvalue("sct")):   
    webbrowser.open("http://localhost/Project/DisplayData.py")
elif(form.getvalue("st")):   
    webbrowser.open("http://localhost/Project/DisplayData2.py")
elif(form.getvalue("dp")):   
    webbrowser.open("http://localhost/Project/delete.py")
elif(form.getvalue("cp")):   
    webbrowser.open("http://localhost/Project/ll.py")
elif(form.getvalue("up")):   
    webbrowser.open("http://localhost/Project/update.py")     
print('</div>')
print('<div style="background-color:lightblue;width:100%;height:15%;font-size:20;">')
print('<marquee behavior="left" scrollamount="10" vspace="1%" style="margin-left:sem;margin-right:sem;">Please be aware that this Registration Form, when completed, along with the Guide and the Declaration of Acceptance, is your contract with Snapstore and that in signing you are agreeing to the terms and conditions listed below</marquee>')
print('</div>')
print('</form></body>')
print('</html>')




