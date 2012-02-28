from imlsdatafile import IMLSDataFile


rtype = "puout"

#just playing with some sample years

d2008 = IMLSDataFile(rtype,2008) 
d1998 = IMLSDataFile(rtype,1998) 


s2008 = d2008.select_all_s("FSCSKEY")
s1998 = d1998.select_all_s("FSCSKEY")


missingLibs = s1998.difference(s2008)
for ml in missingLibs:
    print(d1998.id_lookup(ml,"libname"))
print("missing {0} libs".format(len(missingLibs)))
