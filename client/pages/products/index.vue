<template>
    <div>
          <section class="container g-0 bg-light">
      <div class="row g-0">
        <div
          v-for="product in products"
          :key="product.productid"
          class="col-6 col-lg-3"
        >
          <div class="product">
            <div class="img-thumbnail">
              <img class="img-fluid" :src="product.img" />
            </div>
            <div class="product_title">
              <a :href="getproductsurl(product.productcode)"
                >{{ getsortname(product.name).name }}...</a
              >
            </div>
            <div class="product_price">
              <span>{{ product.price }}$</span>
            </div>
            <div>
              <button type="button" class="btn btn-primary add-to-cart col-12">
                Mua Ngay
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
    </div>
</template>
<script>

export default {
    auth: 'guest',
    async asyncData({ $axios,params}) {
        const products = await $axios.$get(`/products/`)
        return {products}
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
