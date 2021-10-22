#include <iostream>
#include <fstream>
#include <string>

#include <scanner.cpp>

using std::string;

int main() {
    string fileIn = "./tests/pass.txt";

    // Read in file
    std::fstream file;
    file.open(fileIn);

    string line = "";
    while(std::getline(file, line)) {
        bool isPassing = false;

        // Goal -> Expr
        string word = NextWord(line);
        if (Expr()) {
            isPassing = true;
            
        }

    }


    return 0;
}