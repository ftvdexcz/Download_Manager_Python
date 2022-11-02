BÁO CÁO BÀI TẬP LỚN MÔN LẬP TRÌNH MẠNG

HỌC KỲ I NĂM HỌC 2022 - 2023

> Nhóm: 4 - 11

1.  Giới thiệu sơ lược chủ đề

> \* Nhóm em xin phép được đổi chủ đề từ lập trình socket cờ caro (Java)
> sang download manager (Python)

a.  Mục tiêu

    -   Tải file định dạng bất kì

    -   Tải video youtube (1 video hoặc playlist), chọn chất lượng
        > download video

    -   Tải hình ảnh từ instagram

    -   Tải xuống thông qua http (sử dụng thư viện urllib.request,
        > requests)

    -   Hỗ trợ tải song song đa luồng

    -   Tạm dừng, tiếp tục tải

    -   Xây dựng thành ứng dụng có giao diện (sử dụng PyQt5)

b.  Kết quả đã đạt được \[Điền vào buổi báo cáo cuối cùng\]

c.  Hạn chế, hướng phát triển \[Điền vào buổi báo cáo cuối cùng\]

```{=html}
<!-- -->
```
2.  Tổng hợp công việc

+------+--------------+--------------+--------------+--------------+
| STT  | MASV - Họ    | Các nội dung | Thể hiện     | Ghi chú      |
|      | tên          | thực hiện    |              |              |
+======+==============+==============+==============+==============+
| 1.   | B19DCCN386   | -   \[14/10  | -   Index.py | \+ Video     |
|      | -- Đặng Quốc |     > --     |              | chưa có âm   |
|      | Long         |              | \- Thư mục   | thanh        |
|      |              |   > 19/10\]: | downloader   |              |
|      |              |              |              | \+ Code đang |
|      |              | > \+ Tải     | \-           | gộp chung    |
|      |              | > video,     | PauseHandl   | vào 1 file   |
|      |              | > playlist   | erWorkers.py | index.py     |
|      |              | > youtube    |              |              |
|      |              | > (thư viện  |              | \+ Đã thay   |
|      |              | > pafy,      |              | phần         |
|      |              | >            |              | progress bar |
|      |              |  youtube-dl) |              | khi download |
|      |              | >            |              | thành log    |
|      |              | > \+ Xử lý   |              |              |
|      |              | > thanh tiến |              |              |
|      |              | > trình      |              |              |
|      |              | > download   |              |              |
|      |              | > video và   |              |              |
|      |              | > chọn vị    |              |              |
|      |              | > trí lưu    |              |              |
|      |              | > video      |              |              |
|      |              |              |              |              |
|      |              | -   \[26/10  |              |              |
|      |              |     > --     |              |              |
|      |              |              |              |              |
|      |              |    > 3/11\]: |              |              |
|      |              |              |              |              |
|      |              | > \+ Đa      |              |              |
|      |              | > Luồng cho  |              |              |
|      |              | > download   |              |              |
|      |              | > file       |              |              |
|      |              | > (download  |              |              |
|      |              | > đa luồng   |              |              |
|      |              | > nhiều phần |              |              |
|      |              | > của file), |              |              |
|      |              | > xử lý      |              |              |
|      |              | > download   |              |              |
|      |              | > lại khi có |              |              |
|      |              | > lỗi        |              |              |
|      |              | >            |              |              |
|      |              | > \+ Cấu     |              |              |
|      |              | > trúc lại   |              |              |
|      |              | > code       |              |              |
|      |              | >            |              |              |
|      |              | > \+ Chuyển  |              |              |
|      |              | > file       |              |              |
|      |              | > pause.py   |              |              |
|      |              | > thành      |              |              |
|      |              | > PauseHandl |              |              |
|      |              | erWorkers.py |              |              |
+------+--------------+--------------+--------------+--------------+
| 2.   | B16DCCN054 - | -   \[14/10  | -   Index.py | \+ 1 số định |
|      | Nguyễn Tuấn  |     > --     |              | dạng bị lỗi  |
|      | Đăng         |              | \-           |              |
|      |              |   > 19/10\]: | downloa      |              |
|      |              |              | der/pause.py |              |
|      |              | > \+ Tải     |              |              |
|      |              | > file hỗ    |              |              |
|      |              | > trợ nhiều  |              |              |
|      |              | > định dạng  |              |              |
|      |              | >            |              |              |
|      |              | > \+ Xử lý   |              |              |
|      |              | > thanh tiến |              |              |
|      |              | > trình      |              |              |
|      |              | > download,  |              |              |
|      |              | > chọn đường |              |              |
|      |              | > dẫn lưu    |              |              |
|      |              | > file       |              |              |
|      |              |              |              |              |
|      |              | -   \[26/10  |              |              |
|      |              |     > --     |              |              |
|      |              |              |              |              |
|      |              |    > 3/11\]: |              |              |
|      |              |              |              |              |
|      |              | > \+ Cài đặt |              |              |
|      |              | > demo tiếp  |              |              |
|      |              | > tục / tạm  |              |              |
|      |              | > dừng tải   |              |              |
+------+--------------+--------------+--------------+--------------+
| 3.   | B19DCCN352 - | -   \[14/10  | -   ui.py    |              |
|      | Vũ Bá Kiệt   |     > --     |              |              |
|      |              |              | \-           |              |
|      |              |   > 19/10\]: | Clipboa      |              |
|      |              |              | rdWorkers.py |              |
|      |              | > \+ Tạo     |              |              |
|      |              | > giao diện  |              |              |
|      |              | > và xử lý   |              |              |
|      |              | > các nút    |              |              |
|      |              | > bấm,       |              |              |
|      |              | > animation  |              |              |
|      |              |              |              |              |
|      |              | -   \[26/10  |              |              |
|      |              |     > --     |              |              |
|      |              |              |              |              |
|      |              |    > 3/11\]: |              |              |
|      |              |              |              |              |
|      |              | -   Bắt link |              |              |
|      |              |     > từ     |              |              |
|      |              |              |              |              |
|      |              |  > clipboard |              |              |
|      |              |     > dán    |              |              |
|      |              |     > vào    |              |              |
|      |              |     > url    |              |              |
|      |              |     > trên   |              |              |
|      |              |     > giao   |              |              |
|      |              |     > diện   |              |              |
+------+--------------+--------------+--------------+--------------+

