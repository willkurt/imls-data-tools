from imlsdatafile import IMLSDataFile


rtype = "puout"

#just playing with some sample years

for i in range(2008,2009):
    d1 = IMLSDataFile(rtype,i)
    d2 = IMLSDataFile(rtype,i+1)
    s1 = d1.select_all_s("FSCSKEY")
    s2 = d2.select_all_s("FSCSKEY")
    diff = s1.difference(s2)
#    print(diff)
    print("missing from record {0}".format(i))
    for i in diff:
        name = d1.id_lookup(i,"LIBNAME")
        city = d1.id_lookup(i,"CITY")
        state = d1.id_lookup(i,"STABR")
        print("{0} - {1},{2}".format(name.strip(),city.strip(),state))
                            
#    print("missing {0}-{1}: {2}".format(i,i+1,len(diff)))


