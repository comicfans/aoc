#include <charconv>
#include <iostream>
#include <cstdint>
#include <vector>
#include <cassert>
#include <string>
#include <fstream>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

bool issymbol(char c){
    return !isdigit(c) && (c!='.');
}

int main(int argc,char** argv){

    auto input = //ifstream(argv[argc-1]);
        ifstream("input.txt");

    string line;

    vector<string> allLines;

    while(getline(input, line)){
        allLines.push_back(line);
    }

    uint64_t sum = 0;

    for(int i = 0; i< allLines.size(); ++i){

        string number;
        for(int j = 0; j<= allLines[i].size(); ++j){
            if(j < allLines[i].size() && isdigit(allLines[i][j])){
                number.push_back(allLines[i][j]);
                continue;
            }

            int charBegin = j - number.size();
            int charEnd = j;

            bool adjSymbol = false;
            for(int offset:{-1,1}){

                if(i+offset <0 || i+offset == allLines.size()){
                    continue;
                }

                for(int check = charBegin-1; check <= charEnd; ++check){
                    if(check <0 || check == allLines[i].size()){
                        continue;
                    }
                    if(issymbol(allLines[i+offset][check])){
                        adjSymbol  = true;
                        break;
                    }
                }
                if(adjSymbol){
                    break;
                }
            }

            if(!adjSymbol && charBegin >0 && issymbol(allLines[i][charBegin - 1])){
                adjSymbol = true;
            }

            if(!adjSymbol && charEnd < allLines[i].size() && issymbol(allLines[i][charEnd])){
                adjSymbol = true;
            }

            

            if(number.empty() || !adjSymbol){
                number.clear();
                continue;
            }

            int num = 0;
            auto res = std::from_chars(number.data(),number.data() + number.size(), num);

            sum+=num;
            number.clear();
        }

    }
    std::cout<<sum<<std::endl;
}
