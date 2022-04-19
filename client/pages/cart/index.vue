<template>
  <div class="bg-color-brown">
    {{ cart }}
    <Header :brands="brands"></Header>
    <BannerTop />
    <div v-if="$auth.user.numofproducts < 1" class="section pd-top-20">
      <div class="container">
        <div class="row align-items-center justify-content-center bd-rd-5">
          <div class="col-11 flex-column-1 items-cart items-empty-cart">
            <img
              src="http://localhost:3000/images/banner/empty-cart.png"
              alt="Empty Cart"
              class="rounded mx-auto d-block"
            />
            <p class="text-center">
              Không có sản phẩm nào trong giỏ hàng của bạn.
            </p>
            <a href="http://localhost:3000" class="btn btn-primary"
              >Tiếp tục mua sắm</a
            >
          </div>
        </div>
      </div>
    </div>
    <div v-else class="section pd-top-20">
      <div class="container">
        <div class="row align-items-center justify-content-center">
          <div class="col-lg-11 col-12 no-pd">
            <h5>GIỎ HÀNG</h5>
          </div>
        </div>
        <div class="row justify-content-center">
          <div class="col-lg-8 col-12">
            <div
              v-for="item in cart.cartdetails"
              :key="item.productname"
              class="row align-items-center justify-content-center"
            >
              <div class="col-12 flex-column-1 items-cart mg-bottom-20 bd-rd-5">
                <div class="align-middle dp-flex">
                  <img :src="item.img" height="100px" width="150px" />
                  <div class="dp-flex cart-p-content align-items-center">
                    <div class="cart-p-desc dp-flex align-items-center">
                      <div>
                        <span>{{ item.productname }}</span>
                      </div>
                      <div>
                        <span
                          ><b class="text-danger">{{ item.price }}$</b></span
                        >
                      </div>
                    </div>
                    <div class="cart-p-actions dp-flex align-items-center">
                      <div class="cart-p-actions-i">
                        <i
                          class="bi bi-dash"
                          @click="changeitem(item.productid, '-')"
                        ></i>
                        <span
                          ><b> {{ item.quantity }} </b></span
                        >
                        <i
                          class="bi bi-plus"
                          @click="changeitem(item.productid, '+')"
                        ></i>
                      </div>
                      <div>
                        <button
                          type="button"
                          class="btn btn-danger"
                          @click="changeitem(item.productid, 'x')"
                        >
                          <i class="bi bi-trash delete-cart"></i>
                        </button>
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
                class="col-12 flex-column-1 items-cart mg-left-20 bd-rd-5 mg-bottom-20"
              >
                <div class="d-flex justify-content-between mg-bottom-10">
                  <span>Tạm tính</span>

                  <span class="font-weight-500">{{ cart.total }}$</span>
                </div>
                <div class="d-flex justify-content-between">
                  <span>Giảm giá</span>
                  <span class="font-weight-500">0$</span>
                </div>
                <hr />
                <div class="d-flex justify-content-between text-right">
                  <span>Tổng cộng</span>
                  <div class="">
                    <span class="font-weight-500 total-price-1"
                      >{{ cart.total }}$</span
                    >
                    <span class="total-price-2">(Đã bao gồm VAT nếu có)</span>
                  </div>
                </div>
                <NuxtLink to="cart/checkout"
                  ><button type="button" class="btn muahang">
                    Đặt Hàng
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
</template>
<script>
import BannerTop from '../../components/BannerTop.vue'
export default {
  components: { BannerTop },
  async asyncData({ $axios }) {
    const cart = await $axios.$get('/cart/')
    const brands = await $axios.$get('/brand/')
    return { cart, brands }
  },
  data() {
    return {
      details: {
        productid: '',
        operator: '',
      },
    }
  },
  methods: {
    async changeitem(productid, operator) {
      this.details.productid = productid
      this.details.operator = operator
      await this.$axios.$post('changecartdetails/', {
        data: this.details,
      })
      this.$nuxt.refresh()
      await this.$auth.fetchUser()
    },
  },
}
</script>
