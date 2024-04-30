#include <charconv>
#include <iostream>
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

int main(){

    auto input = ifstream("input.txt");

    string line;

    vector<string> allLines;

    while(getline(input, line)){
        allLines.push_back(line);
    }

    uint64_t sum = 0;

    for(int i = 0; i< allLines.size(); ++i){

        string number;
        bool adjSymbol = false;
        for(int j = 0; j<= allLines[i].size(); ++j){
            if(j < allLines[i].size() && isdigit(allLines[i][j])){
                number.push_back(allLines[i][j]);

                if(i>0 && issymbol(allLines[i-1][j])){
                    adjSymbol = true;
                }

                if(!adjSymbol && i < (int)allLines.size()-1 && issymbol(allLines[i+1][j])){
                    adjSymbol = true;
                }

                continue;
            }

            if(number.empty() || !adjSymbol){
                number.clear();
                continue;
            }

            int num = 0;
            auto res = std::from_chars(number.data(),number.data() + number.size(), num);

            sum+=num;
        }

        std::cout<<sum<<std::endl;
    }
}
