#!C:/Users/dell laptap/AppData/Local/Programs/Python/Python36/python.exe
print("Content-Type:text/html")
print("""""")
print("<html>")
print("    <link href='admin/assets/plugins/bootstrap/css/bootstrap.min.css' rel='stylesheet'>")
print("    <link href='admin/main/css/style.css' rel='stylesheet'>")
print("<body><center>")
print("<h4><center>Prediction Of Turnover(in Lakhs) On The Basis Of Close Price And Total Trade Quantity</center></h4>")
print("<form align='center' action='Submit_CP_TT.py'>")
print("<table class='table table-bordered' align='center' style='font-size:12px;'>")
print("<tr><td><b>Enter Close Price:</b></td>")
print("<td><input type='text' class='form-control' name='CP' required></td>")
print("<tr><td><b>Enter Total Trade Quantiy:</b></td>")
print("<td><input type='text' class='form-control' name='TT' required></td>")
print("</tr>")
print("</table>")
print("<button id=btn class='btn btn-info btn-xs'>Submit</button>")
print("</form>")
print("</center></html")