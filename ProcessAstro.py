import csv, re

#Open the file and read as dot delimited

def readLev(row):
    level=0
    pattern = re.compile("[a-zA-Z]")
    for col in row:
        if pattern.search(col) !=None:
            level=row.index(col)
    return level
    

with open('B:\PythonFiles\PythonInOut\AstroObject\Astro.csv', 'rb') as csvfile:
    astroReader = csv.reader(csvfile, delimiter='.')
    astroJson='{"name": "Astronomical Object"'
    prevLev=0
    for row in astroReader:
        #Identify the depth
        currentLev=readLev(row)
        if currentLev>prevLev:
            direction='down'
            astroJson=astroJson+', "children": [{"name": "' + row[currentLev]+'"'
        elif currentLev<prevLev:
            direction='up'
            jump=prevLev-currentLev
            astroJson=astroJson+', "size": 1}'+']}'*jump+', {"name": "' + row[currentLev]+'"'
        elif currentLev==prevLev:
            direction='same'
            astroJson=astroJson+', "size": 1},{"name": "' + row[currentLev]+'"'
        #print direction
        prevLev=readLev(row)
    astroJson=astroJson+ '}]}]}'
    print astroJson

        
