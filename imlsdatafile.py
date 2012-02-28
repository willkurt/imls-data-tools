from imls_const import IMLSConst
from imlsrecord import IMLSRecord


class IMLSDataFile(object):
    """
    Class to handle open and reading from IMLS data files

    """

    def __init__(self,rtype,year):
        f = open(IMLSConst.DATA_PATH.format(rtype,year),'r')
        self.records = []
        self.record_dict = {}
        for line in f.readlines():
            rec = IMLSRecord(line,rtype,year)
            self.records.append(rec)
            #this might be specific to puout format, be carful
            self.record_dict[rec.lookup("FSCSKEY")] = rec

    
    def select_all(self,field_name):
        vals = []
        for r in self.records:
            vals.append(r.lookup(field_name))
        return vals

    #like select all but returns a set
    def select_all_s(self,field_name):
        return set(self.select_all(field_name))

    
    #assumes numeric data
    #calculates a float
    #also it breaks stupid easy... needs more regex ;)
    def sum(self,field_name):
        total = 0
        for r in self.records:
            total += float(r.lookup(field_name))
                 

    def id_lookup(self,fscskey,key):
        return self.record_dict[fscskey].lookup(key)
                  
