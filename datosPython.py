tuplex = ( 'Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado' )
tupleMonth = ( 'January', 'February', 'March', 'April' )
siglosTuple = tuple()

def addTuplasPython( dato, item ):
    ##dato.append( item )
    print( " Para las tuplas no se pueden adicionar elementos... For tuplex can't adition elements...\n" )

def viewTupla( Tupla ):
    index = 0

    while index < len( Tupla ):
        print( Tupla[ index ] )
        index = index + 1
    print("\n\n")

def featuresData( data, nameTuple ):
    print (" Tuplex name: ", nameTuple)
    print ( type( data ) )
    print ( len( data ) )
    viewTupla( data )

def viewTupleToFor( Tupla ):
    print (" Tuple printing with 'For'... ")

    for tupleItem in Tupla:
        print ( tupleItem )
        
    print("\n\n")
        
def printingQuarter( Tupla, QuarterBegin, QuarterFinish ):
    tuplaEnd = Tupla[QuarterBegin:QuarterFinish];
    print( tuplaEnd )

featuresData( tuplex, "Tuplex" )
featuresData( siglosTuple, "siglosTuple")

addTuplasPython( tupleMonth, 'June' )


featuresData( tupleMonth, "tupleMonth")
print ("\n\n")
viewTupleToFor( tuplex )
printingQuarter( tuplex, 2, 5 )

name = "Erik Dario Hernandez Vasquez"

print ( name[4:20] )