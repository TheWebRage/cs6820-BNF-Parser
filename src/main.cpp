#include <iostream>
#include <fstream>
#include <string>

#include <scanner.cpp>
#include <productionTable.cpp>
#include <productions.cpp>

using std::string;

int main() {
    string fileIn = "../tests/pass.txt";


    // Read in file
    std::fstream file;
    file.open(fileIn);


    // Production Table takes care of creating and using the table used for parsing
    ProductionTable pTable = new ProductionTable();


    string line = "";
    while(std::getline(file, line)) {
        bool isPassing = false;
        
        string word = NextWord(line);
        

        // Goal -> Expr
        if (Expr()) {
            isPassing = true;
            
        }

        // Expr -> ExprP
        // ExprP -> Term

        // Term -> TermP
        // TermP -> Factor

        // Factor -> FactorP
        // FactorP -> Expo

        // Expo -> ExpoP
        // ExpoP -> End

        // End -> num
        // End -> var

    }


    return 0;
}