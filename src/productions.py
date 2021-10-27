from production import Production 


def createBnfProductions():
    productions = []

    # Whitespace
    productions.append(Production().AddProduction('\s'))

    # Digit
    productions.append(Production().AddProduction('0'))
    productions.append(Production().AddProduction('1'))
    productions.append(Production().AddProduction('2'))
    productions.append(Production().AddProduction('3'))
    productions.append(Production().AddProduction('4'))
    productions.append(Production().AddProduction('5'))
    productions.append(Production().AddProduction('6'))
    productions.append(Production().AddProduction('7'))
    productions.append(Production().AddProduction('8'))
    productions.append(Production().AddProduction('9'))

    # Number
    productions.append(Production().AddProduction('DIGIT', 'BETA'))

    # Beta
    productions.append(Production().AddProduction('NUMBER'))
    productions.append(Production().AddProduction('EMPTY'))

    # Negative Number
    productions.append(Production().AddProduction('-', 'NUMBER'))

    # Pos or Neg
    productions.append(Production().AddProduction('NUMBER'))
    productions.append(Production().AddProduction('NEGATIVE NUMBER'))

    # Exp
    productions.append(Production().AddProduction('LI', 'AE'))

    # Ae # TODO: separate the parts for oder of operations
    productions.append(Production().AddProduction('+', 'RI', 'AE'))
    productions.append(Production().AddProduction('-', 'RI', 'AE'))
    productions.append(Production().AddProduction('/', 'RI', 'AE'))
    productions.append(Production().AddProduction('*', 'RI', 'AE'))
    productions.append(Production().AddProduction('^', 'RI', 'AE'))
    productions.append(Production().AddProduction('EMPTY'))

    # Li
    productions.append(Production().AddProduction('OP'))
    productions.append(Production().AddProduction('PAREN'))

    # RI
    productions.append(Production().AddProduction('(', 'EXP', ')'))

    # Op
    productions.append(Production().AddProduction('POS OR NEG'))
    productions.append(Production().AddProduction('VARIABLE NAME', 'REF'))

    return productions

def createBnfHash():
    bnfHash = {}

    bnfHash['WHITESPACE'] = [0]
    bnfHash['DIGIT'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bnfHash['NUMBER'] = [11]
    bnfHash['BETA'] = [12, 13]
    bnfHash['NEGATIVE NUMBER'] = [14]
    bnfHash['POS OR NEG'] = [15, 16]
    bnfHash['EXP'] = [17]
    bnfHash['AE'] = [18, 19, 20, 21, 22, 23]
    bnfHash['LI'] = [24, 25]
    bnfHash['RI'] = [26, 27]
    bnfHash['PAREN'] = [28]
    bnfHash['OP'] = [29, 30]

    return bnfHash