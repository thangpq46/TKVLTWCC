<template>
  <div>
    <div v-for="item in cartdetails" :key="item.productname">
      <img :href="item.img">
      <span>{{ item.productname }}</span>
      <button type="button" @click="changeitem(item.productname,'-')">-</button>
      <span> {{ item.quantity }} </span>
      <button type="button" @click="changeitem(item.productname,'+')">+</button>
      <span>{{ item.price }}</span>
      <button type="button" @click="changeitem(item.productname,'x')">Remove</button>
    </div>
    <div>Total: {{$auth.user.cart.carttotal}}</div>
    <div><NuxtLink to="cart/checkout"><button type="button" @click="checkout">Đặt Hàng</button></NuxtLink></div>
  </div>
</template>
<script>
export default {
  async asyncData({ $axios }) {
    const cartdetails = await $axios.$get('/cart/')
    return { cartdetails }
  },
  data() {
    return {
      details: {
        productname: '',
        operator: '',
      },
    }
  },
  methods: {
    async changeitem(ProductName,operator) {
      this.details.productname =ProductName
      this.details.operator =operator
      await this.$axios.$post('changecartdetails/',{
        data: this.details
      })
      this.$nuxt.refresh()
    },
  },
}
</script>
