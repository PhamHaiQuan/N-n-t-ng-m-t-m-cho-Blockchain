# Thư viện sử dụng thuật toán mổ xẻ SHA-256
import hashlib


# ============================
# Hàm mổ xẻ SHA-256
# data.encode('utf-8') : Chuyển chuỗi (str) thành dữ liệu dạng bytes 
# hexdigest()          : Chuyển giá trị Hash sang chuỗi Hex (Thập lục phân)
# hashlib.sha256()     : Mổ xẻ dữ liệu bằng SHA-256
# ============================
def sha256(data):
    # Dùng thuật toán mổ xẻ SHA-256 để tạo Hash.
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


# ============================
# Tính Merkle Root (Hash gốc)
# ============================
def merkle_root(transactions):
    # Nếu danh sách giao dịch rỗng thì không thể tạo Merkle Root
    # len() : Hàm đếm số phần tử
    if len(transactions) == 0:
        return None

    # Băm từng giao dịch (tx) trong danh sách transactions để tạo Leaf Hash 
    # (Hash của từng giao dịch)
    current_level = [sha256(tx) for tx in transactions]

    # Hiển thị các Leaf Hash (Hash của từng giao dịch)
    print("=== Lá (Leaf Hashes) ===")
    # Hiển thị từng Leaf Hash
    # enumerate(): Hàm để lấy số thứ  i và giá trị h của từng phần tử trong danh sách
    for i, h in enumerate(current_level):
        print(f"Giao dịch {i+1}: {h}")
    # Khởi tạo cấp (Level) đầu tiên của cây Merkle
    level = 1

    # Lặp đến khi còn 1 hash
    while len(current_level) > 1:
        # Hiển thị cấp (Level) hiện tại của cây Merkle
        print(f"\n=== Cấp {level} ===")

        # Nếu số lượng hash lẻ thì nhân đôi hash cuối để tất cả Hash đều có cặp
        if len(current_level) % 2 != 0:
            current_level.append(current_level[-1])

        # Danh sách lưu các Hash của cấp tiếp theo
        next_level = []

        # Ghép từng cặp Hash để tạo Hash mới
        # range(): Hàm tạo dãy số để điều khiển vòng lặp
        # 0, len(current_level), 2: bắt đầu, kết thúc, bước nhảy
        for i in range(0, len(current_level), 2):
            # Ghép 2 hash liền nhau thành 1 chuỗi
            combined = current_level[i] + current_level[i + 1]
            # Mổ xẻ chuỗi vừa ghép để tạo Hash mới
            new_hash = sha256(combined)

            # Quá trình tạo Hash
            print(f"Hash {i//2 + 1}:")
            print(f"  {current_level[i]}")
            print(f"+ {current_level[i+1]}")
            print(f"= {new_hash}\n")

            # Thêm Hash mới vào cấp tiếp theo
            next_level.append(new_hash)

        # Chuyển sang cấp tiếp theo của cây Merkle
        current_level = next_level
        level += 1  

    # Trả về Merkle Root (Hash gốc)
    return current_level[0]


# ============================
# Chương trình chính
# ============================

# Danh sách giao dịch
transactions = [
    "A gui 5 BTC cho B",
    "B gui 2 BTC cho C",
    "C gui 1 BTC cho D",
    "D gui 4 BTC cho E",
    "E gui 3 BTC cho F"
]

print("===== DANH SÁCH GIAO DỊCH =====")

# Hiển thị từng giao dịch trong danh sách
# enumerate(): Lấy số thứ tự (i) và nội dung giao dịch (tx), bắt đầu từ 1
for i, tx in enumerate(transactions, 1):
    print(f"{i}. {tx}")

# Tính Merkle Root từ danh sách giao dịch và lưu vào biến root
root = merkle_root(transactions)

# Hiển thị Merkle Root
print("======================================")
print("MERKLE ROOT:")
print(root)