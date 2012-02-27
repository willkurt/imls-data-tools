from puout import PuoutRecord

if __name__ == "__main__":
    print("sanity check for PuoutRecord")
    f = open("./data/puout/puout2009.txt",'r')
    testObj = PuoutRecord(f.readline(),2009)
    print("Print Name and address for test library")
    print(testObj.lookup("libname"))
    print(testObj.lookup("address"))
    print(testObj.lookup("city"))
    print(testObj.lookup("zip"))

    f2 = open("./data/puout/puout2008.txt",'r')
    print("counting total public libraries closed in 2008")
    total_closed = 0
    branches_closed = 0
    total = 0
    for line in f2:
        total += 1
        r = PuoutRecord(line,2008)
        status = r.lookup("statstru")
        if status == "03":
            total_closed += 1
            if r.lookup("c_out_ty") == "BR":
                branches_closed += 1
    print("Total closed: "+str(total_closed))
    print("Branches closed: "+str(branches_closed))
    p =  total_closed/total*100.00

