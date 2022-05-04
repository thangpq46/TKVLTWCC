<template>
  <div>
    <notifications position="top right" ignoreDuplicates width=400 height=700 group="foo" />
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
        @click="addtocart(product.productid)"
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
      type: Object,
      required: true,
      default: null,
    },
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
    async addtocart(productid) {
      if (this.$auth.loggedIn) {
        await this.$axios.$post('addtocart/', {
          productid: productid,
        })
        await this.$auth.fetchUser()
        this.$notify({
            group: 'foo',
            title: 'Notification',
            text: 'Added to Cart!',
          })
      } else {
        this.$router.push('/login/')
      }
      
    },
  },
}
</script>
