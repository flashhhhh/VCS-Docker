# VCS-Docker

## Khái niệm
Docker là một nền tảng để phát triển, đóng gói và chạy ứng dụng. Docker cho phép tách ứng dụng ra khỏi hạ tầng, chạy ứng dụng trên một môi trường cô lập gọi là **container**.

Có thể chạy nhiều container trên cùng một máy và các container này không chia sẻ bất kỳ dữ liệu nào cho nhau. Container nhẹ hơn rất nhiều so với máy ảo, và chứa toàn bộ tất cả thư viện cần thiết để chạy ứng dụng.

## Kiến trúc của Docker
Docker sử dụng kiến trúc client-server. Docker client nói chuyện với Docker daemon (chịu trách nhiệm xây dựng, chạy và phân phối các container. Docker client và daemon có thể chạy trên cùng 1 máy, hoặc có thể kết nối Docker client đến 1 daemon từ xa, kết nối thông qua REST API.

### Docker daemon
Docker deamon (dockerd) lắng nghe các Docker API requests, đồng thời quản lý Docker images, containers, networks, và volumes. Một daemon có thể kết nối với các daemons khác để quản lý Docker.

### Docker client
Docker client là cách cơ bản nhất để người dùng giao tiếp với Docker. Khi gõ lệnh như **docker run**, client sẽ gửi lệnh đó tới **dockerd** để xử lý. Docker client có thể kết nối với nhiều daemon khác nhau.

### Docker registries
Docker registry lưu trữ các Docker image. Docker Hub là registry công khai mà ai cũng có thể tải image về để chạy.

### Image
Image là chỉ dẫn để tạo ra 1 docker container. Thông thường, một image sẽ dựa trên các image có sẵn khác với một vài sửa đổi.

### Container
Container là một thực thể chạy của image. Nó bao gồm tất cả các thành phần cần thiết để chạy ứng dụng, bao gồm mã nguồn, thư viện, và các biến môi trường. Container được tạo ra từ image và có thể được khởi động, dừng, và xóa một cách độc lập.

### Volume
Volume là một phần lưu trữ dữ liệu bên ngoài container. Volume được sử dụng để lưu trữ dữ liệu mà cần giữ lại khi container bị xóa hoặc tái tạo. Volume có thể được chia sẻ giữa các container khác nhau.

### Network
Network là một phần của Docker cho phép các container giao tiếp với nhau. Mỗi container có thể được kết nối đến một hoặc nhiều network, và có thể giao tiếp với các container khác trong cùng một network.

### Docker Compose
Docker Compose là một công cụ để định nghĩa và chạy các ứng dụng Docker đa container. Với Docker Compose, bạn có thể sử dụng một file YAML để cấu hình các dịch vụ, mạng, và volume cần thiết cho ứng dụng của mình. Sau đó, bạn có thể sử dụng lệnh `docker-compose up` để khởi động tất cả các dịch vụ trong một lần.

## Xây dựng Image