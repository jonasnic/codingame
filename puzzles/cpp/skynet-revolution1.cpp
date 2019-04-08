#include <iostream>
#include <vector>
#include <utility>

using namespace std;

void sever(pair<int, int>& link) {
  cout << link.first << ' ' << link.second << endl;
}

void block_first_link(vector<pair<int, int>>& links) {
  sever(links[0]);
  links.erase(links.begin());
}

void block(int agent_node, vector<int>& gateways, vector<pair<int, int>>& links) {
  for (auto gateway : gateways) {
    // Check for a direct link between the agent and a gateway
    for (unsigned i = 0; i < links.size(); i++) {
      pair<int, int>& link = links[i];
      if (link == make_pair(agent_node, gateway) || link == make_pair(gateway, agent_node)) {
        sever(link);
        links.erase(links.begin() + i);
        return;
      }
    }
  }

  block_first_link(links);
}

int main() {
  vector<pair<int, int>> links;
  vector<int> gateways;

  int nb_nodes;
  int nb_links;
  int nb_exits;
  cin >> nb_nodes >> nb_links >> nb_exits; cin.ignore();
  for (int i = 0; i < nb_links; i++) {
    int n1;
    int n2;
    cin >> n1 >> n2; cin.ignore();
    pair<int, int> link = make_pair(n1, n2);
    links.push_back(link);
  }

  for (int i = 0; i < nb_exits; i++) {
    int gateway; // the index of a gateway node
    cin >> gateway; cin.ignore();
    gateways.push_back(gateway);
  }

  // game loop
  while (true) {
    int agent_node; // The index of the node on which the Skynet agent is positioned this turn
    cin >> agent_node; cin.ignore();
    block(agent_node, gateways, links);
  }
}
