<template>
  <div>
    <Header :brands="brands"></Header>
    <BannerTop />
    <Brand :brands="brands"/>
    <Productsections :products="newproducts" sectiontitle="Sản Phẩm Mới Về"/>
    <Productsections :products="instockproducts" sectiontitle="Sản Phẩm Nổi Bật"/>
    <Productsections :products="hotproducts" sectiontitle="Sản Phẩm Bán Chạy"/>
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
}
</script>
