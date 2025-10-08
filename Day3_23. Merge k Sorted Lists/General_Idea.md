## 🧩 1. Giải thích đề bài

Bạn được cho một **mảng `lists` gồm k danh sách liên kết (linked lists)**, mỗi danh sách **đã được sắp xếp tăng dần**.
Nhiệm vụ là **gộp tất cả các danh sách này lại thành một danh sách duy nhất**, cũng **được sắp xếp tăng dần**.

**Ví dụ:**

```
Input: [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

Giải thích:
Ba danh sách liên kết:

```
1 -> 4 -> 5
1 -> 3 -> 4
2 -> 6
```

Sau khi gộp:

```
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
```

---

## 💡 2. Ý tưởng ban đầu và vì sao nảy ra ý tưởng này

Ta nhận thấy rằng **vấn đề này tương tự việc trộn nhiều danh sách đã sắp xếp** (giống như trong merge sort).
Nếu chỉ có **hai danh sách**, ta có thể **dùng kỹ thuật trộn hai mảng đã sắp xếp (two-pointer)** để tạo ra danh sách kết quả trong **O(n)**.
Nhưng khi có **k danh sách**, ta cần chọn chiến lược trộn sao cho **hiệu quả hơn O(k·n)**.

Ý tưởng hợp lý là:

* Tại mọi thời điểm, **chỉ cần biết phần tử nhỏ nhất hiện tại trong tất cả các danh sách**.
* Khi ta chọn được phần tử nhỏ nhất, ta thêm nó vào kết quả, rồi **chuyển node tiếp theo trong danh sách đó vào hàng chờ**.

Điều này gợi ý đến việc dùng **cấu trúc dữ liệu “min-heap”** (hoặc priority queue):

* Heap luôn cho phép ta truy xuất phần tử nhỏ nhất trong **O(log k)**.
* Khi thêm node mới, cũng chỉ tốn **O(log k)**.

Tổng cộng, với N là tổng số phần tử của tất cả danh sách:

* **Thời gian chạy: O(N log k)** — tối ưu hơn nhiều so với gộp lần lượt từng danh sách.

---

## 🚫 3. Ý tưởng “nghe có vẻ đúng” nhưng thực ra có vấn đề

### ❌ Cách 1: Gộp tuần tự từng danh sách

Ví dụ:

* Gộp list1 và list2 → listA
* Sau đó gộp listA với list3 → listB
* Tiếp tục cho đến hết...

Tuy đúng về mặt logic, nhưng độ phức tạp:

```
O(n1 + n2) + O(n1+n2+n3) + ... ≈ O(k·N)
```

với `k` là số danh sách.
Nếu k lớn (ví dụ 10000), cách này sẽ **rất chậm**.

---

## ⚙️ 4. Giải pháp đúng và tối ưu: Dùng Min-Heap

Ta đưa **node đầu tiên của mỗi danh sách** vào **min-heap**.
Mỗi phần tử trong heap chứa `(giá trị, chỉ số danh sách, node)`.

Bước lặp:

1. Lấy phần tử nhỏ nhất ra khỏi heap.
2. Gắn node đó vào danh sách kết quả.
3. Nếu node vừa lấy có `next`, thêm node đó vào heap.

Cứ thế cho đến khi heap rỗng.

---

## 📊 5. Độ phức tạp

* **Thời gian:** `O(N log k)`
  (N = tổng số node trong tất cả danh sách)
* **Bộ nhớ:** `O(k)` cho heap
