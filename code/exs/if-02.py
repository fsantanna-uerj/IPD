v1 = raw_input("v1 = ")
v2 = raw_input("v2 = ")
v3 = raw_input("v3 = ")
if v1 > v2:
    if v1 > v3:
        print "maior: ", v1
    else:
        print "maior: ", v3
else:
    if v2 > v3:
        print "maior: ", v2
    else:
        print "maior: ", v3
