#include <cassert>
#include <fstream>
#include <iostream>
#include <regex>
#include <stdint.h>

int main() {
  std::ifstream f("input.txt");
  std::string line;
  std::regex reg("mul\\(([0-9]{1,3}),([0-9]{1,3})\\)|do\\(\\)|don't\\(\\)");

  uint64_t res = 0;
  auto enable = true;
  while (std::getline(f, line)) {

    std::smatch sm;

    std::sregex_iterator it(line.begin(), line.end(), reg);
    for (auto end = std::sregex_iterator(); it != end; ++it) {

      if (it->str().find("mul") != std::string::npos) {

        if (enable) {
          int this_res = std::stoi((*it)[1]) * std::stoi((*it)[2]);
          res += this_res;
        }
        continue;
      }

      if (it->str() == "do()") {
        enable = true;
        continue;
      }
      if (it->str() == "don't()") {
        enable = false;
        continue;
      }

      assert(false);
    }
  }
  std::cout << res << std::endl;
}
