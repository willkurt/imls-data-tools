from puoutkeys import PuoutKeys


class PuoutRecord(object):
    """
    A class for processing the Record Layout for Public Library Outlet Data File from
    The Institue of Museum and Library Studies.
    
    Futher information can be found in this file:
    https://harvester.census.gov/imls/pubs/Publications/fy2009_pls_database_documentation.pdf
    """
    
    def __init__(self,record_string,year):
        self.record_string = record_string
        self.year = year

    def lookup(self,field):
        f = field.upper()
        if not PuoutKeys.fields[self.year].has_key(f):
            #maybe change to real exception later
            print("no such field: "+f)
            return ""
        else:
            pair = PuoutKeys.fields[self.year][f]
            #imls data is 1 offset            
            offset = pair[1]-1
            end_position = pair[0]+offset
            return self.record_string[offset:end_position]

        
