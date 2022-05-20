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
