# Thư viện tạo khóa RSA và thực hiện ký/xác minh chữ ký số
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Thư viện sử dụng thuật toán mổ xẻ SHA-256
from cryptography.hazmat.primitives import hashes

# ============================
# 1. Tạo cặp khóa RSA
# ============================

# Tạo khóa bí mật (Private Key)
private_key = rsa.generate_private_key(
    # Số mũ chuẩn dùng trong RSA (thường dùng chuẩn là 65537)
    public_exponent=65537,

    # Độ dài khóa RSA (2048 bit)
    # Khóa càng dài càng an toàn nhưng xử lý chậm hơn
    key_size=2048
)

# Tạo khóa công khai (Public Key) từ khóa bí mật
public_key = private_key.public_key()

# ============================
# 2. Thông điệp cần ký
# ============================

# Tạo thông điệp "Hello Blockchain" cần ký.
# Chữ 'b' trước chuỗi cho biết dữ liệu được lưu dưới dạng bytes.
message = b"Hello Blockchain"

# ============================
# 3. Ký thông điệp:
# Bước 1: Nhận thông điệp (message).
# Bước 2: Băm thông điệp bằng SHA-256.
# Bước 3: Áp dụng thuật toán đệm PSS.
# Bước 4 Dùng Private Key tạo chữ ký số.
# Bước 5: Hiển thị chữ ký dưới dạng Hex.
# ============================

# Gọi hàm sign() để tạo chữ ký số bằng Private Key
signature = private_key.sign(

    # Dữ liệu cần ký (dạng bytes): "Hello Blockchain"
    message,

    # Thuật toán đệm (Padding) PSS - Tăng tính bảo mật khi ký RSA
    padding.PSS(

        # Sử dụng MGF1 kết hợp thuật toán mổ xẻ SHA-256
        mgf=padding.MGF1(hashes.SHA256()),

        # Tự tạo Salt ngẫu nhiên với độ dài tối đa để tăng độ bảo mật
        salt_length=padding.PSS.MAX_LENGTH
    ),

    # Sử dụng thuật toán mổ xẻ SHA-256 để ký
    hashes.SHA256()
)

# Thông báo ký thành công
print("Đã ký thông điệp thành công!")

# (5) Hiển thị chữ ký dưới dạng Hex (thập lục phân)
print("Chữ ký (hex):")
print(signature.hex())

# ============================
# 4. Xác minh chữ ký:
# Bước 1. Nhận chữ ký (signature).
# Bước 2. Nhận thông điệp (message).
# Bước 3. Băm thông điệp bằng SHA-256.
# Bước 4. Áp dụng thuật toán đệm PSS.
# Bước 5. Dùng Public Key để kiểm tra chữ ký.
# Bước 6. Nếu đúng → Chữ ký hợp lệ.
#         Nếu sai → Phát sinh Exception.
# ============================

try:
    # Dùng Public Key để kiểm tra chữ ký
    public_key.verify(

        # Chữ ký cần xác minh
        signature,

        # Thông điệp gốc cần kiểm tra
        message,

            # Thuật toán đệm (Padding) PSS - Tăng tính bảo mật khi ký RSA
            padding.PSS(
        
                # Sử dụng MGF1 kết hợp thuật toán mổ xẻ SHA-256
                mgf=padding.MGF1(hashes.SHA256()),
        
                # Tự tạo Salt ngẫu nhiên với độ dài tối đa để tăng độ bảo mật
                salt_length=padding.PSS.MAX_LENGTH
            ),

        # Sử dụng thuật toán mổ xẻ SHA-256 để xác minh chữ kí
        hashes.SHA256()
    )

    # Nếu không xảy ra ngoại lệ (Exception) thì chữ ký hợp lệ
    print("\nChữ ký hợp lệ.")

except:
    # Nếu xảy ra lỗi (chữ ký sai hoặc thông điệp đã bị sửa)
    print("\nChữ ký KHÔNG hợp lệ.")
