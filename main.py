from imlsrecord import IMLSRecord
from imlsdatafile import IMLSDataFile

#right now this main is just for experimenting
#and playing around with code


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
    df = IMLSDataFile('pupld',2009)
    df.to_csv()
    print("2009 csv complete")
    df2 = IMLSDataFile('pupld',2008)
    df2.to_csv()
    print("2008 csv complete")
    df3 = IMLSDataFile('pupld',2007)
    df3.to_csv()
    print("2007 csv complete")
    df4 = IMLSDataFile('pupld',2006)
    df4.to_csv()
    print("2006 csv complete")

    print("pusum data")
    


