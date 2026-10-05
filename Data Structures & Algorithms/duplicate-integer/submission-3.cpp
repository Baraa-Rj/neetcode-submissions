#include <set>
#include <vector>
using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set< int> myMap;
        for (int num : nums) {
            if (!myMap.insert(num).second) {
                // Found a duplicate
                return true;
            }
            // Insert the number with a dummy value
            myMap.insert(num);
        }
        return false; // No duplicates found
    }
};
