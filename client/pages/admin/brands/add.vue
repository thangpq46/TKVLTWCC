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
                  >Add Brand</span
                >
              </div>
              <div class="col-12 mg-top-20">
                <div class="row justify-content-center">
                  <div class="col-md-11 col-12 bg-white bd-rd-5 mg-bottom-20">
                   
                    <table class="table ">
                      <tr>
                        <th>Hình ảnh</th>
                        <td>
                          <img :src="preview" height="100px" width="150px"/>
                          <input type="file" accept="image/png, image/jpeg" @change="onFileChange" />
                        </td>
                      </tr>
                      <tr>
                        <th>Tên Hãng </th>
                        <td>
                          <input
                            v-model="brand.brandname"
                            type="text"
                            class="form-control"
                          />
                        </td>
                      </tr>
                      <tr>
                        <th>Mô Tả</th>
                        <td>
                          <input
                            v-model="brand.branddes"
                            type="text"
                            class="form-control"
                          />
                        </td>
                      </tr>
                      <tr>
                        <td></td>
                        <td>
                          <button class="btn btn-success" @click="submitBrand">Add</button>
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
    data() {
    return {
      brand: {
        brandname:"",  
        branddes: "",
        img: "",
      },
      preview: ""
    };
  },
  head() {
    return {
      title: "Add Brands"
    };
  },
  methods: {
    onFileChange(e) {
      const files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
        return;
      }
      this.brand.img = files[0];
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
    async submitBrand() {
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      const formData = new FormData();
      for (const data in this.brand) {
        formData.append(data, this.brand[data]);
      }
      try {
        const response= await this.$axios.$put("/adminbrand/",formData,config);
        if(response.status===202){
            // ĐÃ THÀNH CÔNG-> CHUYỂN HƯỚNG VỀ TRANG HÃNG
            alert("Success!")
        }
      } catch (e) {
          if(e.response.status===409){
            //   Tên Hãng đã tồn tại
            alert("Brand name already exists!")
          }
      }
    }
  }
};
</script>