<template>
  <div>
    <Header-admin></Header-admin>
    <div class="section">
      <div class="container-fluid">
        <div class="row">
          <div class="col-md-2 col-4 bg-color-admin">
            <Left-admin></Left-admin>
          </div>
          <div class="col-md-10 col-8">
            <div class="row">
              <div class="col-12 bg-color-brown">
                <span style="font-size: 22px; font-weight: 600"
                  >List Orders</span
                >
              </div>
              <div class="col-12 table-responsive">
                <div v-for="order in orders" :key="order.orderstatus">
                  <br />
                  <hr />
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
                    <tr
                      v-for="details in order.details"
                      :key="details.productname"
                    >
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
                        <span
                          class="text-success"
                          v-if="order.orderstatus === 'done'"
                        >
                          Đã hoàn tất
                        </span>
                        <span
                          class="text-danger"
                          v-else-if="order.orderstatus === 'canceled'"
                        >
                          Đã hủy
                        </span>
                        <span v-else
                          ><button v-if="order.orderstatus === 'pending'"
                            class="btn btn-success"
                            @click="changeorderstatus(order.orderid)"
                          >
                            Xác nhận đơn hàng
                          </button>
                          <button v-if="order.orderstatus === 'confirmed'"
                            class="btn btn-success"
                            @click="changeorderstatus(order.orderid)"
                          >
                            Xử lý đơn hàng
                          </button>
                          
                          <button
                            class="btn btn-danger"
                            @click="changeorderstatus(order.orderid, true)"
                          >
                            Hủy
                          </button></span
                        >
                      </th>
                    </tr>
                  </table>
                </div>
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
  async asyncData({ $axios }) {
    const orders = await $axios.$get('/adminorderview/')
    return { orders }
  },
  methods: {
    async changeorderstatus(OrderID, cancelorder = false) {
      if (cancelorder) {
        await this.$axios.delete('adminorderview/', {
          data: { orderid: OrderID },
        })
      }
      await this.$axios.post('adminorderview/', {
        orderid: OrderID,
      })
      this.$router.go()
    },
  },
}
</script>