3.  Quá trình phát triển

+------+----------+----------+----------+----------+----------+
| STT  | Phiên    | Vấn đề   | Xử lý    | Tự đánh  | Người    |
|      | bản      |          |          | giá      | thực     |
|      |          |          |          |          | hiện     |
+======+==========+==========+==========+==========+==========+
| 1.   | *1.0     | *- Chưa  |          | *- Ổn*   | *Đặng    |
|      | 18/10*   | hỗ trợ   |          |          | Quốc     |
|      |          | đa luồng |          |          | Long*    |
|      |          | và tải   |          |          |          |
|      |          | ảnh từ   |          |          |          |
|      |          | in       |          |          |          |
|      |          | stagram* |          |          |          |
|      |          |          |          |          |          |
|      |          | *- Với   |          |          |          |
|      |          | playlist |          |          |          |
|      |          | youtube  |          |          |          |
|      |          | chưa     |          |          |          |
|      |          | chọn     |          |          |          |
|      |          | được     |          |          |          |
|      |          | chất     |          |          |          |
|      |          | lượng    |          |          |          |
|      |          | tải*     |          |          |          |
+------+----------+----------+----------+----------+----------+
| 2.   | *1.1     | *- Vấn   | \+ Tạm   | *- Cơ    |          |
|      | 3/11*    | đề tiếp  | dừng /   | bản các  |          |
|      |          | tục/tạm  | tiếp tục | chức     |          |
|      |          | dừng     | tải:     | năng*    |          |
|      |          | tải*     | chưa cài |          |          |
|      |          |          | đặt được |          |          |
|      |          |          | với      |          |          |
|      |          |          | trường   |          |          |
|      |          |          | hợp tạo  |          |          |
|      |          |          | nút bấm  |          |          |
|      |          |          | trên     |          |          |
|      |          |          | giao     |          |          |
|      |          |          | diện mà  |          |          |
|      |          |          | đang sử  |          |          |
|      |          |          | dụng bắt |          |          |
|      |          |          | sự kiện  |          |          |
|      |          |          | nhấn     |          |          |
|      |          |          | phím 'p' |          |          |
|      |          |          | thay cho |          |          |
|      |          |          | việc ấn  |          |          |
|      |          |          | nút trên |          |          |
|      |          |          | giao     |          |          |
|      |          |          | diện     |          |          |
+------+----------+----------+----------+----------+----------+
| 3.   |          |          |          |          |          |
+------+----------+----------+----------+----------+----------+

4.  Mã nguồn: https://github.com/ftvdexcz/Download_Manager_Python.git

