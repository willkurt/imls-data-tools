import re
"""
Takes raw data about field mapping from imls and creates a python dictionary
"""
for year in range(2003,2010):
    fin = "./pusum_keys_raw/{0}.txt".format(year)
    fout = "./pusum_keys_processed/{0}.txt".format(year)
    print("reading from {0}".format(fin))
    fr = open(fin,'r')
    fw = open(fout,'w')
    p = re.compile("([A-Z_]+) +([0-9]+) +([0-9]+)")
    fw.write("{0}:\{1}n".format(year,'{'))
    for line in fr:
        m = p.match(line)
        if m:
            fw.write("\"{0}\":({1},{2}),\n".format(m.group(1),int(m.group(2)),int(m.group(3))))

    fw.write("}")
    fr.close()

    fw.close()
print("all done!!!")
