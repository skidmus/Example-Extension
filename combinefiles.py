import os

outputfile = 'bundledScript/output.js'

if os.path.exists(outputfile):
    os.remove(outputfile)

# Creating a list of filenames
filenames = [
    'src/script/scripts/script.js'
]
 
# Open file3 in write mode
with open(outputfile, 'w') as outfile:
    for names in filenames:
        with open(names) as infile:
            outfile.write(infile.read())
            
        outfile.write("\n")
    print("Output file is " + outputfile)
