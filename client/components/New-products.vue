<template>
  <div>
    <div class="section">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="block__header">
            <h2 class="block-header-title text-center">SẢN PHẨM MỚI VỀ</h2>
            </div>
          </div>
          <div
            v-for="product in newproducts"
            :key="product.productcode"
            class="col-lg-3 col-md-4 col-6 items-product mg-bt-30"
          >
            <div class="product-img">
              <a :href="getproductsurl(product.productcode)">
                <img
                  :src="product.img"
                  alt=""
                  class="img-fluid rounded mx-auto d-block pd-10"
                />
              </a>
            </div>
            <div class="product-info">
              <a :href="getproductsurl(product.productcode)">
              <h6>{{ getsortname(product.name).name }}...</h6>
              </a>
              <span>{{ product.price }}$</span>
              <button
                type="button"
                class="btn btn-danger add-to-cart col-12"
                @click="addtocart(product.name)"
              >
                Mua Ngay
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  auth: 'guest',
  props: ['newproducts'],
  methods: {
    getsortname(name) {
      name = name.substring(0, 55)
      return { name }
    },
    getproductsurl(productid) {
      const url = '/products/' + productid
      return url
    },
    async addtocart(ProductName) {
      if (this.$auth.loggedIn) {
        await this.$axios.$post('addtocart/', {
          productname: ProductName,
        })
        this.$nuxt.refresh()
        this.$router.go()
      } else {
        this.$router.push('/login/')
      }
    },
    filterproducts(searchinput) {
      if (searchinput === '') {
        return '/products'
      } else {
        return '/products/filter/' + searchinput
      }
    },
  },
}
</script>
