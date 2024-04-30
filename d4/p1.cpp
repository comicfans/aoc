#include <charconv>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <string_view>
#include <cassert>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

vector<int> parseVec(std::string_view view){
    string num;
    vector<int> ret;
    for(int i = 0; i <= view.size(); ++i){
        if(i!= view.size() && isdigit(view[i])){
            num.push_back(view[i]);
            continue;
        }

        if(num.empty()){
            continue;
        }

        int number;
        auto cvt_res = from_chars(num.data(),num.data()+num.size(), number);
        num.clear();
        ret.push_back(number);
    }
    return ret;
}

pair<vector<int>,vector<int>> parseLine(const std::string& line){
    auto split1 = line.find(':');
    auto split2 = line.find('|', split1);

    string_view view(line);
    vector<int> win = parseVec(view.substr(split1,split2-split1));
    sort(win.begin(),win.end());

    vector<int> card = parseVec(view.substr(split2));
    sort(card.begin(),card.end());

    return {win,card};

}

int countMatch(const vector<int>& s1, const std::vector<int>& s2){

    int res = 0;

    for(int i = 0,j=0; i< s1.size() && j < s2.size(); ){

        if(s1[i] == s2[j]){
            ++res;
            ++i;
            ++j;
            continue;
        }

        if(s1[i] < s2[j]){
            ++i;
            continue;
        }

        ++j;
    }

    return res;

}

int main1(){

    auto input = //ifstream(argv[argc-1]);
        ifstream("input.txt");

    string line;
    uint64_t res = 0;
    while(getline(input, line)){

        auto p = parseLine(line);

        auto m = countMatch(p.first,p.second);
        if(m>0){
            res += (1<<(m-1));
        }
    }

    std::cout<<res<<std::endl;
    return 0;
}

int main(){

    auto input = //ifstream(argv[argc-1]);
        ifstream("input.txt");

    string line;
    uint64_t res = 0;

    vector<pair<int,int>> upto;

    int lineCount = 0;
    for(;getline(input, line); ++lineCount){

        auto p = parseLine(line);


        auto pos = lower_bound(upto.begin(),upto.end(), pair<int,int>{lineCount,lineCount},[](const auto& lhs, const auto& rhs){
            return lhs.first < rhs.first;
        });
        upto.erase(upto.begin(), pos);

        auto m = countMatch(p.first,p.second);
        

        int thisAdd = 1;
        for(auto kv: upto){
            thisAdd += kv.second;
        }

        res += thisAdd;


        int toEnd = m + lineCount;
        auto insPos = lower_bound(upto.begin(), upto.end(), pair<int,int>{toEnd,toEnd},[](const auto& lhs, const auto& rhs){
            return lhs.first < rhs.first;
        });

        if(insPos == upto.end() || (insPos->first !=  toEnd)){
            upto.insert(insPos, {toEnd,thisAdd});
        }else{
            insPos->second+= thisAdd;
        }
    }

    std::cout<<res<<std::endl;
}
