<template>
  <div>
    <notifications position="top center" ignoreDuplicates width=400 height=700 group="foo" />
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
                        <th colspan="5">ĐƠN HÀNG {{ order.orderid }}</th>
                      </tr>
                    </thead>
                    <tr>
                      <td>Ngày đặt hàng</td>
                      <td colspan="4">
                        {{ order.orderdate }}
                      </td>
                    </tr>
                    <tr>
                      <td>Tên người đặt</td>
                      <td colspan="4">
                        {{ order.username }}
                      </td>
                    </tr>
                    <tr>
                      <td>Số điện thoại</td>
                      <td colspan="4">
                        {{ order.userphonenum }}
                      </td>
                    </tr>
                    <tr>
                      <td>Địa chỉ</td>
                      <td colspan="4">
                        {{ order.orderaddress }}
                      </td>
                    </tr>
                    <tr>
                      <th>Tên sản phẩm:</th>
                      <th>Giá:</th>
                      <th>Số lượng</th>
                      <th>Hình ảnh</th>
                      <th>Thành Tiền</th>
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
                      <th class="align-middle">{{details.intomoney }}$</th>
                    </tr>
                    <tr>
                      <th>Tổng :</th>
                      <th colspan="2">{{ order.total }}$</th>
                      <th colspan="2">
                        <span
                          class="text-success"
                          v-if="order.orderstatus === 2"
                        >
                          Đã hoàn tất
                        </span>
                        <span
                          class="text-danger"
                          v-else-if="order.orderstatus === -1"
                        >
                          Đã hủy
                        </span>
                        <span v-else
                          ><button v-if="order.orderstatus === 0"
                            class="btn btn-success"
                            @click="changeorderstatus(order.orderid)"
                          >
                            Xác nhận đơn hàng
                          </button>
                          <button v-if="order.orderstatus === 1"
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
  middleware:  ['auth-admin'],
  async asyncData({ $axios }) {
    const orders = await $axios.$get('/adminorderview/')
    return { orders }
  },
  methods: {
    async changeorderstatus(OrderID, cancelorder = false) {
      if (cancelorder) {
        const response= await this.$axios.delete('adminorderview/', {
          data: { orderid: OrderID },
        })
        if(response.status===202){
          this.$notify({
            group: 'foo',
            position:'top center',
            title: 'Notification',
            text: 'Cancel Order Successfuly!',
          })
        }
      }
      else{
        const response= await this.$axios.post('adminorderview/', {
        orderid: OrderID,
      })
        if(response.status===200){
          this.$notify({
            group: 'foo',
            title: 'Notification',
            text: 'Change Order State Successfuly!',
          }) 
        }
      }
      this.$nuxt.refresh()
      // this.$router.go()
    },
  },
}
</script>