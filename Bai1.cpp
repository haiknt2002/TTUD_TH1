#include <iostream>
#include <vector>
#include<windows.h>

using namespace std;

class PriorityQueue {
private:
    vector<int> heap;  // Một mảng lưu trữ các phần tử trong cấu trúc đống

    // Hàm giúp điều chỉnh đống khi một phần tử được thêm vào
    void heapifyUp(int index) {
        while (index > 0) {
            int parentIndex = (index - 1) / 2;
            if (heap[index] > heap[parentIndex]) {  // So sánh giá trị của phần tử với cha
                swap(heap[index], heap[parentIndex]);  // Hoán đổi nếu cần
                index = parentIndex;
            } else {
                break;
            }
        }
    }

    // Hàm giúp điều chỉnh đống khi một phần tử bị loại bỏ
    void heapifyDown(int index) {   
        int leftChild = 2 * index + 1;
        int rightChild = 2 * index + 2;
        int largest = index;

        // Tìm ra phần tử lớn nhất giữa cha và hai con
        if (leftChild < heap.size() && heap[leftChild] > heap[largest]) {
            largest = leftChild;
        }
        if (rightChild < heap.size() && heap[rightChild] > heap[largest]) {
            largest = rightChild;
        }

        // Nếu cha không lớn nhất, hoán đổi và tiếp tục điều chỉnh đống
        if (largest != index) {
            swap(heap[index], heap[largest]);
            heapifyDown(largest);
        }
    }

public:
    // Thêm một phần tử vào hàng đợi ưu tiên
    void push(int value) {
        heap.push_back(value);  // Thêm vào cuối mảng
        heapifyUp(heap.size() - 1);  // Điều chỉnh để đảm bảo tính ưu tiên
    }

    // Trả về giá trị có độ ưu tiên cao nhất (đầu hàng đợi)
    int top() {
        if (!empty()) {
            return heap[0];
        }
        throw std::out_of_range("PriorityQueue is empty");
    }

    // Loại bỏ phần tử có độ ưu tiên cao nhất
    void pop() {
        if (!empty()) {
            heap[0] = heap.back();  // Thay thế phần tử đầu bằng phần tử cuối
            heap.pop_back();  // Loại bỏ phần tử cuối
            heapifyDown(0);  // Điều chỉnh để tái thiết lại đống
        }
    }

    // Kiểm tra xem hàng đợi ưu tiên có trống hay không
    bool empty() const {
        return heap.empty();
    }
};

int main() {

    PriorityQueue priorityQueue;

    // Chèn các giá trị vào hàng đợi
    priorityQueue.push(8);
    priorityQueue.push(3);
    priorityQueue.push(9);
    priorityQueue.push(1);
    priorityQueue.push(7);
    priorityQueue.push(5);
    priorityQueue.push(6);
    priorityQueue.push(4);

    //hiển thị dấu trong console
    SetConsoleOutputCP(65001);

    // Hiển thị các phần tử trong hàng đợi
    cout << "Các phần tử trong hàng đợi ưu tiên: ";
    while (!priorityQueue.empty()) {
        cout << priorityQueue.top() << " ";
        priorityQueue.pop();
    }
    
    cout << endl;

    return 0;
}
