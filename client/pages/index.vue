<template>
  <div>
    <Header :brands="brands"></Header>
    <BannerTop />
    <Brand :brands="brands"></Brand>
    <New-products :newproducts="newproducts"></New-products>
    <Instock-products :instockproducts="instockproducts"></Instock-products>
    <Hot-products :hotproducts="hotproducts"></Hot-products>
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
    filterproducts(searchinput){
      if (searchinput === '') {
        return "/products"
      }
      else {
        return"/products/filter/"+ searchinput
      }
    }
  },
}
</script>
