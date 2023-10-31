#!/usr/bin/env python

import cgi
import cgitb

# Enable detailed error messages
cgitb.enable()

# Get form data
form = cgi.FieldStorage()

# Check if the username and password match
if form.getvalue("username") == "abc" and form.getvalue("password") == "abc":
    result_message = "Login successful! Welcome, abc."
else:
    result_message = "Invalid username or password. Please try again."

# Generate an HTML response
print("Content-type: text/html\n")
print("<html>")
print("<head><title>Sign In Result</title></head>")
print("<body>")
print("<h1>Sign In Result</h1>")
print("<p>{}</p>".format(result_message))
print("</body>")
print("</html>")
