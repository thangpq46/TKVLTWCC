<template>
  <div>
    <AdminHeader />
    {{orders}}
    <div v-for="order in orders" :key="order.orderstatus">
      <span>{{ order.orderid }}</span>
      <span>{{ order.orderdate }}</span>
      <span>{{ order.username }}</span>
      <span>{{ order.orderaddress }}</span>
      <span>{{ order.total }}</span>
      <div v-for="details in order.details" :key="details.productname">
        <span>{{ details.productname }}</span>
        <span>{{ details.img }}</span>
        <span>{{ details.quantity }}</span>
        <span>{{ details.price }}</span>
      </div>
      <span v-if="order.orderstatus === 'done'"
        ><span>Đã Hoàn Tất</span></span
      >
      <span v-else-if="order.orderstatus === 'canceled'">
        <span>Đã Hủy</span>
      </span>
      <span v-else
        ><button @click="changeorderstatus(order.orderid)">
          {{ order.orderstatus }}
        </button>
        <button @click="changeorderstatus(order.orderid,true)">Hủy</button>
        </span
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
    async changeorderstatus(OrderID,cancelorder=false) {
      if (cancelorder){
        await this.$axios.delete('adminorderview/', { data: { orderid: OrderID } })
      }
      await this.$axios.post('adminorderview/', {
        orderid: OrderID,
      })
      this.$router.go()
    },
  },
}
</script>
