## Ví dụ dài

Sử dụng:

s = "mississippi"

p = "c*mis*is*ip*."

| Bước | `(i, j)` | `s[i:]`       | `p[j:]`         | Trường hợp trong code  | Hành động                          | Lý do/giải thích                                                                |
| ---: | :------: | ------------- | --------------- | ---------------------- | ---------------------------------- | ------------------------------------------------------------------------------- |
|    1 |  (0, 0)  | `mississippi` | `c*mis*is*ip*.` | Có `*` sau `p[0]='c'`  | **Bỏ qua `c*`** → `(0, 2)`         | `first_match` với `'c'` là **False** (vì `s[0]='m'`), nên chỉ còn nhánh bỏ qua. |
|    2 |  (0, 2)  | `mississippi` | `mis*is*ip*.`   | Không có `*` sau `'m'` | `(1, 3)`                           | `first_match` True (`'m'=='m'`), tiến cả hai.                                   |
|    3 |  (1, 3)  | `ississippi`  | `is*is*ip*.`    | Không có `*` sau `'i'` | `(2, 4)`                           | `first_match` True (`'i'=='i'`).                                                |
|    4 |  (2, 4)  | `ssissippi`   | `s*is*ip*.`     | Có `*` sau `'s'`       | Nhánh **dùng ≥1 lần** → `(3, 4)`   | `first_match` True (`'s'=='s'`), ăn 1 ký tự `s`, giữ `j`.                       |
|    5 |  (3, 4)  | `sissippi`    | `s*is*ip*.`     | Vẫn ở `s*`             | Nhánh **dùng ≥1 lần** → `(4, 4)`   | Còn `'s'` nữa, tiếp tục ăn.                                                     |
|    6 |  (4, 4)  | `issippi`     | `s*is*ip*.`     | Vẫn ở `s*`             | **Bỏ qua `s*`** → `(4, 6)`         | Giờ `s[4]='i'` không còn `'s'`, `first_match` False nên chỉ bỏ qua `s*`.        |
|    7 |  (4, 6)  | `issippi`     | `is*ip*.`       | Không có `*` sau `'i'` | `(5, 7)`                           | `first_match` True (`'i'=='i'`).                                                |
|    8 |  (5, 7)  | `ssippi`      | `s*ip*.`        | Có `*` sau `'s'`       | Nhánh **dùng ≥1 lần** → `(6, 7)`   | `first_match` True (`'s'=='s'`).                                                |
|    9 |  (6, 7)  | `sippi`       | `s*ip*.`        | `s*` tiếp              | Nhánh **dùng ≥1 lần** → `(7, 7)`   | Ăn nốt chữ `'s'` thứ hai.                                                       |
|   10 |  (7, 7)  | `ippi`        | `s*ip*.`        | `s*`                   | **Bỏ qua `s*`** → `(7, 9)`         | `s[7]='i'` ≠ `'s'`, không ăn nữa.                                               |
|   11 |  (7, 9)  | `ippi`        | `ip*.`          | Không có `*` sau `'i'` | `(8, 10)`                          | `first_match` True (`'i'=='i'`).                                                |
|   12 |  (8, 10) | `ppi`         | `p*.`           | Có `*` sau `'p'`       | Nhánh **dùng ≥1 lần** → `(9, 10)`  | `first_match` True (`'p'=='p'`).                                                |
|   13 |  (9, 10) | `pi`          | `p*.`           | `p*` tiếp              | Nhánh **dùng ≥1 lần** → `(10, 10)` | Còn `'p'` thứ hai, ăn tiếp.                                                     |
|   14 | (10, 10) | `i`           | `p*.`           | `p*` tiếp              | **Bỏ qua `p*`** → `(10, 12)`       | `s[10]='i'` ≠ `'p'`, dừng ăn `p`.                                               |
|   15 | (10, 12) | `i`           | `.`             | Không có `*` sau `'.'` | `(11, 13)`                         | `.` khớp **bất kỳ 1 ký tự** → khớp `'i'`.                                       |
|   16 | (11, 13) | `` (rỗng)     | `` (rỗng)       | **Mẫu hết**            | Trả `i == len(s)` → **True**       | Cả `s` và `p` đều hết → khớp toàn bộ.                                           |
