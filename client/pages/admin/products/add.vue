<template>
    <div>
      <div>
        <img :src="preview">
        <input type="file" @change="onFileChange">
        <input v-model="product.productcode" type="text">
        <input v-model="product.name" type="text">
        <input v-model="product.price" type="number">
        <input v-model="product.description" type="text">
        <input v-model="product.stock" type="number">

        <select v-model="product.brandname">
                  <option v-for="brand in brands" :key='brand.id' :value="brand.id">{{brand.brandname}}</option>
                  <!-- <option value="Medium">Medium</option>
                  <option value="Hard">Hard</option> -->
        </select>
        <button @click="submitProduct">Add</button>
      </div>
    </div>
</template>

<script>
export default {
    async asyncData({ $axios}){
      const brands = await $axios.$get('/brand/')
      return {brands}
    },  
    data() {
    return {
      product: {
        productcode:"",  
        name: "",
        img: "",
        price: "",
        description: "",
        stock: "",
        brandname: "",
        type:'+'
      },
      preview: ""
    };
  },
  head() {
    return {
      title: "Add Product"
    };
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
    async submitProduct() {
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      const formData = new FormData();
      for (const data in this.product) {
        formData.append(data, this.product[data]);
      }
      try {
        await this.$axios.$put("/productadminview/",formData,config);
        this.$router.push('/admin/products/')
      } catch (e) {
      }
    }
  }
};
</script>

<style scoped>
</style>