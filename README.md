# Các bước cài ứng dụng
##  Cài đặt Python
### Bước 1: Tải python từ trang https://www.python.org/ và tiến hành cài đặt 
### Bước 2: Chọn tùy chọn "add Python to Path" như hình
![installpy](https://user-images.githubusercontent.com/38754038/169266195-bf7fa41e-2c19-4cf4-bcc4-733f03882877.png)
### Bước 3: Kiểm tra python đã cài đặt trên máy hay chưa bằng cách vào terminal nhập lệnh
```
py
```
![image](https://user-images.githubusercontent.com/38754038/169266520-f8720c17-988e-4767-be5c-3a96bd830648.png)
### Nếu màn hình xuất hiện như hình thì đã thành công(có thể có vài thay đổi nhỏ tùy theo phiên bản Python-phiên bản mình cài là 3.10)
## Cài đặt Nodejs
### Bước 1: Tải Nodejs từ trang https://nodejs.org/en/ và tiến hành cài đặt 
![image](https://user-images.githubusercontent.com/38754038/169276731-d908c1d6-ce31-48fe-a8f9-cfc93656bc6d.png)

### Lưu ý: Nên cài toàn bộ các Feature
### Bước 2: Ở tùy chọn "add to Path" chọn Entired feature will be installed on local hard drive 
![image](https://user-images.githubusercontent.com/38754038/169280152-8e479670-dd7e-4c94-90f1-cbf63d432d33.png)
### Bước 3: Kiểm tra nodejs và python đã được thêm vào path hay chưa bằng cách vào tìm kiếm->Edit environment variables for your account->Path->Edit
![image](https://user-images.githubusercontent.com/38754038/169426693-80385cc1-7ad5-46cd-8253-f3e451032847.png)
### Nếu Path chứa Python và npm thì đã thành công
![image](https://user-images.githubusercontent.com/38754038/169426883-999668d6-5171-404b-8936-b5dc6f0fc59f.png)
## Cài đặt Visual Studio Code
### Bước 1: Tải Visual Studio Code từ https://code.visualstudio.com/ và tiến hành cài đặt 
![image](https://user-images.githubusercontent.com/38754038/169427343-19d2cc33-64cf-443e-ab6c-a366598222c6.png)
## 
![image](https://user-images.githubusercontent.com/38754038/169435343-a0f7f3eb-1cb5-4aa0-8055-27ddda4e72f6.png)
## Cài đặt các requirement 
### Bước 1: Mở ứng dụng Visual Studio Code
### Bước 2: Chọn File->Open Folder->Chọn đến vị trí bạn lưu. Sau khi mở bạn sẽ như trong hình dưới dây.
### Bước 3: Chọn terminal->new terminal
![image](https://user-images.githubusercontent.com/38754038/169443974-63c80f2b-e293-481b-ab2c-9c3f6afd1baa.png)
### Bước 4: chạy lệnh 'pip install -r requirements.txt' để cài đặt những thư viện cần thiết ( Yêu cầu phải có Visual C++ 2015-2019. các bạn có thể tìm tải tại đây:  https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170 )
```
pip install -r requirements.txt
```
![image](https://user-images.githubusercontent.com/38754038/169446274-e39bdfe9-6e16-4e5e-9821-9259ab96c339.png)
### Bước 5: Vào api->api->settings.py tìm phần **DATABASE** để chỉnh lại thông tin cơ sở dữ liệu
![image](https://user-images.githubusercontent.com/38754038/169447131-c96fb3ec-bd60-4cd6-904c-1c598134ea1d.png)
### Bước 6: Mở MySQL WorkBench đã cài. Nhấn chuột phải vào ** Local Instance MySQL80->Edit Connection->**
![image](https://user-images.githubusercontent.com/38754038/169447318-e8428b2b-5bef-4e43-aa5a-c22ed35de898.png)
### Bước 7: Chỉnh sửa các thông số như PORT và HOST (HOST 127.0.0.1 tương đương với localhost nên không cần chỉnh) trong **settings.py** giống với trong WorkBench và nhập mật khấu MySQL của bạn( mật khẩu đã tạo trong lúc cài đặt MySQL WorkBench)
![image](https://user-images.githubusercontent.com/38754038/169448076-8b0e1f76-73aa-4b89-a864-7026ed7629b5.png)
### Bước 8: Tắt phần Edit Connection ở WorkBench và nhấp vào Connection(Local Instance MySQL80) 
![image](https://user-images.githubusercontent.com/38754038/169448470-34ae8e04-aa34-4de6-83c8-3ba3170a35a1.png)
### Bước 9: Chọn qua tab **Schemas**
![image](https://user-images.githubusercontent.com/38754038/169448590-fbc0c8b7-7035-4e5a-adeb-362d038094ec.png)
### Bước 10: Nhấn chuột phải trên tab **schemas**->New Schema->đặt là django(hoặc bạn có thể đặt tùy thích và chỉnh **Name** trong settings.py)->Apply
![image](https://user-images.githubusercontent.com/38754038/169449036-ee9f24df-eb01-4fa4-9833-60029cfaa418.png)
### Bước 11: Mở terminal tại thư mục lưu trữ ứng dụng. Nhập các lệnh:
``` Cd api ```

``` py manage.py makemigrations ```

``` py manage.py migrate ``` 
![image](https://user-images.githubusercontent.com/38754038/170161136-13e3f98b-9069-4c5e-8901-8438254b0630.png)
### Bước 12: Tạo tài khoản admin.tại thư mục **TKVLTWCC\api** chạy lệnh:
``` py manage.py createsuperuser ```

```username:admin (có thể khác tùy )```

``` Email address: tùy ý ```

```Password: tùy ý ```
![image](https://user-images.githubusercontent.com/38754038/170183741-ea80de2b-19b2-4808-996e-6b1e6b84a7c2.png)

### **Lưu ý**: nếu gặp thông báo **Bypass password validation and create user anyway? [y/N]: y** 
### Bước 13: Sau khi cập nhật cơ sở dữ liệu vào MySQL. Bạn cần chạy các triggers,procedure,Functions. Trước tiên chọn làm mới trong workbench để thấy được các thay đổi trên CSDL.
![image](https://user-images.githubusercontent.com/38754038/170163431-8ffad9d0-34b6-4e22-8192-5fdd53ba4ce8.png)
###                       Trước khi làm mới
![image](https://user-images.githubusercontent.com/38754038/170163497-d1ea3b7e-66aa-4e00-87df-cb4f1c8501ec.png)
###                       Sau khi làm mới
### Bước 14: Trên thanh công cụ của MySQL WorkBench.Chọn **File->Open SQL Script-> trỏ đến django.sql tại thư mục lưu ứng dụng->Open**:
![image](https://user-images.githubusercontent.com/38754038/170163931-ea7dc062-97d9-4da4-b60a-1be270b94c38.png)
### Bước 15: Nhấn chuột phải lên schema django và chọn **Set as default Schema**. Chạy toàn bộ script trong file django.sql
![image](https://user-images.githubusercontent.com/38754038/170164386-1c18fa6e-cd86-4215-b92b-cf101c9df2b9.png)
### Bước 16: làm mới schema và kiểm tra xem toàn bộ script đã chạy chưa
![image](https://user-images.githubusercontent.com/38754038/170165050-d7c9f943-8ee2-486e-b422-432fcbfc6863.png)
### Bước 17: Bật terminal tại thư mục api và nhập 
``` py manage.py runserver ```
![image](https://user-images.githubusercontent.com/38754038/170165427-e834cd28-826b-4f20-8a21-a48928e4a6f6.png)
###                     Bạn có thể bật trình duyệt và nhập đường dẫn **http://127.0.0.1:8000/** để kiểm tra. nếu như hình dưới đây là đã thành công.
![image](https://user-images.githubusercontent.com/38754038/170166360-01077b64-e9df-48bb-b7d6-3b0529052bf9.png)
### Bước 18: Mở thêm 1 tab Terminal bằng lệnh ``` ctrl+shift+` ``` hoặc terminal->new terminal và mở đến thư mục **client**
``` cd client ```
### Bước 19: Cài đặt các dependencies bằng cách nhập lệnh:
``` npm install ```
![image](https://user-images.githubusercontent.com/38754038/170180683-a64f180c-e2a8-4e59-9833-92d4b70b07a0.png)
### *Lưu ý: trong trường hợp lỗi **The term 'npm' is not recognized** thì bạn khởi động lại máy(nếu vẫn lỗi thì kiểm tra trong **Edit the system environment variables->Environment variables->Path** xem đã có npm hay chưa)
### Bước 20: chạy bằng lệnh:
``` npm run dev ```
![image](https://user-images.githubusercontent.com/38754038/170183821-431c09bb-2a34-4c2a-8aa2-4b6d2d754846.png)
                              ### ctrl+nhấn vào đường dẫn hoặc gõ **http://localhost:3000/** bằng trình duyệt
                              ## Chúc Bạn thành công :D
                              
                                                                                                              
