# Bài 3. (Ứng dụng cấu trúc dữ liệu ánh xạ/từ điển)
# Cho danh sách các sản phẩm của 2 kho hàng A và B.
# Do chiến lược kinh doanh bạn được giao nhiệm vụ nhập các 
# sản phẩm từ kho B vào kho A sao cho những sản phẩm nào đã có trong kho A thì không nhập.
# Ví dụ: Với A = {"Banana", "Banana", "Apple“}, B = {"Orange", "Apple", "Banana", "Watermelon“},
# thì mergeProducts(A, B) = {Apple -> false, Banana -> false, Orange -> true, Watermelon -> true}.


def mergeProducts(A, B):
    # Chuyển danh sách sản phẩm A thành một từ điển, với sản phẩm là khóa và giá trị là True.
    products_in_A = {product: True for product in A}

    # Tạo một từ điển để lưu trữ kết quả cuối cùng với sản phẩm là khóa và
    # giá trị là True nếu sản phẩm chưa có trong kho A, ngược lại là False.
    result = {}

    # Duyệt qua danh sách sản phẩm trong kho B.
    for product in B:
        # Kiểm tra xem sản phẩm đã có trong kho A (tồn tại trong products_in_A) hay chưa.
        if product in products_in_A:
            result[product] = False
        else:
            result[product] = True

    return result

# Ví dụ sử dụng hàm mergeProducts:
A = {"Banana", "Banana", "Apple"}
B = {"Orange", "Apple", "Banana", "Watermelon"}
merged_result = mergeProducts(A, B)

# In ra kết quả với sản phẩm là khóa và True/False là giá trị tương ứng.
for product, is_new in merged_result.items():
    print(f"{product} -> {is_new}")
