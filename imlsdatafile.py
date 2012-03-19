from imls_const import IMLSConst
from imlsrecord import IMLSRecord
from imlsrecord_keys import IMLSRecordKeys


class IMLSDataFile(object):
    """
    Class to handle open and reading from IMLS data files

    """

    def __init__(self,rtype,year):
        f = open(IMLSConst.DATA_PATH.format(rtype,year),'r')
        self.records = []
        self.record_dict = {}
        self.rtype = rtype
        self.year = year
        self.fields = IMLSRecordKeys.fields[rtype][year]
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

    def id_lookup(self,fscskey,key):
        return self.record_dict[fscskey].lookup(key)
    
    def to_csv(self):
        fout = open("{0}-{1}.csv".format(self.rtype,self.year),'w')
        keys = self.fields.keys()
        #i always want these 2 to be first
        #every record set should have these keys
        keys.remove('FSCSKEY')
        keys.remove('LIBNAME')
        fout.write('FSCSKEY,LIBNAME,'+','.join(keys)+'\n')
        keys = ['FSCSKEY','LIBNAME'] + keys
        for r in self.records:
            vals = []
            for k in keys:
                v = r.lookup(k) or 'NA'
                #-3 is the IMLS value for 'NA'
                #-1 is for missing
                v_strip = v.strip()
                if v is '-3' or v is '-1':
                    v = 'NA'
                v = v.replace(',','<comma>')
                vals.append(v)
            fout.write(','.join(vals)+'\n')
        fout.close()
        
