<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container g-0">
      <a
        class="navbar-brand btn btn-outline-success"
        href="http://localhost:3000"
        >QT Store</a
      >
    </div>
    <input v-model="searchinput" type="text">
    <a :href="filterproducts(searchinput)"><button type="button" class="">Search</button></a>
    <div v-if="$auth.loggedIn">
      <div>Wellcome {{ $auth.user.first_name }}{{$auth.user.last_name }}<img :src="$auth.user.img"></div>
      <NuxtLink to="/cart">Cart {{ $auth.user.productincart}}</NuxtLink>
      <NuxtLink to="/"><button @click="logout">Logout</button></NuxtLink>
    </div>
    <div v-else>
      <NuxtLink to="/login">Login</NuxtLink>
      <NuxtLink to="/register">Register</NuxtLink>
    </div>
  </nav>
</template>
<script>
export default {
  data() {
    return {
      searchinput: '',
    }
  },
  methods: {
    filterproducts(searchinput){
      if (searchinput === '') {
        return "/products"
      }
      else {
        return"/products/filter/"+ searchinput
      }
    },
    async logout(){
      await this.$auth.logout(/* .... */)
      window.localStorage.clear();
      // console.log($cookies.keys());
    },
  }
}
</script>
