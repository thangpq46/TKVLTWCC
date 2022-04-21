<template>
  <div class="bg-color-brown">
    <Header :brands="brands"></Header>
    <BannerTop />
    <div class="section pd-top-20">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-11 no-pd">
            <h5>Lịch sử đơn hàng</h5>
          </div>
        </div>

        <div class="row justify-content-center">
          <div class="col-11 bg-white bd-rd-5 mg-bottom-20 table-responsive">
            <div v-for="order in orders" :key="order.orderstatus">
              <br />

              <table class="table align-middle table-bordered">
                <thead>
                  <tr>
                    <th colspan="5"># {{ order.orderid }}</th>
                  </tr>
                </thead>
                <tr>
                  <td>Ngày đặt hàng</td>
                  <td colspan="4">
                    {{ order.orderdate }}
                  </td>
                </tr>
                <tr>
                  <td>Tài khoản</td>
                  <td colspan="4">
                    {{ order.username }}
                  </td>
                  
                </tr>
                <tr>
                  <td>SĐT</td>
                  <td colspan="4">
                    {{ order.phonenum }}
                  </td>
                </tr>
                <tr>
                  <td>Địa chỉ</td>
                  <td colspan="5">
                    {{ order.orderaddress }}
                  </td>
                </tr>
                <tr>
                  <th>Tên sản phẩm:</th>
                  <th>Giá:</th>
                  <th>Số lượng</th>
                  <th>Hình ảnh</th>
                  <th>Thành tiền</th>
                </tr>
                <tr v-for="details in order.details" :key="details.productname">
                  <td class="align-middle">
                    {{ details.productname }}
                  </td>
                  <th class="align-middle">{{ details.price }}$</th>
                  <th class="align-middle">
                    {{ details.quantity }}
                  </th>
                  <th>
                    <a>
                      <img
                        :src="details.img"
                        alt=""
                        height="100px"
                        width="150px"
                      />
                    </a>
                  </th>
                  <th class="align-middle">
                    {{ details.intomoney }}$
                  </th>
                </tr>
                <tr>
                  <th>Tổng giá:</th>
                  <th colspan="2">{{ order.total }}$</th>
                  <th colspan="2">
                    <span v-if="order.orderstatus === 0" class="btn btn-warning"
                      >Đang chờ xử lí</span
                    >
                    <span
                      v-else-if="order.orderstatus === 1"
                      class="btn btn-success"
                      >Đã Xác Nhận</span
                    >
                    <span
                      v-else-if="order.orderstatus === 2"
                      class="btn btn-success"
                      >Đã Hoàn Tất</span
                    >
                    <span v-else class="btn btn-danger">Đã Hủy</span>
                    <button
                      v-if="order.orderstatus === 0"
                      type="button"
                      class="btn btn-danger"
                      @click="cancelorder(order.orderid)"
                    >
                      Hủy đơn
                    </button>
                  </th>
                </tr>
              </table>
            </div>
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
  props: {
    brand: {
      type: Object,
      default: null,
    },
  },
  async asyncData({ $axios }) {
    const orders = await $axios.$get('/userorders/')
    const brands = await $axios.$get('/brand/')
    return { orders, brands }
  },
  methods: {
    async cancelorder(id) {
      await this.$axios.$post('/userorders/', {
        orderid: id,
      })
      this.$router.go()
    },
  },
}
</script>
