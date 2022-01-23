<template>
  <div class="bg-color-brown">
    <Header :brands="brands"></Header>
    <BannerTop />
    <div class="section pd-top-20 ">
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
                    <th colspan="4">ĐƠN HÀNG {{ order.orderid }}</th>
                  </tr>
                </thead>
                <tr>
                  <td>Ngày đặt hàng</td>
                  <td colspan="3">
                    {{ order.orderdate }}
                  </td>
                </tr>
                <tr>
                  <td>Tài khoản</td>
                  <td colspan="3">
                    {{ order.username }}
                  </td>
                </tr>
                <tr>
                  <td>Địa chỉ</td>
                  <td colspan="3">
                    {{ order.orderaddress }}
                  </td>
                </tr>
                <tr>
                  <th>Tên sản phẩm:</th>
                  <th>Giá:</th>
                  <th>Số lượng</th>
                  <th>Hình ảnh</th>
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
                </tr>
                <tr>
                  <th>Tổng giá:</th>
                  <th colspan="2">{{ order.total }}$</th>
                  <th>
                    <span v-if="order.orderstatus === 'pending'" class="btn btn-warning"
                      >Đang chờ xử lí</span
                    >
                    <span v-else-if="order.orderstatus === 'confirmed'" class="btn btn-success"
                      >Đã Xác Nhận</span
                    >
                    <span v-else-if="order.orderstatus === 'done'" class="btn btn-success"
                      >Đã Hoàn Tất</span
                    >
                    <span v-else class="btn btn-danger">Đã Hủy</span>
                    <button
                      v-if="order.orderstatus === 'pending'"
                      type="button" class="btn btn-danger"
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
      required: true,
      default: null,
    },
  },
  async asyncData({ $axios }) {
    const orders = await $axios.$get('/userorders/')
    const brands = await $axios.$get('/brand/')
    return { orders , brands }
  },
  methods: {
    async cancelorder(id) {
      const response = await this.$axios.$post('/userorders/', {
        orderid: id,
      })
      console.log(response)
    },
  },
}
</script>
