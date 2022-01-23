<template>
  <div>
    <div class="bg-color-brown section-checkout">
      <Header :preview="preview" :brands="brands"></Header>
      <BannerTop />
      <div class="section pd-top-20">
        <div class="container">
          <div class="row align-items-center justify-content-center">
            <div class="col-lg-11 col-12 no-pd">
              <h5>THANH TOÁN</h5>
            </div>
          </div>
          <div class="row justify-content-center">
            <div class="col-lg-8 col-12">
              <div
                v-for="item in cartdetails"
                :key="item.productname"
                class="row align-items-center justify-content-center"
              >
                <div
                  class="col-12 flex-column-1 items-cart mg-bottom-20 bd-rd-5"
                >
                  <div class="align-middle dp-flex-boostrap">
                    <img :src="item.img" height="100px" width="150px" />
                    <div class="dp-flex cart-p-content align-items-center">
                      <div class="cart-p-desc dp-flex align-items-center">
                        <div class="pd-lr">
                          <span>{{ item.productname }}</span>
                        </div>
                        <div class="checkout-sl ">
                          <div class="pd-lr ">
                            <span
                              ><b class="text-danger"
                                >{{ item.price }}$</b
                              ></span
                            >
                          </div>
                          <div class="pd-lr">
                            <span
                              ><b class="text-danger"
                                >Số lượng: {{ item.quantity }}</b
                              ></span
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-lg-3 col-12">
              <div class="row">
                <div
                  class="
                    col-12
                    flex-column-1
                    items-cart
                    mg-left-20
                    bd-rd-5
                    mg-bottom-20
                  "
                >
                  <div class="d-flex justify-content-between mg-bottom-10">
                    <span><b>Giao tới</b></span>
                  </div>
                  <div class="d-flex justify-content-between mg-bottom-10">
                    <span>Tên</span>
                    <span class="font-weight-500"
                      >{{ $auth.user.first_name }}
                      {{ $auth.user.last_name }}</span
                    >
                  </div>
                  <div class="d-flex justify-content-between mg-bottom-10">
                    <span>Email</span>
                    <span class="font-weight-500">{{ $auth.user.email }}</span>
                  </div>
                  <div class="justify-content-between">
                    <span class="font-weight-500"
                      ><input
                        class="form-control no-bd"
                        v-model="shippingaddress"
                        type="text"
                        placeholder="Nhập địa chỉ giao hàng..."
                        required
                    /></span>
                  </div>
                  <hr />
                  <div class="d-flex justify-content-between text-right">
                    <span>Tổng</span>
                    <div class="">
                      <span class="font-weight-500 total-price-1"
                        >{{ $auth.user.cart.carttotal }}$</span
                      >
                    </div>
                  </div>
                  <NuxtLink to="cart/checkout"
                    ><button
                      type="button"
                      class="btn muahang"
                      @click="checkout()"
                    >
                      Thanh Toán
                    </button></NuxtLink
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <Top-footer />
      <Footer />
    </div>
  </div>
</template>
<script>
export default {
  auth: 'auth',
  async asyncData({ $axios }) {
    const cartdetails = await $axios.$get('/cart/')
    const brands = await $axios.$get('/brand/')
    return { cartdetails, brands }
  },
  data() {
    return {
      shippingaddress: '',
    }
  },
  methods: {
    async checkout() {
      await this.$axios.$post('checkout/', {
        address: this.shippingaddress,
      })
      this.$router.push('/')
    },
  },
}
</script>
