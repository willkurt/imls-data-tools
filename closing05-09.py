from puout import PuoutRecord

if __name__ == "__main__":
    print("total closing/year 2005-2009")
    for year in range(2005,2010):
        f = open("./data/puout/puout{0}.txt".format(year),'r')
        total_closed = 0
        branches_closed = 0
        total = 0
        for line in f:
            total += 1
            r = PuoutRecord(line,year)
            status = r.lookup("statstru")
            if status == "03":
                total_closed += 1
                if r.lookup("c_out_ty") == "BR":
                    branches_closed += 1
        print("{0} {1} {2}".format(year,total_closed,branches_closed))
    print("all done!")

