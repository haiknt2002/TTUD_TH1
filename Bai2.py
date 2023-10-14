# Bài 2. (Ứng dụng cấu trúc dữ liệu tập hợp)
# Một vector v được gọi là vector beautiful nếu một số trong v chỉ xuất hiện đúng một lần.
# Cần xác định xem phải xóa ít nhất bao nhiêu phần tử trong v để v trở thành vector beautiful.

def minDeletionsToMakeBeautiful(vector):
    # Khởi tạo một từ điển để lưu trữ số lần xuất hiện của mỗi phần tử và một biến để đếm số lượng phần tử cần xóa.
    counts = {}
    deletions = 0

    # Duyệt qua từng phần tử trong vector.
    for number in vector:
        # Kiểm tra nếu phần tử đã xuất hiện trong từ điển counts (đã xuất hiện trước đó).
        if number in counts:
            # Nếu đã xuất hiện trước đó, tăng biến deletions lên 1 và đánh dấu rằng phải xóa một phần tử để biến vector thành beautiful.
            deletions += 1
        else:
            # Nếu phần tử chưa từng xuất hiện trước đó, thì đánh dấu nó trong từ điển counts.
            counts[number] = 1

    # Trả về giá trị của biến deletions, tức là số lượng phần tử cần xóa để biến vector thành beautiful.
    return deletions


vector = [3, 4, 2, 2, 6, 6, 3, 7, 8]
deletions_needed = minDeletionsToMakeBeautiful(vector)
print(f"Phải xóa ít nhất {deletions_needed} phần tử để biến vector thành beautiful.")


