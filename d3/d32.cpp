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

int main(int argc,char** argv){

    auto input = //ifstream(argv[argc-1]);
        ifstream("input.txt");

    string line;

    vector<string> allLines;

    while(getline(input, line)){
        allLines.push_back(line);
    }


    map<pair<int,int>, vector<int>> gears;

    for(int i = 0; i< allLines.size(); ++i){

        string number;
        for(int j = 0; j<= allLines[i].size(); ++j){
            if(j < allLines[i].size() && isdigit(allLines[i][j])){
                number.push_back(allLines[i][j]);
                continue;
            }

            if(number.empty()){
                continue;
            }

            int charBegin = j - number.size();
            int charEnd = j;


            int num = 0;
            auto res = std::from_chars(number.data(),number.data() + number.size(), num);
            for(int offset:{-1,1}){

                if(i+offset <0 || i+offset == allLines.size()){
                    continue;
                }

                for(int check = charBegin-1; check <= charEnd; ++check){
                    if(check <0 || check == allLines[i].size()){
                        continue;
                    }
                    if(allLines[i+offset][check] == '*'){
                        gears[{i+offset, check}].push_back(num);
                    }
                }
                
            }

            if( charBegin >0 && allLines[i][charBegin - 1] == '*'){
                gears[{i, charBegin - 1}].push_back(num);
            }

            if(charEnd != allLines[i].size() && allLines[i][charEnd] == '*'){
                gears[{i, charEnd}].push_back(num);
            }

            
            number.clear();
        }
    }

    uint64_t sum = 0;
    for(const auto &[k,v]: gears){
        if(v.size()!=2){
            continue;
        }
        sum += v[0]*v[1];
    }

    std::cout<<sum<<std::endl;
}
