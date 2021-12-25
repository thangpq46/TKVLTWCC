<template>
    <div>
      <div>
        <img :src="preview">
        <input type="file" @change="onFileChange">
        <input v-model="product.productcode" type="text">
        <input v-model="product.name" type="text">
        <input v-model="product.price" type="text">
        <input v-model="product.description" type="text">
        <input v-model="product.stock" type="text">
        <input v-model="product.brandname" type="text">
        <button @click="submitProduct">Add</button>
      </div>
    </div>
</template>

<script>
export default {
    data() {
    return {
      product: {
        productcode:"3",  
        name: "3",
        img: "",
        price: "3",
        description: "3",
        stock: "3",
        brandname: "3"
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
        
        const response = await this.$axios.$post("/adminproduct/",formData,config);
        console.log(response);
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style scoped>
</style>