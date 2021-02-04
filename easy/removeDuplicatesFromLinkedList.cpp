#include <iostream>
#include <vector>

class List {
   public:
    int m_value;
    List *m_next;

    List(int value, List *next = nullptr) : m_value{value}, m_next{next} {};

    void fill(std::vector<int> values);
    void freeListButHead();
    void print();
};

List *removeDuplicatesFromLinkedList(List *head);

int main() {
    std::vector<int> values{7, 7, 7, 13, 13, 14};
    List listHead{List(5)};

    listHead.fill(values);
    listHead.print();
    List *head{&listHead};
    head = removeDuplicatesFromLinkedList(head);
    listHead.print();
    listHead.freeListButHead();

    return 0;
}

void List::fill(std::vector<int> values) {
    List *current{this};
    for (const int &number : values) {
        current->m_next = new List(number);
        current = current->m_next;
    }
}

void List::freeListButHead() {
    while (this->m_next) {
        List *tmp = this->m_next;
        this->m_next = tmp->m_next;
        delete tmp;
    }
}

void List::print() {
    List *temp{this};

    if (temp == nullptr) {
        return;
    }

    while (temp->m_next != nullptr) {
        std::cout << temp->m_value << "->";
        temp = temp->m_next;
    }
    std::cout << temp->m_value << std::endl;
}

List *removeDuplicatesFromLinkedList(List *head) {
    List *prev{head};
    List *current{nullptr};
    while (prev != nullptr) {
        current = prev->m_next;
        while ((current != nullptr) && (prev->m_value == current->m_value)) {
            List *temp{current};
            current = current->m_next;
            delete temp;
            prev->m_next = current;
        }
        prev = prev->m_next;
    }

    return head;
}
