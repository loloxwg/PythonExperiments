filename = 'demo.py'
with open(filename,'r') as fp:
    lines = fp.readline()
    maxlength = len(max(lines,key = len))
lines = [ '#' + str(index) + lines.ljust(maxlength)+"\n"
         for index,line in enumerate(lines)]
with open(filename[:-3]+'_new.py','w') as fp:
    fp.writelines(lines)