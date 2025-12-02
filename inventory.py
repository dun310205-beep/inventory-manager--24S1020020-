# Danh sách toàn cục lưu trữ sản phẩm
products = []

def main():
    while True:
        print("\n===== MENU QUẢN LÝ KHO HÀNG =====")
        print("1. Thêm sản phẩm")
        print("2. Hiển thị danh sách sản phẩm")
        print("3. Cập nhật thông tin sản phẩm")
        print("4. Xóa sản phẩm")
        print("5. Tìm kiếm sản phẩm")
        print("0. Thoát chương trình")
        
        choice = input(">> Nhập lựa chọn của bạn: ")

        if choice == "1":
            print(">>> Chức năng thêm sản phẩm")
        elif choice == "2":
            print(">>> Chức năng hiển thị danh sách sản phẩm")
        elif choice == "3":
            print(">>> Chức năng cập nhật sản phẩm")
        elif choice == "4":
            print(">>> Chức năng xóa sản phẩm")
        elif choice == "5":
            print(">>> Chức năng tìm kiếm sản phẩm")
        elif choice == "0":
            print(">>> Thoát chương trình. Tạm biệt!")
            break
        else:
            print("!!! Lựa chọn không hợp lệ, vui lòng thử lại.")

# Gọi hàm main để chạy chương trình
main()
