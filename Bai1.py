# Bài 1. Cài đặt cấu trúc dữ liệu hàng đợi ưu tiên (sử dụng cấu trúc đống).
# Thử nghiệm chèn lần lượt vào hàng đợi các giá trị 8, 3, 9, 1, 7, 5, 6, 4 dùng thao tác Push();
# sau đó hiển thị các phần tử đó lên màn hình và rút tất cả các phần tử ra khỏi hàng đợi dùng thao tác pop().


class PriorityQueue:
    def __init__(self):
        self.queue = []                             # Khởi tạo một danh sách để lưu trữ các phần tử trong hàng đợi ưu tiên.

    def push(self, value):
        self.queue.append(value)                    # Thêm giá trị vào danh sách.
        self._heapify_up(len(self.queue) - 1)       # Gọi phương thức _heapify_up để cân bằng lại cây đống.

    def pop(self):
        if not self.is_empty():                     # Kiểm tra xem hàng đợi có rỗng hay không.
            if len(self.queue) == 1:
                return self.queue.pop()
            root = self.queue[0]                    # Lấy ra phần tử gốc của cây đống (phần tử nhỏ nhất).
            self.queue[0] = self.queue.pop()        # Gán phần tử cuối cùng của danh sách lên vị trí gốc.
            self._heapify_down(0)                   # Gọi phương thức _heapify_down để cân bằng lại cây đống.
            return root
        else:
            print("Hàng đợi ưu tiên đã rỗng.")

    def is_empty(self):
        return len(self.queue) == 0                 # Kiểm tra xem hàng đợi có rỗng hay không.

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2         # Tìm vị trí của nút cha. (// python = % C++)
            if self.queue[index] < self.queue[parent_index]:
                self.queue[index], self.queue[parent_index] = self.queue[parent_index], self.queue[index]
                                                    # Hoán đổi phần tử con với phần tử cha nếu điều kiện thứ tự đống bị vi phạm.
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1        # Tìm vị trí của nút con bên trái.
            right_child_index = 2 * index + 2       # Tìm vị trí của nút con bên phải.
            smallest = index                        # Gán vị trí của nút hiện tại là vị trí nhỏ nhất.

            if (left_child_index < len(self.queue) and
                self.queue[left_child_index] < self.queue[smallest]):
                smallest = left_child_index
            # So sánh với nút con bên trái và cập nhật vị trí nhỏ nhất nếu cần.

            if (right_child_index < len(self.queue) and
                self.queue[right_child_index] < self.queue[smallest]):
                smallest = right_child_index
            # So sánh với nút con bên phải và cập nhật vị trí nhỏ nhất nếu cần.

            if smallest != index:
                self.queue[index], self.queue[smallest] = self.queue[smallest], self.queue[index]
                # Hoán đổi phần tử hiện tại với phần tử nhỏ nhất nếu điều kiện thứ tự đống bị vi phạm.
                index = smallest
            else:
                break

priority_queue = PriorityQueue()

values_to_insert = [8, 3, 9, 1, 7, 5, 6, 4]
for value in values_to_insert:
    priority_queue.push(value)

print("Các phần tử trên hàng đợi ưu tiên:")
while not priority_queue.is_empty():
    item = priority_queue.pop()
    print(item,end=" ")