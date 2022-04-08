<template>
  <div>
    <div class="bg-color-brown section-checkout">
      <!-- <Header :preview="preview" :brands="brands"></Header> -->
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
                v-for="item in cart.cartdetails"
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
                    <select v-model="province">
                      <option 
                        v-for="(adr, index) in address"
                        :key="adr.name"
                        :value=index
                      >{{adr.name}}</option>
                    </select>
                    <select v-model="distri">
                      <option 
                        v-for="(district,index) in address[province].districts"
                        :key="district.name"
                        :value=index
                      >{{district.name}}</option>
                    </select>
                    <select v-model="ward">
                      <option 
                        v-for="(ward,index) in address[province].districts[distri].wards"
                        :key="ward.name"
                        :value=index
                      >{{ward.name}}</option>
                    </select>
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
                        >{{ cart.total }}$</span
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
    const cart = await $axios.$get('/cart/')
    const brands = await $axios.$get('/brand/')
    const address = await $axios.$get('/get_provinces_json')
    return { cart, brands,address }
  },
  data() {
    return {
      shippingaddress: '',
      province: 0,
      distri:0,
      ward:0
    }
  },
  methods: {
    async checkout() {
      const userprovince = this.address[this.province];
      const userdistrict = userprovince.districts[this.distri];
      const userward = userdistrict.wards[this.ward]
      const address =this.shippingaddress + ', '+userward.name + ', '+userdistrict.name+ ', '+ userprovince.name ;
      try{
        const response= await this.$axios.post('checkout/', {
        address: address,
        })
        if(response.status==202){
          // must haave nofi success on place order
          this.$router.push('/')
        }
      }
      catch(e){
        console.log(e.response)
      }
      // this.$router.push('/')
    },
  },
}
</script>
