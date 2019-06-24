#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
operands = form.getlist('operand')
total = sum(map(float, operands))

print("Content-type: text/plain")
print()
print("The numbers you are attempting to add: {}".format(str(operands)))
print("The sum is: {}".format(str(total)))
