<template>
  <div>
    <Header :preview="preview" :brands="brands"></Header>
    <BannerTop />
    <div class="section section-lienhe pd-top-20">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-7 col-12">
            <div class="form-lienhe">
              <h5 style="color: #1976d2">
                XIN HÂN HẠNH ĐƯỢC HỖ TRỢ QUÝ KHÁCH.
              </h5>
              <table>
                <tr>
                  <td>Quý khách đang quan tâm về:</td>
                  <td>
                    <select class="form-control" v-model="feedback.topic">
                      <option value="0" selected>Chọn Chủ đề</option>
                      <option value="Tư vấn" selected>Tư vấn</option>
                      <option value="Khiếu nại - Phản ánh">
                        Khiếu nại - Phản ánh
                      </option>
                      <option value="Góp ý cải tiến">Góp ý cải tiến</option>
                      <option value="Khác">Khác</option>
                    </select>
                  </td>
                </tr>
                <tr>
                  <td>Tiêu đề:</td>
                  <td>
                    <input
                      type="text"
                      v-model="feedback.title"
                      class="form-control"
                    />
                  </td>
                </tr>
                <tr>
                  <td>Họ và tên:</td>
                  <td>
                    <input
                      type="text"
                      v-model="feedback.name"
                      class="form-control"
                    />
                  </td>
                </tr>
                <tr>
                  <td>Địa chỉ Email:</td>
                  <td>
                    <input
                      type="email"
                      v-model="feedback.email"
                      class="form-control"
                    />
                  </td>
                </tr>
                <tr>
                  <td>Số điện thoại:</td>
                  <td>
                    <input
                      type="text"
                      v-model="feedback.phone"
                      class="form-control"
                    />
                  </td>
                </tr>
                <tr>
                  <td>Nội dung:</td>
                  <td>
                    <textarea
                      v-model="feedback.des"
                      placeholder="Xin quý khách vui lòng mô tả chi tiết"
                      class="form-control"
                    ></textarea>
                  </td>
                </tr>
                <tr>
                  <td></td>
                  <td>
                    <input
                      type="button"
                      @click="submitFeed()"
                      class="btn btn-primary"
                      value="Gửi"
                    />
                  </td>
                </tr>
                <tr>
                  <td></td>
                  <td>
                    <span class="btn-outline-danger" if="status !=null">{{
                      status
                    }}</span>
                  </td>
                </tr>
              </table>
            </div>
          </div>
          <div
            class="
              col-lg-3 col-12
              d-max-992-none
              icons-lienhe
              align-items-center
            "
          >
            <img class="lh1" src="images/banner/lh1.png" alt="" />
            <a href="tel:19001234">
              <i class="fas fa-phone-alt"></i>
              <span>1900 1234</span>
            </a>
            <a href="mailto:laptrinhweb@gmail.com">
              <i class="bi bi-envelope"></i>
              <span>nhom4@gmail.com</span>
            </a>
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
  async asyncData({ $axios }) {
    const brands = await $axios.$get('/brand/')
    return { brands }
  },
  data() {
    return {
      feedback: {
        topic: '',
        title: '',
        name: '',
        email: '',
        phone: '',
        des: '',
      },
      status: null,
    }
  },
  methods: {
    async submitFeed() {
      const response = await this.$axios.$post('/submitfeed/', {
        feedback: this.feedback,
      })
      this.status = response.status
    },
  },
}
</script>
