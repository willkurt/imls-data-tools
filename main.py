from imlsrecord import IMLSRecord

if __name__ == "__main__":
    print("sanity check for IMLSRecord")
    fpuout = open("./data/puout/puout2009.txt",'r')
    testObj = IMLSRecord(fpuout.readline(),"puout",2009)
    print("puout data")
    print("Print Name and address for test library")
    print(testObj.lookup("libname"))
    print(testObj.lookup("address"))
    print(testObj.lookup("city"))
    print(testObj.lookup("zip"))
    fpuout.close()

    print("pupld data")
    
    print("pusum data")
    


