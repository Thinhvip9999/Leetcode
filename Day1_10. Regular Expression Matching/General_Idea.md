# Regular Expression Matching — General Idea, Sai lầm thường gặp, và Hướng giải đúng

## Mục tiêu bài toán (tóm lược)

Ta cần kiểm tra xem **toàn bộ** chuỗi `s` có khớp mẫu `p` hay không, với chỉ hai phép đặc biệt:

* `.` khớp **đúng 1** ký tự bất kỳ.
* `*` áp dụng cho **ký tự ngay trước nó** (có thể là chữ hoặc `.`), nghĩa là lặp lại ký tự đó **0, 1 hoặc nhiều lần**.

> Nhấn mạnh: phải khớp **hết** `s`, không được khớp một phần.

---

## Sai lầm phổ biến: “Tham lam” (`greedy`) với `*`

Nhiều bạn chọn cách “ăn càng nhiều càng tốt” khi gặp `*`. Điều này *trực giác có vẻ đúng* nhưng **thường sai** khi phía sau còn ràng buộc. Ví dụ:

* `s = "aabcb"`, `p = "a.*b"`
  Nếu `.*` “ăn hết” đến cuối chuỗi thì sẽ **không** còn `b` để khớp ký tự cuối của mẫu. Đúng ra `.*` phải **dừng ở “bc”** để chữ `b` cuối của mẫu khớp chữ `b` cuối của `s`.

* `s = "ab"`, `p = ".*c"`
  `.*` có thể ăn hết “ab”, nhưng sau đó còn phải khớp `c` — không có → **false**. Tham lam dễ bỏ qua bước **quay lui**.

**Bản chất vấn đề:** `*` tạo ra **nhánh chọn** (0 lần, 1 lần, nhiều lần). Một chiến lược đơn điệu (tham lam hoặc “ăn ít nhất có thể”) **không đảm bảo đúng**, vì chọn sai ở sớm sẽ khóa hỏng ràng buộc phía sau.

---

## Hướng giải đúng: Quy hoạch động/Đệ quy có nhớ (Top-down DP)

### Trực giác

Ta nên mô hình hóa việc khớp từ một vị trí `(i, j)` trong `s` và `p`. Quyết định tại đây (dùng hay bỏ qua `*`, hoặc khớp 1 ký tự thường) sẽ dẫn đến các **trạng thái con**. Vì số trạng thái hữu hạn (≤ `len(s) * len(p)`), dùng **memo** để tránh lặp.

### Định nghĩa trạng thái

`match(i, j)` = `True` nếu và chỉ nếu `s[i:]` khớp hoàn toàn `p[j:]`.

### Điều kiện dừng

* Nếu `j == len(p)` (mẫu đã hết) ⇒ khớp khi **và chỉ khi** `i == len(s)`.

### So khớp ký tự đầu (first_match)

```text
first_match = (i < len(s)) and (p[j] == s[i] or p[j] == '.')
```

### Chuyển trạng thái

1. **Nếu** `j + 1 < len(p)` **và** `p[j+1] == '*'` (khối `x*`):

   * **Bỏ qua `x*`** (dùng 0 lần): `match(i, j+2)`
   * **Dùng `x*` ≥ 1 lần** (chỉ nếu `first_match`): `match(i+1, j)`
     (tiêu thụ 1 ký tự từ `s`, vẫn giữ `j` vì `*` còn hiệu lực)
   * Kết quả: **OR** của hai nhánh trên.

2. **Ngược lại** (không có `*` sau `p[j]`):

   * Phải có `first_match` **và** tiến cả hai: `match(i+1, j+1)`.

### Tại sao hướng này “đúng hơn” so với greedy?

* Nó **xem xét đầy đủ** mọi khả năng do `*` tạo ra (0/1/nhiều) và nhờ **memo** nên **không trùng lặp**.
* Bất kỳ lựa chọn tham lam nào cũng chỉ là **một đường trong không gian khả năng**; DP đảm bảo không bỏ sót đường đúng.
* Với giới hạn `|s|, |p| ≤ 20`, độ phức tạp `O(n*m)` là quá ổn.

---

## Phác thảo tính đúng đắn (Sketch)

* **Cơ sở:** Khi `j` đến cuối mẫu, điều kiện `i == len(s)` là cần & đủ để khớp toàn bộ.
* **Bước quy nạp:**

  * Nếu sau `p[j]` là `*`, mọi cách lặp của ký tự trước `*` đều được bao phủ bởi hai nhánh: dùng 0 lần (bước tới `j+2`) **hoặc** dùng ≥1 lần (tiêu thụ 1 ký tự ở `s`, giữ `j`).
  * Nếu không có `*`, điều kiện khớp 1 ký tự (`first_match`) rồi tiến đồng bộ bảo toàn quy tắc “khớp toàn bộ”.
* **Memo** đảm bảo mỗi `(i, j)` được đánh giá một lần, tránh vòng lặp do các nhánh quay lui.

---

## Độ phức tạp

* **Thời gian:** `O(n * m)` — mỗi cặp `(i, j)` được tính đúng 1 lần.
* **Không gian:** `O(n * m)` cho bộ nhớ đệ quy + cache.

---

## Các tình huống méo mó dễ sai

* `a*` có thể là **chuỗi rỗng**: mẫu `"c*a*b"` khớp `"aab"` bằng cách **tắt `c*`**, dùng `a*` ăn `"aa"`, rồi `b`.
* `.` luôn chỉ khớp **1 ký tự**; nếu muốn tùy ý độ dài dùng `.*`.
* Bắt buộc khớp **toàn bộ** `s`: `"ab"` với `"."` → false (thiếu 1 ký tự).
* Nhiều cụm `*` liên tiếp vẫn hoạt động nhờ cấu trúc nhánh (ví dụ `"a*b*c*"` phải thử các cách tắt/bật từng cụm).

---

## TL;DR

* **Sai lầm:** xử lý `*` theo kiểu tham lam một chiều.
* **Đúng đắn & gọn:** mô hình hóa `match(i, j)` và dùng **hai nhánh** cho `x*` (bỏ qua hoặc dùng ≥1 lần), cộng với **memo**.
* **Đảm bảo:** bao phủ mọi khả năng, đúng với ràng buộc “khớp toàn bộ”, chạy nhanh trong giới hạn bài.
