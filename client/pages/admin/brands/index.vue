<template>
  <div>
    <div>{{brands}}</div>
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
                  >List Brands</span
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
                      <th>Tên Hãng</th>
                      <th>Mô Tả</th>
                      <th>Hình Ảnh</th>
                      <th>
                        <a href="/admin/brands/add" class="btn btn-success">
                          <i class="bi bi-clipboard-plus"></i>
                          <span>Add Brand</span>
                        </a>
                      </th>
                    </tr>
                  </thead>
                  <tr v-for="brand in brands" :key="brand.brandname">
                    <th>{{ brand.brandname }}</th>
                    <td>{{ brand.branddes }}</td>
                    <td>
                      <img :src="brand.img" class="add-pr"/>
                    </td>
                    <td>
                      <NuxtLink :to="'/admin/brands/'+brand.id"
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
  middleware:  ['auth-admin'],
    head() {
    return {
      title: "Brands"
    };
  }, 
  async asyncData({ $axios }) {
    const brands = await $axios.$get('/brand/')
    return { brands }
  },
}
</script>
