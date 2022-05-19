<template>
  <div>
    <Header :brands="brands"></Header>
    <BannerTop />
    <div class="section pd-top-20 section-gioithieu">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-10">
            <h5 class="text-center">GIỚI THIỆU Ý TƯỞNG THIẾT KẾ WEB</h5>
            <p>
              &emsp; Hiện nay, với sự phát triển bùng nổ của công nghệ thông
              tin, Internet ngày càng đóng vai trò quan trọng trong nền công
              nghiệp 4.0. Mạng Internet đã thật sự tạo nên một cuộc cách mạng
              trao đổi thông tin trong mọi lĩnh vực văn hóa, xã hội, kinh tế,
              chính trị....
            </p>
            <p>
              &emsp;Trong bối cảnh dịch bệnh covid-19 đã và đang tác động trực
              tiếp tới hoạt động sản xuất, kinh doanh của nhiều tổ chức, cá
              nhân. Trong đó, các doanh nghiệp, nhất là các cửa hàng kinh doanh
              truyền thống chịu ảnh hưởng không nhỏ. Những biến động, khó khăn
              hiện nay bắt buộc các đơn vị phải thực hiện chuyển đổi hoặc đa
              dạng hóa hình thức kinh doanh. Trong đó, hình thức kinh doanh
              online chính là xu hướng để duy trì hoạt động và tạo cơ hội “trở
              mình” cho nhiều đơn vị.
            </p>
            <p>
              &emsp;Trong xu thế toàn cầu hóa nền kinh tế trên thế giới, nhu cầu
              tìm kiếm thông tin, giải trí của con người dần được đáp ứng, đặc
              biệt là nhu cầu về trao đổi hàng hóa và mua bán. Đáp ứng nhu cầu
              đó là sự ra đời của hàng loạt website cho mục đích thương mại,
              giải trí, tin tức và website bán hàng online là nhu cầu mang tính
              thiết yếu.
            </p>
            <p>
              &emsp;Với lý do đó thì việc có một website để quảng bá sản phẩm
              của công ty không còn là điều gì xa xỉ nữa và các đơn vị kinh
              doanh laptop cũng không nằm ngoài số đó. Thông qua website doanh
              nghiệp có thể quảng bá thương hiệu và bán hàng 1 cách nhanh chóng
              và hiệu quả.
            </p>
            <p>
              &emsp;Trong thời đại 4.0 hiện nay, chúng ta không thể không nhắc
              tới máy tính đây là một thiết bị công nghệ cao nó có tầm ảnh hưởng
              rất lớn tới con người từ học tập, lao động cho đến giải trí. Vì
              vậy nó đã trở thành người bạn đồng hành không thể thiếu trong thời
              đại công nghiệp hóa ngày nay. Trên thế giới nói chung và ở Việt
              Nam nói riêng đã xuất hiện nhiều công ty, doanh nghiệp, cửa hàng
              chuyên bán máy tính. Để đáp ứng nhu cầu đẩy mạnh phát triển thông
              qua nền thương mại điện tử, "website bán laptop trực tuyến” được
              ra đời.
            </p>
            <p>
              &emsp;Website được xây dựng dựa trên nhu cầu của khách hàng trên
              thị trường. Mang đến cho khách hàng các thông tin đầy đủ về các
              sản phẩm laptop. Qua đó khách hàng có thể đồng ý mua hàng, hệ
              thống sẽ thống báo cho khách hàng biết đã mua thành công. Và công
              ty sẽ giao hàng đến địa chỉ mà khách hàng đã cung cấp.
            </p>
          </div>
        </div>
      </div>
    </div>
    <Top-footer />
    <Footer />
  </div>
</template>
<script>
export default {
  auth: false,
  async asyncData({ $axios }) {
    const brands = await $axios.$get('/brand/')
    return {  brands }
  },
  methods: {
    
    filterproducts(searchinput){
      if (searchinput === '') {
        return "/products"
      }
      else {
        return"/products/filter/"+ searchinput
      }
    }
  },
}
</script>