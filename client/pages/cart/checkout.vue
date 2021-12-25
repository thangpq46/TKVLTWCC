<template>
  <div>
    <div v-for="item in cartdetails" :key="item.productname">
      <img :href="item.img">
      <span>{{ item.productname }}</span>
      <span> {{ item.quantity }} </span>
      <span>{{ item.price }}</span>
    </div>
    <div><span>{{ $auth.user.first_name }}{{$auth.user.last_name }}</span></div>
    <div><span>{{ $auth.user.email }}</span></div>
    <div><span>Shipping address: <input v-model="shippingaddress" type="text" placeholder="hihi" required></span></div>
    <div><span>Total: {{ $auth.user.cart.carttotal }}</span></div>
    <div><button type="button" @click="checkout()">Checkout</button></div>
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
      shippingaddress:''
    }
  },
  methods: {
    async checkout() {
      await this.$axios.$post('checkout/',{
        address : this.shippingaddress
        }
      )
      this.$router.push('/')
    },
  },
}
</script>
