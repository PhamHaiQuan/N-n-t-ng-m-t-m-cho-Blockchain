# Thư viện dùng để tạo Hash (chuỗi mổ xẻ)
import hashlib as hasher
# Thư viện lấy thời gian thực
import datetime as date


class Block:
    # def: Khi tạo hàm bắt buộc có
    # __init__ : Hàm khởi tạo (Constructor), được gọi tự động khi tạo
    #            đối tượng. Dùng để khởi tạo giá trị ban đầu cho các 
    #            thuộc tính của đối tượng ban đầu
    # (self, index, timestamp, data, previous_hash): Tham số
    #            
    # self         : Đại diện cho chính đối tượng hiện tại.
    # index        : STT
    # timestamp    : Thời gian tạo
    # data         : Dữ liệu
    # previous_hash: Hash của Block trước
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        # Gọi hàm để tính Hash rồi lưu vào hash
        self.hash = self.hash_block()

    # Hàm tính Hash (Chuỗi mổ xẻ)
    def hash_block(self):
        # Tạo đối tượng SHA-256.
        sha = hasher.sha256()

        # Ghép dữ liệu trong block thành 1 chuỗi
        text = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
        )

        # Chuyển chuỗi thành bytes rồi đưa vào SHA-256.
        sha.update(text.encode("utf-8"))
        # Tính và trả về Hash dưới dạng chuỗi Hex (thập lục phân)
        return sha.hexdigest()


# Tạo Block 0
def create_genesis_block():
    return Block(
        0,
        date.datetime.now(),
        "Block 0",
        "0"
    )


# Tạo block tiếp theo
def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    # Lấy Hash của Block trước để liên kết các Block với nhau.
    this_hash = last_block.hash

    return Block(
        this_index,
        this_timestamp,
        this_data,
        this_hash
    )


# Khởi tạo Blockchain
blockchain = [create_genesis_block()]
# Gắn Block 0 làm Block trước
previous_block = blockchain[0]

# Số block cần tạo thêm
num_of_blocks_to_add = 20

# Thêm block vào Blockchain
# Lặp lại "num_of_blocks_to_add" lần
for i in range(num_of_blocks_to_add):
    # Tạo block mới dựa trên block trước đso
    block_to_add = next_block(previous_block)
    # Thêm block mới vào Blockchain
    blockchain.append(block_to_add)
    # Cập nhật block mới thành block trước
    previous_block = block_to_add
    # In nội dung block mới 
    print("Block #{} has been added to the blockchain!".format(block_to_add.index))
    # In Hash của block mới
    print("Hash: {}\n".format(block_to_add.hash))