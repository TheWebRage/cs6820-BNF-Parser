#include <iostream>

using std::string;

bool isWordBreak(char part) {
    if (part == ' ' || part == '+' || part == '-' || part == '*' || part == '/' || part == '^' || part == '(' || part == ')')
        return true;
    return false;
}

string NextWord(string line) {
    string returnString = "";

    for(int i = 0; i < line.size(); i++) {
        if (isWordBreak(line[i]))
            break;
        
        returnString += line[i];
    }

    return returnString;
}