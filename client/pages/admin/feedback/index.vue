<template>
  <div>
    <Header-admin></Header-admin>
    <div class="section bg-color-brown">
      <div class="container-fluid">
        <div class="row">
          <div class="col-md-2 col-4 bg-color-admin">
            <Left-admin> </Left-admin>
          </div>
          <div class="col-md-10 col-8">
            <div class="row">
              <div class="col-12 bg-color-brown">
                <span style="font-size: 22px; font-weight: 600"
                  >Feedbacks</span>
                
              </div>
              <div class="col-12 mg-top-20">
                <table v-for="feedbacks in feedbacks" :key="feedbacks.id"
                  class="
                    table table-striped table-bordered table-hover mg-bt-20
                    align-middle bg-white
                  "
                >
                <tr>
                    <th>Thư số</th>
                    <td> {{feedbacks.id}} </td>
                  </tr>
                  <tr>
                    <th>Chủ đề</th>
                    <td> {{feedbacks.topic}} </td>
                  </tr>
                  <tr>
                    <td>Tiêu đề</td>
                    <td>{{feedbacks.title}}</td>
                  </tr>
                  <tr>
                    <th colspan="2">THÔNG TIN LIÊN HỆ</th>
                  </tr>
                  <tr>
                    <td>Tên người gửi</td>
                    <td>{{feedbacks.name}}</td>
                  </tr>
                  <tr>
                    <td>E-Mail</td>
                    <td>{{feedbacks.email}}</td>
                  </tr>
                  <tr>
                    <td>Số điện thoại</td>
                    <td>{{feedbacks.phone}}</td>
                  </tr>
                  <tr>
                    <th colspan="2">NỘI DUNG</th>
                  </tr>
                  <tr>
                    <td colspan="2">{{feedbacks.des}}</td>
                  </tr>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>
<script>
export default {
    head() {
    return {
      title: "Feedback"
    };
  },
  async asyncData({ $axios }) {
    const feedbacks = await $axios.$get('/feedview/')
    return { feedbacks }
  },
}
</script>