#!C:/Users/dell laptap/AppData/Local/Programs/Python/Python36/python.exe
import cgi
import finalproject as fp
print("Content-Type:text/html")
print("""""")
print("<html>")
print("    <link href='admin/assets/plugins/bootstrap/css/bootstrap.min.css' rel='stylesheet'>")
print("    <link href='admin/main/css/style.css' rel='stylesheet'>")
print("<body><center>")
f=fp.Project()
request=cgi.FieldStorage()
CP=float(request.getvalue('CP'))
res=f.Prediction_CP_Turnover(CP)
res1=f.Intercept_Slope_CP_Turn()

print("<span><a href=ClosePrice_Turnover.py target=mw align='right'>Back</a></span><br>")
print("<h1><center>ClosePrice VS TurnOver</center></h1>")
print("<table class='table table-bordered' align='center' style='font-size:14px;'>")
print("<tr><th><b><i>Predicted TurnOver(in Lakhs) For Close Price {}</i></b>".format(CP))
print("<th><b><i>Intercept</i></b>")
print("<th><b><i>Slope</i></b>")
print("<th><b><i>Residual</i></b>")
print("<th><b><i>Score</i></b>")
print("</tr>")
print("<tr>")
print("<td>{}</td>".format(res))
print("<td>{}</td>".format(res1[0]))
print("<td>{}</td>".format(res1[1]))
print("<td>{}</td>".format(res1[0]))
print("<td>{}</td>".format(res1[1]))
print("</tr>")
print("</table>")
print("<a href=G_CP_turn.py class='btn btn-danger btn-xs'>GRAPHS:</a><br>")
print("</center></body>")
print("</html>")
