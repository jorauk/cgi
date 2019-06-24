#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
operands = form.getlist('operand')
total = sum(map(int, operands))

print("Content-type: text/plain")
print()
print("The numbers you are attempting to add: ", end="")
print(*operands, sep=" + ")
print("The sum is: {}".format(str(total)))
