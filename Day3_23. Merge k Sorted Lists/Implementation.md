# Giải thích cho triển khai `mergeKLists` (min-heap)

```python
from typing import List, Optional
import heapq
```

* Import **kiểu chú thích** `List`, `Optional` để code dễ đọc và IDE hỗ trợ lint/type.
* Import **`heapq`** để dùng **min-heap (priority queue)** — luôn lấy phần tử nhỏ nhất trong `O(log k)`.

```python
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
```

* Khai báo cấu trúc **node** của danh sách liên kết đơn (LeetCode đã cho sẵn).
* Mỗi node có `val` (giá trị) và `next` (trỏ sang node kế tiếp).

```python
class Solution:
    def mergeKLists(self, lists: List[Optional['ListNode']]) -> Optional['ListNode']:
```

* Hàm cần cài đặt.
* `lists`: mảng gồm `k` **head** của các danh sách liên kết **đã sắp xếp tăng dần**.
* Trả về **head** của danh sách kết quả (cũng tăng dần).
* Mục tiêu: **gộp k danh sách** về **1 danh sách** với độ phức tạp tối ưu **O(N log k)** (N = tổng số node).

```python
        heap = []
```

* Khởi tạo **min-heap rỗng**.
* Ta sẽ lưu trong heap các **ứng viên nhỏ nhất hiện tại** từ mỗi danh sách.

```python
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
```

* Duyệt qua **k danh sách**:

  * `i`: **chỉ số** của danh sách (0..k-1).
  * `node`: head của danh sách đó.
* Bỏ qua danh sách rỗng.
* **Push** vào heap **bộ 3** `(node.val, i, node)`:

  * `node.val`: **khóa so sánh chính** trong heap (giá trị nhỏ nhất ưu tiên).
  * `i`: **tie-breaker** khi hai `val` bằng nhau (tránh Python phải so sánh trực tiếp `ListNode` → sẽ `TypeError`).
  * `node`: **con trỏ thật** tới node để ta nối vào kết quả và truy cập `node.next` ở bước sau.

```python
        dummy = ListNode(0)
        tail = dummy
```

* Tạo **dummy head** để đơn giản hóa thao tác nối (không cần xử lý riêng case “node đầu tiên”).
* `tail` luôn trỏ tới **cuối** danh sách kết quả (giúp nối trong `O(1)`).

```python
        while heap:
```

* Vòng lặp chính: tiếp tục cho tới khi heap rỗng (tức **mọi node** đã được lấy ra theo thứ tự tăng dần).

```python
            _, i, node = heapq.heappop(heap)
```

* **Lấy** phần tử có **giá trị nhỏ nhất** hiện tại khỏi heap.
* Bóc tách tuple; không cần dùng lại `node.val` nên gán `_`.

```python
            tail.next = node
            tail = tail.next
```

* **Nối** `node` nhỏ nhất vừa lấy vào **đuôi** của danh sách kết quả.
* **Cập nhật** `tail` sang node vừa nối (để lần sau nối tiếp ngay sau nó).

```python
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
```

* Nếu node vừa gắn có **phần tử kế tiếp**, đẩy **`node.next`** vào heap:

  * Duy trì bất biến: “**Mỗi danh sách** (nếu còn phần tử) **đóng góp đúng 1 ứng viên** vào heap.”
  * Nhờ vậy, heap luôn so sánh **k (tối đa)** đầu danh sách còn lại → mỗi lần lấy nhỏ nhất là **đúng**.

```python
        tail.next = None
```

* Cắt **liên kết thừa** (an toàn khi tái sử dụng node có sẵn từ input).
* Đảm bảo danh sách kết quả **kết thúc đúng chỗ**.

```python
        return dummy.next
```

* Bỏ qua `dummy`, trả về **head thực** của danh sách đã gộp.

---

## Tại sao viết như thế?

* **Min-heap** cho phép luôn rút ra **node nhỏ nhất hiện tại** trong `O(log k)`.
  Mỗi node **vào** và **ra** heap đúng **1 lần** ⇒ tổng thời gian **O(N log k)**.
* Lưu `(val, i, node)` thay vì `(val, node)` để:

  * Tránh lỗi so sánh `ListNode` khi `val` bằng nhau.
  * Vẫn giữ được **con trỏ node** để nối và sinh `node.next`.
* **Dummy head + tail**:

  * Giảm nhánh rẽ (không cần “nếu là node đầu tiên thì…”).
  * Nối đuôi trong `O(1)`.

---

## Độ phức tạp

* **Thời gian:** `O(N log k)` — `N` node, mỗi thao tác heap `log k`.
* **Không gian phụ:** `O(k)` — heap chứa tối đa 1 node “đầu” từ mỗi danh sách.


