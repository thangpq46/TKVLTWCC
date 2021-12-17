<template>
    <div>
        <NuxtLink to="/admin/ordermanage">Quản Lý đơn Hàng</NuxtLink>
        <NuxtLink to="/admin/productmanage">Quản Lý Sản Phẩm</NuxtLink>
        {{orders}}
    </div>
</template>
<script>
export default {
    async asyncData({ $axios }) {
    const orders = await $axios.$get('/adminorderview/')
    return { orders }
  },
}
</script>
