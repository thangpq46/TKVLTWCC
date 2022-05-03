<template>
  <div>
    <Header-admin></Header-admin>
    <div class="section bg-color-brown">
      
      <div class="container-fluid">
        
        <div class="row">
          
          <div class="col-md-2 col-4 bg-color-admin">
            <Left-admin></Left-admin>
          </div>
          <div class="col-md-10 col-8">
            <div class="row">
              <div class="col-12 bg-white">
                <span style="font-size: 22px; font-weight: 600"
                  >Edit Products</span
                >
              </div>
              <div class="col-12 mg-top-20">
                <div class="row justify-content-center">
                  <div class="col-md-11 col-12 bg-white bd-rd-5 mg-bottom-20">
                    
                      <table class="table ">
                        <notifications position="top center" ignoreDuplicates width=400 height=700 group="productadmin" />
                        <tr>
                          <th>Hình ảnh</th>
                          <td>
                            <img :src="preview" height="100px" width="150px" />
                            <input type="file" accept="image/png, image/jpeg" @change="onFileChange" />
                          </td>
                        </tr>
                        <tr>
                          <th>Mã sản phẩm</th>
                          <td>
                            <input
                              v-model="product.productcode"
                              type="text"
                              class="form-control"
                            />
                          </td>
                        </tr>
                        <tr>
                          <th>Tên sản phẩm</th>
                          <td>
                            <input
                              v-model="product.name"
                              type="text"
                              class="form-control"
                            />
                          </td>
                        </tr>
                        <tr>
                          <th>Thông số sản phẩm</th>
                          <td>
                            <textarea
                              class="form-control"
                              v-model="product.description"
                              name=""
                              id=""
                              cols="30"
                              rows="10"
                            ></textarea>
                          </td>
                        </tr>
                        <tr>
                          <th>Giá sản phẩm</th>
                          <td>
                            <input
                              v-model="product.price"
                              type="number"
                              class="form-control"
                            />
                          </td>
                        </tr>
                        <tr>
                          <th>Số lượng trong kho</th>
                          <td>
                            <input
                              v-model="product.stock"
                              type="number"
                              class="form-control"
                            />
                          </td>
                        </tr>
                        <tr>
                          <th>Hãng</th>
                          <td>
                            <select
                              v-model="product.brandname"
                              class="form-control"
                            >
                              <option
                                v-for="brand in brands"
                                :key="brand.id"
                                :value="brand.id"
                              >
                                {{ brand.brandname }}
                              </option>
                            </select>
                          </td>
                        </tr>
                        <tr>
                          <td></td>
                          <td>
                            <button class="btn btn-success" @click="editProduct(product)">Change</button>
                            <button class="btn btn-danger" @click="deleteProduct(product.productid)">Delete</button>
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
    </div>
  </div>
</template>
<script>
export default {
  middleware:  ['auth-admin'],
    head() {
    return {
      title: "Edit Product"
    };
  },
  async asyncData({ $axios, params }) {
    const product = await $axios.$get(`/products/${params.edit}`)
    const brands = await $axios.$get('/brand/')
    const preview = product.img
    return { product,brands,preview}
  },
  data() {
    return {
      preview: '',
    }
  },
  methods: {
    onFileChange(e) {
      const files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
        return;
      }
      this.product.img = files[0];
      this.createImage(files[0]);
    },
    createImage(file) {
      const reader = new FileReader();
      const vm = this;
      reader.onload = e => {
        vm.preview = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    async editProduct(product) {
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      const formData = new FormData();
      console.log(product)
      for (const data in product) {
        formData.append(data,product[data]);
      }
      try {
        await this.$axios.$post("/productadminview/",formData,config);
        this.$router.push('/admin/products/'+this.product.productcode)
        this.$notify({
            title: 'Notification',
            group: 'productadmin',
            text: 'Change Success',
          })
      } catch (e) {
      }
    },
    async deleteProduct(productid) {
      try {
        await this.$axios.$delete("/productadminview/",
          { data: { productid: productid } }
        );
        // add nofi make sure user want to delete product
        this.$router.push('/admin/products/');
      } catch (e) {
        console.log(e);
      }
    }
  }
}
</script>
