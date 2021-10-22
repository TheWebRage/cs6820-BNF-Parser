#include <iostream>

using std::string;

bool isWordBreak(char part) {
    return (part == '+' || part == '-' || part == '*' || part == '/' || part == '^' || part == '(' || part == ')');
}

string NextWord(string& line) {
    string returnString = "";

    int endPos = 0;
    for(endPos; endPos < line.size(); endPos++) { // TODO: if last check was isWordBreak, need to make that it's own word
        if (isWordBreak(line[endPos]))
            break;
        else if (line[endPos] == ' ')
            continue;
        
        returnString += line[endPos];
    }

    line = line.erase(0, endPos)
    return returnString;
}