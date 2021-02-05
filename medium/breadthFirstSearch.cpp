#include <iostream>
#include <stdexcept>
#include <vector>

class Node {
   public:
    std::string m_name;
    std::vector<Node *> m_children;

    Node(const std::string &name) : m_name{name} {};

    void addChild(Node *node);
    std::vector<std::string> breadthFirstSearch(
        std::vector<std::string> *nodes);
};

int main() {
    Node root{Node("A")};
    Node nodeB{Node("B")};
    Node nodeC{Node("C")};
    Node nodeD{Node("D")};
    Node nodeE{Node("E")};
    Node nodeF{Node("F")};
    Node nodeG{Node("G")};

    root.addChild(&nodeB);
    root.addChild(&nodeC);

    nodeB.addChild(&nodeD);
    nodeB.addChild(&nodeE);
    nodeB.addChild(&nodeF);

    nodeC.addChild(&nodeG);

    std::vector<std::string> visitedNodes{};
    root.breadthFirstSearch(&visitedNodes);

    for (const std::string &node : visitedNodes) {
        std::cout << node << " ";
    }
    std::cout << std::endl;

    return 0;
}

void Node::addChild(Node *node) { this->m_children.push_back(node); }

std::vector<std::string> Node::breadthFirstSearch(
    std::vector<std::string> *nodes) {
    if (!nodes->empty()) {
        throw std::invalid_argument("Non empty vector provided");
    }

    std::vector<Node *> to_visit{this};
    while (!to_visit.empty()) {
        nodes->push_back(to_visit[0]->m_name);
        for (Node *child : to_visit[0]->m_children) {
            to_visit.push_back(child);
        }
        to_visit.erase(to_visit.begin());
    }

    return *nodes;
}
