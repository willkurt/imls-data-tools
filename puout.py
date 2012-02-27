


class PuoutRecord(object):
    """
    A class for processing the Record Layout for Public Library Outlet Data File from
    The Institue of Museum and Library Studies.
    
    Futher information can be found in this file:
    https://harvester.census.gov/imls/pubs/Publications/fy2009_pls_database_documentation.pdf
    """
    
    #rather than process all of these on object creation
    #we just do a lookup each time we need one
    # fieldname (length,offset)
    fields = {
        # Two-letter Federal Information Processing Standards 
        # (FIPS) State Code
        "STABR":(2,1),
        
        # Outlet identification code assigned by IMLS.  Outlets of 
        # an administrative entity have the same FSCSKEY as 
        # their administrative entity.  The outlet is separately 
        # identified by a unique 3-digit suffix called FSCS_SE
        "FSCSKEY":(6,3),

        # Outlet's unique three-digit suffix to FSCSKEY, assigned by IMLS
        "FSCS_SEQ":(3,9),
        
        # Outlet identification code assigned by the state.  If the 
        # state did not assign a code, IMLS assigns a combination 
        # of FSCSKEY and FSCS_SEQ, separated by a dash
        "LIBID": (20,12),

        # Name of outlet
        "LIBNAME": (60,32),

        # Complete street address of outlet
        "ADDRESS": (35,92),

        # City or town of outlet
        "CITY": (20,127),

        # Standard five-digit postal zip code for street address of 
        # outlet 
        # M = Missing (unknown, not reported)
        "ZIP": (5,147),

        # Four-digit postal zip code extension for street address of 
        # outlet 
        # M = Missing (unknown, not reported)         
        "ZIP4": (4,152), 

        # County in which the outlet is physically located
        "CNTY": (20,156), 

        # Telephone number of the outlet, in following format:  
        # area code/exchange/number (e.g., 7037315072) 
        # M = missing (unknown, not reported) 
        # -3 = Not applicabl
        "PHONE": (10,176),

        # Outlet type 
        # CE–Central Library 
        # BR–Branch Library 
        # BS–Bookmobile(s) 
        # BM–Books-by-Mail Only
        "C_OUT_TY": (2,186),

        # Metropolitan Status Code 
        # CC–Central City 
        # NC–Metropolitan Area, but not within central city limits 
        # NO–Not in a Metropolitan Area 
        # M–Missing (unknown, not reported)
        "C_MSA": (2,188),

        #Area in square feet of the public library outlet
        "SQ_FEET":  (8,190)

        }



    def __init__(self,record_string):
        self.record_string = record_string


    def lookup(self,field):
        f = field.upper()
        if !fields.has_key(f):
            #maybe change to real exception later
            print("no such field: "+f)
            return ""
        else:
            pair = fields[f]
            #imls data is 1 offset            
            offset = pair[1]-1
            end_position = pair[0]+offset
            return self.record_string[offset:end_position]

        
