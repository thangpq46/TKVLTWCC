<template>
  <div>
    <NuxtLink to="/admin/">Quản Lý đơn Hàng</NuxtLink>
    <NuxtLink to="/admin/products">Quản Lý Sản Phẩm</NuxtLink>
    <div>{{products}}</div>
    <div v-for="product in products" :key="product.productcode">
      <span><img :src="product.img"></span>
      <span>{{product.productcode}}</span>
      <span>{{product.name}}</span>
      <span>{{product.price}}</span>
      <span>{{product.description}}</span>
      <span>{{product.stock}}</span>
      <NuxtLink :to="'products/'+product.productcode"><button type="button">Chỉnh sửa</button></NuxtLink>
    </div>
  </div>
</template>
<script>
export default {
  async asyncData({ $axios }) {
    const products = await $axios.$get('/products/')
    return { products }
  },
  methods: {
    async changeorderstatus(OrderID) {
      await this.$axios.post('adminorderview/', {
        orderid: OrderID,
      })
      this.$router.go()
    },
  },
}
</script>
