#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int main() {
  int nbPlaces, nbRides, nbGroups;
  cin >> nbPlaces >> nbRides >> nbGroups; cin.ignore();
  vector<long> groups;
  for (int i = 0; i < nbGroups; i++) {
    long nbPeople;
    cin >> nbPeople; cin.ignore();
    groups.push_back(nbPeople);
  }

  // Calculate earnings starting from each group (1 ride)
  // Save the result (dynamic programming)
  vector<pair<long, int>> results;
  for (int i = 0; i < nbGroups; i++) {
    int index = i;
    long nbPeople = groups[index];
    long nbPeopleRiding = 0;
    while (nbPeopleRiding + nbPeople <= nbPlaces) {
      nbPeopleRiding += nbPeople;
      if (index < nbGroups - 1) {
        index++;
      } else {
        index = 0;
      }
      // all groups are riding already?
      if (index == i) {
        break;
      }
      nbPeople = groups[index];
    }
    results.push_back(make_pair(nbPeopleRiding, index));
  }

  // Calculate the total earnings starting from the first group (all rides)
  long totalMoney = 0;
  int currentGroup = 0;
  for (int i = 0; i < nbRides; i++) {
    totalMoney += results[currentGroup].first;
    currentGroup = results[currentGroup].second;
  }
  cout << totalMoney << endl;
}
