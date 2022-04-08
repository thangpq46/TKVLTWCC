<template>
  <div>
    <Header :preview="preview" :brands="brands"></Header>
    <BannerTop />
    <Brand :brands="brands"></Brand>
     <div class="section">
      <div class="container">
        <div class="row">
          <div
            v-for="product in products"
            :key="product.productcode"
            class="col-lg-3 col-md-4 col-6 items-product mg-bt-30"
          >
            <div class="product-img">
              <a :href="getproductsurl(product.productcode)">
                <img
                  :src="product.img"
                  alt=""
                  class="img-fluid rounded mx-auto d-block"
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
    <Top-footer />
    <Footer />
  </div>
</template>

<script>
export default {
    auth: false,
    async asyncData({ $axios,params}) {
        const products = await $axios.$get(`/products/`)
        const brands = await $axios.$get('/brand/')
        return {products, brands}
    },
    methods: {
    getsortname(name){
      name=name.substring(0,55)
      return { name }
    },
    getproductsurl(productid){
      const url = '/products/'+productid
      return url;
    },
  }
}
</script>
