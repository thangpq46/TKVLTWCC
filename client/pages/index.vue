<template>
  <div>
    <Header :brands="brands"></Header>
    <BannerTop />
    <Brand :brands="brands"></Brand>
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
            <ProductCard :product="product"></ProductCard>
          </div>
        </div>
      </div>
    </div>
    <div class="section">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="block__header">
              <h2 class="block-header-title text-center">SẢN PHẨM NỔI BẬT</h2>
            </div>
          </div>
          <div
            v-for="product in instockproducts"
            :key="product.productcode"
            class="col-lg-3 col-md-4 col-6 items-product mg-bt-30"
          >
            <ProductCard :product="product"></ProductCard>
          </div>
        </div>
      </div>
    </div>
    <div class="section">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="block__header">
              <h2 class="block-header-title text-center">SẢN PHẨM BÁN CHẠY</h2>
            </div>
          </div>
          <div
            v-for="product in hotproducts"
            :key="product.productcode"
            class="col-lg-3 col-md-4 col-6 items-product mg-bt-30"
          >
            <ProductCard :product="product"></ProductCard>
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
  auth: 'guest',
  async asyncData({ $axios }) {
    const brands = await $axios.$get('/brand/')
    const newproducts = await $axios.$get('/newproducts/')
    const instockproducts = await $axios.$get('/instockproducts/')
    const hotproducts = await $axios.$get('/hotproducts/')
    console.log(newproducts)
    return { newproducts, instockproducts, hotproducts, brands }
  },
  methods: {
    getsortname(name) {
      name = name.substring(0, 55)
      return { name }
    },
    getproductsurl(productid) {
      const url = '/products/' + productid
      return url
    },
    async addtocart(productcode) {
      if (this.$auth.loggedIn) {
        await this.$axios.$post('addtocart/', {
          productcode: productcode,
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
