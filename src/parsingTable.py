from constants import terminals, nonTerminals

def first(productions):
    firstTable = {}

    for terminal in terminals:
        firstTable[terminal] = terminal

    for nonTerminal in nonTerminals:
        firstTable[nonTerminal] = None

    stillChanging = True
    rhs = ""
    while stillChanging:
        for production in productions:
            rhs = firstTable[production[0]].remove('EMPTY')
            
            i = 1
            k = len(production)
            while 'EMPTY' in firstTable[production[i]] and i <= k-1:
                rhs = rhs if rhs != None else firstTable[production[i+1]].remove('EMPTY')
                i += 1

            if i == k and 'EMPTY' in firstTable[production[k]]:
                rhs = rhs if rhs != None else 'EMPTY'
    
    return firstTable

def follow(productions, firstTable):
    followTable = {}

    for nonTerminal in nonTerminals:
        followTable[nonTerminal] = None

    followTable['S'] = 'EOF' # TODO: change the 'S' to be useful
    isChanging = True
    while isChanging:
        for production in productions:
            trailer = followTable[production]

            for i in range (0, len(followTable)):
                if production.production[i] in nonTerminals:
                    followTable[production.production[i]] = followTable[production.production[i]] if followTable[production.production[i]] != None else trailer

                    if 'EMPTY' in firstTable[production.production[i]]:
                        trailer = trailer if trailer != None else firstTable[production.production[i]].remove('EMPTY')
                    else:
                        trailer = firstTable[production.production[i]]
                
                else:
                    trailer = firstTable[production.production[i]]

    return followTable

def firstP(firstTable, followTable):
    firstPTable = {}

    for item in firstTable:
        pass # TODO: complete this table

    return firstPTable

def createParsingTable(productions, bnfHash):
    firstTable = first(productions, bnfHash) # TODO: make sure all of these tables are being created correctly
    followTable = follow(productions, firstTable)
    firstPTable = firstP(firstTable, followTable)

    parsingTable = [['ERROR'] * len(nonTerminals)] * len(terminals) # TODO: make sure this is a 2d array initialized to 'ERROR'

    for nonTerminal in nonTerminals:
        for production in productions:
            for terminal in terminals:
                parsingTable[nonTerminal][terminal] = production

            if 'EOF' in firstPTable[nonTerminal]:
                parsingTable[nonTerminal]['EOF'] = production

    return parsingTable
