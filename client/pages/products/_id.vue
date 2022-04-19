<template>
  <div>
    <Header></Header>
    <div class="section pd-top-20">
      <div class="container">
        <div class="row">
          <div class="col-md-6 col-12">
            <img
              class="item img-fluid"
              :src="product.img"
              :alt="product.productid"
            />
          </div>
          <div class="col-md-6 col-12 info-product-right align-items-center">
            <h4>{{ product.name }}</h4>
            <div>
              <span class="price">{{ product.price }}$</span>
            </div>
            <ul class="review">
              <li><i class="lni lni-star-filled"></i></li>
              <li><i class="lni lni-star-filled"></i></li>
              <li><i class="lni lni-star-filled"></i></li>
              <li><i class="lni lni-star-filled"></i></li>
              <li><i class="lni lni-star-filled"></i></li>
              <li><span>5.0</span></li>
            </ul>
            <hr />
            <div class="product-info-items">
              <p v-for="detail in details" :key="detail">{{ detail }}</p>
              <p v-if="product.stock > 1"><b>Còn Hàng</b></p>
              <p v-else><b>Hết Hàng</b></p>
              <button class="btn btn-danger" @click="addtocart(product.productid)">
                MUA HÀNG
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Productsections :products="products" sectiontitle="Sản Phẩm Tương Tự"/>
    <Top-footer />
    <Footer />
  </div>
</template>
<script>
export default {
  auth: false,
  async asyncData({ $axios, params }) {
    const product = await $axios.$get(`/products/${params.id}`)
    const products = await $axios.$get(`/products`)
    const details = product.description.split('- ')
    return { product, products, details }
  },
    methods: {
    async addtocart(productid) {
      if (this.$auth.loggedIn) {
        await this.$axios.$post('addtocart/', {
          productid: productid,
        })
        // this.$nuxt.refresh()
        this.$router.go()
      } else {
        this.$router.push('/login/')
      }
    },
  },
}
</script>
