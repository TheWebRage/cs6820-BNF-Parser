from production import Production 
from productions import createBnfProductions, createBnfHash
from parsingTable import createParsingTable

productions = createBnfProductions()
bnfHash = createBnfHash()

parsingTable = createParsingTable(productions, bnfHash)
