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
                  >Edit Brand</span
                >
              </div>
              <div class="col-12 mg-top-20">
                <div class="row justify-content-center">
                  <div class="col-md-11 col-12 bg-white bd-rd-5 mg-bottom-20">
                    
                      <table class="table ">

                        <tr>
                          <th>Hình ảnh</th>
                          <td>
                            <img :src="preview" height="100px" width="150px" />
                            <input type="file" @change="onFileChange" />
                          </td>
                        </tr>
                        <tr>
                          <th>Tên Hãng</th>
                          <td>
                            <input
                              v-model="brand.brandname"
                              type="text"
                              class="form-control"
                            />
                          </td>
                        </tr>
                        <tr>
                          <th>Thông Tin Hãng</th>
                          <td>
                            <textarea
                              class="form-control"
                              v-model="brand.branddes"
                              name=""
                              id=""
                              cols="30"
                              rows="10"
                            ></textarea>
                          </td>
                        </tr>
                        <tr>
                          <td></td>
                          <td>
                            <button class="btn btn-success" @click="editBrand(brand)">Change</button>
                            <button class="btn btn-danger" @click="deleteBrand(brand.id)">Delete</button>
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
      title: "Edit Brand"
    };
  },
  async asyncData({ $axios, params }) {
    const brand = await $axios.$get(`/brand/${params.edit}`)
    const brands = await $axios.$get('/brand/')
    const preview = brand.img
    return { brand,brands,preview}
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
    async editBrand(brand) {
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      const formData = new FormData();
      for (const data in brand) {
        formData.append(data,brand[data]);
      }
      try {
        await this.$axios.$post("/adminbrand/",formData,config);
      } catch (e) {
      }
    },
    async deleteBrand(brandid) {
      try {
        await this.$axios.$delete("/adminbrand/",
          { data: { brandid } }
        );
        // add nofi make sure user want to delete product
      } catch (e) {
        console.log(e);
      }
    }
  }
}
</script>
