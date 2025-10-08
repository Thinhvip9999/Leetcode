## 🧩 Ví dụ đầu vào

Giả sử ta có:

```
lists = [
  1 -> 4 -> 5,
  1 -> 3 -> 4,
  2 -> 6
]
```

Ta có 3 danh sách (k = 3).

---

## 🧠 Bước 1: Khởi tạo min-heap

Ta sẽ tạo **min-heap** chứa **phần tử đầu tiên** của mỗi danh sách:

| Danh sách | Node đầu | Giá trị |
| --------- | -------- | ------- |
| List 1    | 1        | 1       |
| List 2    | 1        | 1       |
| List 3    | 2        | 2       |

➡️ Heap sau khi khởi tạo:

```
[(1, 0, node(1 from list1)), (1, 1, node(1 from list2)), (2, 2, node(2 from list3))]
```

Heap tự động **duy trì phần tử nhỏ nhất ở đầu**.

---

## ⚙️ Bước 2: Bắt đầu vòng lặp

Chúng ta có một con trỏ `tail` trỏ vào `dummy` (danh sách kết quả rỗng ban đầu).

### 🔹 Lần 1:

* Pop phần tử nhỏ nhất từ heap → `(1, 0, node(1 from list1))`.
* Gắn node(1) vào danh sách kết quả.
* Node(1) này có `next = node(4)` → push vào heap `(4, 0, node(4 from list1))`.

Kết quả tạm thời:

```
Result: 1
Heap: [(1, 1, node(1 from list2)), (2, 2, node(2 from list3)), (4, 0, node(4 from list1))]
```

---

### 🔹 Lần 2:

* Pop nhỏ nhất → `(1, 1, node(1 from list2))`.
* Gắn node(1) này vào danh sách kết quả.
* Node(1) có `next = node(3)` → push `(3, 1, node(3 from list2))`.

```
Result: 1 -> 1
Heap: [(2, 2, node(2 from list3)), (4, 0, node(4 from list1)), (3, 1, node(3 from list2))]
```

---

### 🔹 Lần 3:

* Pop nhỏ nhất → `(2, 2, node(2 from list3))`.
* Gắn node(2) vào kết quả.
* Node(2) có `next = node(6)` → push `(6, 2, node(6 from list3))`.

```
Result: 1 -> 1 -> 2
Heap: [(3, 1, node(3 from list2)), (4, 0, node(4 from list1)), (6, 2, node(6 from list3))]
```

---

### 🔹 Lần 4:

* Pop nhỏ nhất → `(3, 1, node(3 from list2))`.
* Gắn node(3) vào kết quả.
* Node(3) có `next = node(4)` → push `(4, 1, node(4 from list2))`.

```
Result: 1 -> 1 -> 2 -> 3
Heap: [(4, 0, node(4 from list1)), (6, 2, node(6 from list3)), (4, 1, node(4 from list2))]
```

---

### 🔹 Lần 5:

* Pop nhỏ nhất → `(4, 0, node(4 from list1))`.
* Gắn node(4) vào kết quả.
* Node(4) có `next = node(5)` → push `(5, 0, node(5 from list1))`.

```
Result: 1 -> 1 -> 2 -> 3 -> 4
Heap: [(4, 1, node(4 from list2)), (6, 2, node(6 from list3)), (5, 0, node(5 from list1))]
```

---

### 🔹 Lần 6:

* Pop nhỏ nhất → `(4, 1, node(4 from list2))`.
* Gắn node(4) vào kết quả.
* Node(4) không có `next` → không push thêm gì.

```
Result: 1 -> 1 -> 2 -> 3 -> 4 -> 4
Heap: [(5, 0, node(5 from list1)), (6, 2, node(6 from list3))]
```

---

### 🔹 Lần 7:

* Pop nhỏ nhất → `(5, 0, node(5 from list1))`.
* Gắn node(5) vào kết quả.
* Node(5) không có `next`.

```
Result: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5
Heap: [(6, 2, node(6 from list3))]
```

---

### 🔹 Lần 8:

* Pop nhỏ nhất → `(6, 2, node(6 from list3))`.
* Gắn node(6) vào kết quả.
* Node(6) không có `next`.

```
Result: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
Heap: []
```

✅ Heap trống → dừng.

---

## 🏁 Kết quả cuối cùng

```
1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
```

---

## 🧩 Tổng kết lại cơ chế hoạt động

| Bước | Node được lấy | Thêm vào heap gì | Kết quả tạm     | Heap sau bước |
| ---- | ------------- | ---------------- | --------------- | ------------- |
| 1    | 1 (list1)     | 4                | 1               | [1,2,4]       |
| 2    | 1 (list2)     | 3                | 1→1             | [2,3,4]       |
| 3    | 2 (list3)     | 6                | 1→1→2           | [3,4,6]       |
| 4    | 3 (list2)     | 4                | 1→1→2→3         | [4,4,6]       |
| 5    | 4 (list1)     | 5                | 1→1→2→3→4       | [4,5,6]       |
| 6    | 4 (list2)     | –                | 1→1→2→3→4→4     | [5,6]         |
| 7    | 5 (list1)     | –                | 1→1→2→3→4→4→5   | [6]           |
| 8    | 6 (list3)     | –                | 1→1→2→3→4→4→5→6 | []            |
