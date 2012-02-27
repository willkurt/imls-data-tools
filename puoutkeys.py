"""
ultimatley I'm going to want to pull this all out
into [filetype][year][key], but first I'll have to make some tools
to automaticlaly pull that data out... ugh
"""
class PuoutKeys:
    
    fields = {
        2009: {
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
        # CE-Central library
        # BR-Branch Library
        # BS-Bookmobiles(s)
        # BM-Books by mail only
        "C_OUT_TY": (2,186),

        # Metropolitan Status Code 
        # CC-Central City
        # NC-Metropolitian Area, not within city limits
        # NO-Not in a Metropolitan Area 
        # M-Missing (unknown, not reported)
        "C_MSA": (2,188),

        # Area in square feet of the public library outlet
        "SQ_FEET":  (8,190),

        # SQ_FEET imputation flag.
        "F_SQ_FT": (4,198),

        # Number of bookmobiles in the bookmobile outlet recor
        "L_NUM_BM":  (2,202),

        # L_NUM_BM imputation flag.  
        "F_BKMOB": (4,204),

        # FSCS submission year of public library data in 4-digit format (YYYY)  
        "YR_SUB": (4,208),

        # Structure Change Code 
        # 00-No change from last year 
        # 01-Existing Administrative Entity or Outlet absorbs 
        # another Administrative Entity or Outlet 
        # 02-Newly created Administrative Entity or Outlet 
        # 03-Closed 
        # 04-Move Outlet to a newly created Administrative Entity
        # 05-Merge two or more Administrative Entities or Outlets 
        # to form a new Administrative Entity or Outlet 
        # 06-(reserved) 
        # 07-(reserved) 
        # 08-Restored a closed Administrative Entity or Outlet 
        # record 
        # 09-Restored an incorrectly deleted Administrative Entity 
        # or Outlet 
        # 10-Delete an incorrect record 
        # 11-Outlet moved to a different previously existing 
        # Administrative Entity 
        # 12-(reserved) 
        # 13-Add an existing Administrative Entity or Outlet not 
        # previously reported 
        # 22-Future Administrative Entity FSCS ID Request 
        # 23-Temporary Closure 
        # 24-Restore/Undo Was a 23 (Reopen a Temporarily 
        # Closed Administrative Entity) 
        # (Note: This code records structure changes to 
        # administrative entities and outlets, and is included on 
        # the Public Library Data File and the Public Library 
        # Outlet File.  Structure changes include action 
        "STATSTRU": (2,212),


        # Name Change Code 
        # 00-No change from last year 
        # 06-Official name change 
        # 14-Minor name change
        "STATNAME": (2,214),
 
        # Address Change Code 
        # 00-No change from last year 
        # 07-Moved to a new location 
        # 15-Minor address change
        "STATADDR": (2,216),

        # Longitude. This field consists of a negative sign, three 
        # integers and six decimal places, with an explicit decimal 
        # point. 
        # 0.000000 - Missing
        "LONGITUD": (11,218), 

        # Latitude. This field consists of two integers and six 
        # decimal places, with an explicit decimal point. 
        # 0.000000 - Missing
        "LATITUDE": (9,229), 


        # Two-digit Federal Information Processing Standards 
        # (FIPS) State Code (assigned based on the physical 
        # location of the outlet).  (See Appendix D for list of State 
        # Codes.) 
        # 00 - Missing
        "FIPSST": (2,238),


        # Three-digit FIPS County Code (assigned based on the 
        # physical location of the outlet) 
        # 000 - Missing
        "FIPSCO": (3,240),
 
        # FIPS Place 
        # 00000 - Missing
        "FIPSPLAC": (5,243),

        # County Population 
        # -1 = Missing 
        "CNTYPOP":(8,248), 

        #  Urban-centric locale code. The geographic location in 
        # terms of the size of the community in which it is located 
        # and the proximity of that community to urban and 
        # metropolitan areas. 
        # .-Missing 
        # 11-City, Large: Territory inside an urbanized area and 
        # inside a principal city with population of 250,000 or 
        # more 
        # 12-City, Mid-size: Territory inside an urbanized area 
        # and inside a principal city with a population less than 
        # 250,000 and greater than or equal to 100,000 
        # 13-City, Small: Territory inside an urbanized area and 
        # inside a principal city with a population less than 
        # 100,000 
        # 21-Suburb, Large: Territory outside a principal city and 
        # inside an urbanized area with population of 250,000 
        # or more 
        # 22-Suburb, Mid-size: Territory outside a principal city 
        # and inside an urbanized area with a population less 
        # than 250,000 and greater than or equal to 100,000 
        # 23-Suburb, Small: Territory outside a principal city and 
        # inside an urbanized area with a population less than 
        # 100,000 
        # 31-Town, Fringe: Territory inside an urban cluster that is 
        # less than or equal to 10 miles from an urbanized area
        # 32-Town, Distant: Territory inside an urban cluster that 
        # is more than 10 miles and less than or equal to 35 
        # miles from an urbanized area 
        # 33-Town, Remote: Territory inside an urban cluster that 
        # is more than 35 miles from an urbanized area 
        # 41-Rural, Fringe: Census-defined rural territory that is 
        # less than or equal to 5 miles from an urbanized area, 
        # as well as rural territory that is less than or equal to 
        # 2.5 miles from an urban cluster 
        # 42-Rural, Distant: Census-defined rural territory that is 
        # more than 5 miles but less than or equal to 25 miles 
        # from an urbanized area, as well as rural territory that 
        # is more than 2.5 miles but less 
        # 43-Rural, Remote: Census-defined rural territory that is 
        # more than 25 miles from an urbanized area and is 
        # also more than 10 miles from an urban cluste
        "LOCALE": (2,256),

        #  Census Tract.  A small, relatively permanent statistical 
        # subdivision of a county or statistically equivalent entity 
        # delineated by local participants as part of the Census 
        # Bureau's Participant Statistical Areas Program. This field 
        # consists of four integers and two decimals, with an 
        # explicit decimal point. 
        # 0 - Missing
        "CENTRACT": (7,258),
 

        # Census Block. An area bounded on all sides by visible 
        # features, such as streets, roads, streams, and railroads 
        # tracks, and by invisible boundaries, such as city, town, 
        # township, and county limits, property lines, and short, 
        # imaginary extensions of streets and roads (designated 
        # by the Census Bureau). 
        # 0 - Missing 
        "CENBLOCK": (4, 265),

        
        # Congressional District. FIPS code based on the location 
        # of the administrative entity/outlet.  Legislatively defined 
        # subdivisions of the state for the purpose of electing 
        # representatives to the House of Representatives of the 
        # U.S. Congress. 
        # . - Missing 
        "CDCODE": (2,269),


        # Match Centroid.  The geographic level at which the 
        # address was matched. 
        # . - Missing 
        # 0-Matched the actual street of this location 
        # 4-The centroid of the 5-digit zip code + 4 area that the 
        # location falls within 
        # 2-The centroid of the 5-digit zip code + 2 area that the 
        # location falls within 
        # X-The centroid of the 5-digit zip code that the library or 
        # administrative entity is located in 
        "MAT_CENT": (1,271)
        },
        2008:{
            "STABR":(2,1),
            "FSCSKEY":(6,3),
            "FSCS_SEQ":(3,9),
            "LIBID":(20,12),
            "LIBNAME":(60,32),
            "ADDRESS":(35,92),
            "CITY":(20,127),
            "ZIP":(5,147),
            "CNTY":(20,156),
            "PHONE":(10,176),
            "C_OUT_TY":(2,186),
            "C_MSA":(2,188),
            "SQ_FEET":(8,190),
            "F_SQ_FT":(4,198),
            "L_NUM_BM":(2,202),
            "F_BKMOB":(4,204),
            "PUB_FIPS":(2,208),
            "CNTYFIPS":(3,210),
            "YR_SUB":(4,213),
            "STATSTRU":(2,217),
            "STATNAME":(2,219),
            "STATADDR":(2,221),
            "LONGITUD":(11,223),
            "LATITUDE":(9,234),
            "FIPSST":(2,243),
            "FIPSCO":(3,245),
            "FIPSPLAC":(5,248),
            "CNTYPOP":(8,253),
            "LOCALE":(2,261),
            "CENTRAC":(7,263),
            "CENBLOCK":(4,270),
            "CDCODE":(2,274),
            "MAT_CENT":(1,276)
            },

        2007:{
            "STABR":(2,1),
            "FSCSKEY":(6,3),
            "FSCS_SEQ":(3,9),
            "LIBID":(20,12),
            "LIBNAME":(60,32),
            "ADDRESS":(35,92),
            "CITY":(20,127),
            "ZIP":(5,147),
            "CNTY":(20,156),
            "PHONE":(10,176),
            "C_OUT_TY":(2,186),
            "C_MSA":(2,188),
            "SQ_FEET":(8,190),
            "F_SQ_FT":(2,198),
            "L_NUM_BM":(2,200),
            "F_BKMOB":(2,202),
            "PUB_FIPS":(2,204),
            "CNTYFIPS":(3,206),
            "YR_SUB":(4,209),
            "STATSTRU":(2,213),
            "STATNAME":(2,215),
            "STATADDR":(2,217),
            "LONGITUD":(11,219),
            "LATITUDE":(9,230),
            "FIPSST":(2,239),
            "FIPSCO":(3,241),
            "FIPSPLAC":(5,244),
            "CENTRAC":(7,249),
            "CENBLOCK":(4,256),
            "CDCODE":(2,260),
            "MAT_CENT":(1,262)
            },
        2006:{
            "STABR":(2,1),
            "FSCSKEY":(6,3),
            "FSCS_SEQ":(3,9),
            "LIBID":(20,12),
            "LIBNAME":(60,32),
            "ADDRESS":(35,92),
            "CITY":(20,127),
            "ZIP":(5,147),
            "CNTY":(20,156),
            "PHONE":(10,176),
            "C_OUT_TY":(2,186),
            "C_MSA":(2,188),
            "SQ_FEET":(8,190),
            "F_SQ_FT":(2,198),
            "L_NUM_BM":(2,200),
            "F_BKMOB":(2,202),
            "PUB_FIPS":(2,204),
            "CNTYFIPS":(3,206),
            "YR_SUB":(4,209),
            "STATSTRU":(2,213),
            "STATNAME":(2,215),
            "STATADDR":(2,217)
            },
        2005:{
            "STABR":(2,1),
            "FSCSKEY":(6,3),
            "FSCS_SEQ":(3,9),
            "LIBID":(20,12),
            "LIBNAME":(60,32),
            "ADDRESS":(35,92),
            "CITY":(20,127),
            "ZIP":(5,147),
            "CNTY":(20,156),
            "PHONE":(10,176),
            "C_OUT_TY":(2,186),
            "C_MSA":(2,188),
            "SQ_FEET":(8,190),
            "F_SQ_FT":(2,198),
            "L_NUM_BM":(2,200),
            "F_BKMOB":(2,202),
            "PUB_FIPS":(2,204),
            "CNTYFIPS":(3,206),
            "YR_SUB":(4,209),
            "STATSTRU":(2,213),
            "STATNAME":(2,215),
            "STATADDR":(2,217)
            },
        2004:{
            "STABR":(2,1),
            "FSCSKEY":(6,3),
            "FSCS_SEQ":(3,9),
            "LIBID":(20,12),
            "LIBNAME":(60,32),
            "ADDRESS":(35,92),
            "CITY":(20,127),
            "ZIP":(5,147),
            "CNTY":(20,156),
            "PHONE":(10,176),
            "C_OUT_TY":(2,186),
            "C_MSA":(2,188),
            "SQ_FEET":(8,190),
            "F_SQ_FT":(2,198),
            "L_NUM_BM":(2,200),
            "F_BKMOB":(2,202),
            "PUB_FIPS":(2,204),
            "CNTYFIPS":(3,206),
            "YR_SUB":(4,209)
            },
        2003:{
            "STABR":(2,1),
            "FSCSKEY":(6,3),
            "FSCS_SEQ":(3,9),
            "LIBID":(20,12),
            "LIBNAME":(60,32),
            "ADDRESS":(35,92),
            "CITY":(20,127),
            "ZIP":(5,147),
            "CNTY":(20,156),
            "PHONE":(10,176),
            "C_OUT_TY":(2,186),
            "C_MSA":(2,188),
            "SQ_FEET":(8,190),
            "F_SQ_FT":(2,198),
            "L_NUM_BM":(2,200),
            "F_BKMOB":(2,202),
            "PUB_FIPS":(2,204),
            "CNTYFIPS":(3,206),
            "YR_SUB":(4,209)
            },
        2002:{
            "STABR":(2,1),
            "FSCSKEY":(6,3),
            "FSCS_SEQ":(3,9),
            "LIBID":(20,12),
            "LIBNAME":(45,32),
            "ADDRESS":(35,77),
            "CITY":(17,112),
            "CNTY":(17,129),
            "ZIP":(5,146),
            "PHONE":(10,155),
            "C_OUT_TY":(2,165),
            "C_MSA":(2,167),
            "SQ_FEET":(8,169),
            "L_NUM_BM":(2,177),
            "PUB_FIPS":(2,179),
            "CNTYFIPS":(3,181),
            "YR_SUB":(4,184)
            },
        2001:{
            "STABR":(2,1),
            "FSCSKEY":(6,3),
            "FSCS_SEQ":(3,9),
            "LIBID":(20,12),
            "LIBNAME":(45,32),
            "ADDRESS":(35,77),
            "CITY":(17,112),
            "CNTY":(17,129),
            "ZIP":(5,146),
            "PHONE":(10,155),
            "C_OUT_TY":(2,165),
            "C_MSA":(2,167),
            "L_NUM_BM":(2,169),
            "WEB_ADDR":(50,171),
            "PUB_FIPS":(2,221),
            "CNTYFIPS":(3,223),
            "YR_SUB":(4,226)
            },
        2000:{
            "STABR":(2,1),
            "FSCSKEY":(6,3),
            "FSCS_SEQ":(3,9),
            "LIBID":(20,12),
            "LIBNAME":(45,32),
            "ADDRESS":(35,77),
            "CITY":(17,112),
            "CNTY":(17,129),
            "ZIP":(5,146),
            "PHONE":(10,155),
            "C_MSA":(2,167),
            "L_NUM_BM":(2,169),
            "WEB_ADDR":(50,171),
            "PUB_FIPS":(2,221),
            "CNTYFIPS":(3,223),
            "YR_SUB":(4,226)
            },
        1999:{
            "STABR":(2,1),
            "FSCSKEY":(6,3),
            "FSCS_SEQ":(3,9),
            "LIBID":(20,12),
            "LIBNAME":(45,32),
            "ADDRESS":(35,77),
            "CITY":(17,112),
            "CNTY":(17,129),
            "ZIP":(5,146),
            "PHONE":(10,155),
            "C_MSA":(2,167),
            "L_NUM_BM":(2,169),
            "WEB_ADDR":(50,171),
            "PUB_FIPS":(2,221),
            "CNTYFIPS":(3,223),
            "YR_SUB":(4,226)
            },
        1998:{
            "STABR":(2,1),
            "FSCSKEY":(6,3),
            "FSCS_SEQ":(3,9),
            "LIBID":(20,12),
            "LIBNAME":(45,32),
            "ADDRESS":(35,77),
            "CITY":(17,112),
            "CNTY":(17,129),
            "ZIP":(5,146),
            "PHONE":(10,155),
            "C_MSA":(2,167),
            "L_NUM_BM":(2,169),
            "WEB_ADDR":(50,171),
            "PUB_FIPS":(2,221),
            "CNTYFIPS":(3,223),
            "YR_SUB":(4,226)
            }

}
