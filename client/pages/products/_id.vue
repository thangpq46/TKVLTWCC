<template>
    <div>
        <Header/>
        <div class="container">
            <div class="row">
                <div class="col-12 col-md-6">
                    <img :src="product.img" :alt="product.productid" class="img-fluild">
                </div>
                <div class="col-12 col-md-6">
                    <h3>{{product.name}}</h3>
                    <div>
                      <h5 v-for="detail in details" :key="detail"> {{detail}}</h5>
                    </div>
                    <h4 v-if="product.stock > 1">Còn Hàng</h4>
                    <h4 v-else>Hết Hàng</h4>
                    <button class="btn btn-primary">MUA HÀNG</button>
                </div>
            </div>
        </div>
            <section class="container g-0 bg-light">
      <h2 class="block-header-title text-center">Sản Phẩm Tương Tự</h2>
      <div class="row g-0">
        <div v-for="p in products" :key="p.productcode" class="col-6 col-lg-3">
          <div class="product">
            <div class="img-thumbnail">
              <img
                class="img-fluid"
                :src="p.img"
              />
            </div>
            <div class="product_title">
              <a :href="getproductsurl(p.productcode)"
                >{{getsortname(p.name).name}}...</a
              >
            </div>
            <div class="product_price">
              <span>{{p.price}}$</span>
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
        <Footer/>
    </div>
</template>
<script>

export default {
    async asyncData({ $axios,params}) {
        const product = await $axios.$get(`/products/${params.id}`)
        const products = await $axios.$get(`/products`)
        const details=product.description.split('- ')
        return { product,products,details }
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
