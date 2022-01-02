<template>
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
      <button
        type="button"
        class="btn btn-primary add-to-cart col-12"
        @click="addtocart(product.name)"
      >
        Mua Ngay
      </button>
    </div>
  </div>
</template>
<script>
export default {
  auth: 'guest auth',
  props: {
    product: {
      type:Object,
      required:true,
      default: null
    }
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
    async addtocart(ProductName) {
      if(this.$auth.loggedIn){
        await this.$axios.$post('addtocart/', {
        productname: ProductName,
      })
      this.$nuxt.refresh();
      this.$router.go()
      }
      else{
        this.$router.push('/login/');
      }
    },
  },
}
</script>