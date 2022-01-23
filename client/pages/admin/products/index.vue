<template>
  <div>
    <Header-admin></Header-admin>
    <div class="section">
      <div class="container-fluid">
        <div class="row">
          <div class="col-md-2 col-4 bg-color-admin">
            <Left-admin />
          </div>
          <div class="col-md-10 col-8">
            <div class="row">
              <div class="col-12 bg-color-brown">
                <span style="font-size: 22px; font-weight: 600"
                  >List Products</span
                >
              </div>
              <div class="col-12 table-responsive">
                <table
                  class="
                    table table-bordered table-striped table-hover
                    align-middle-dt
                  "
                >
                  <thead>
                    <tr>
                      <th>Mã SP</th>
                      <th>Tên sản phẩm</th>
                      <th>Giá</th>
                      <th>Thông số</th>
                      <th>Hình ảnh</th>
                      <th>Số lượng</th>
                      <th>
                        <a href="/admin/products/add" class="btn btn-success">
                          <i class="bi bi-clipboard-plus"></i>
                          <span>Add Products</span>
                        </a>
                      </th>
                    </tr>
                  </thead>
                  <tr v-for="product in products" :key="product.productcode">
                    <th>{{ product.productcode }}</th>
                    <td>
                      {{ product.name }}
                    </td>
                    <td>{{ product.price }}$</td>
                    <td>{{ product.description }}</td>
                    <td>
                      <img :src="product.img" class="add-pr"/>
                    </td>
                    <td>{{ product.stock }}</td>
                    <td>
                      <NuxtLink :to="'/admin/products/' + product.productcode"
                        ><button class="btn btn-danger" type="button">
                          Chỉnh sửa
                        </button></NuxtLink
                      >
                    </td>
                  </tr>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>
<script>
export default {
    head() {
    return {
      title: "Products"
    };
  }, 
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
