<template>
  <div>
    <NuxtLink to="/admin/">Quản Lý đơn Hàng</NuxtLink>
    <NuxtLink to="/admin/products">Quản Lý Sản Phẩm</NuxtLink>
    <div v-for="order in orders" :key="order.orderstatus">
      <span>{{ order.orderid }}</span>
      <span>{{ order.orderdate }}</span>
      <span>{{ order.username }}</span>
      <div v-for="details in order.details" :key="details.productname">
        <span>{{ details.productname }}</span>
        <span>{{ details.img }}</span>
        <span>{{ details.quantity }}</span>
        <span>{{ details.price }}</span>
      </div>
      <span v-if="order.orderstatus === 'done'"
        ><span>Đã Hoàn Tất</span></span
      >
      <span v-else
        ><button @click="changeorderstatus(order.orderid)">
          {{ order.orderstatus }}
        </button></span
      >
    </div>
  </div>
</template>
<script>
export default {
  async asyncData({ $axios }) {
    const orders = await $axios.$get('/adminorderview/')
    return { orders }
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
