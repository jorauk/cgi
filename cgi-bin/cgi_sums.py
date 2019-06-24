#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
listval = form.getlist('operand')

print("Content-type: text/plain")
print()
print("The numbers: {}".format(str(listval)))
