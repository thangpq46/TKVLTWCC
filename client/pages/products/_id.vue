<template>
  <div>
    <Header />
    <div class="container">
      <div class="row">
        <div class="col-12 col-md-6">
          <img :src="product.img" :alt="product.productid" class="img-fluild" />
        </div>
        <div class="col-12 col-md-6">
          <h3>{{ product.name }}</h3>
          <div>
            <h5 v-for="detail in details" :key="detail">{{ detail }}</h5>
          </div>
          <h4 v-if="product.stock > 1">Còn Hàng</h4>
          <h4 v-else>Hết Hàng</h4>
          <button class="btn btn-primary" @click="addtocart(product.name)">
            MUA HÀNG
          </button>
        </div>
      </div>
    </div>
    <section class="container g-0 bg-light">
      <h2 class="block-header-title text-center">Sản Phẩm Tương Tự</h2>
      <div class="row g-0">
        <div
          v-for="product in products"
          :key="product.productcode"
          class="col-6 col-lg-3"
        >
          <ProductCard :product="product" />
        </div>
      </div>
    </section>
    <Footer />
  </div>
</template>
<script>
export default {
  auth: 'guest auth',
  async asyncData({ $axios, params }) {
    const product = await $axios.$get(`/products/${params.id}`)
    const products = await $axios.$get(`/products`)
    const details = product.description.split('- ')
    return { product, products, details }
  },
  methods: {
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
  },
}
</script>
