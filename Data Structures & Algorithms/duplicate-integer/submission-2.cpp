#include <map>
#include <vector>
using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, int> myMap;
        for (int num : nums) {
            if (myMap.find(num) != myMap.end()) {
                // Found a duplicate
                return true;
            }
            // Insert the number with a dummy value
            myMap.insert({num, 1});
        }
        return false; // No duplicates found
    }
};
