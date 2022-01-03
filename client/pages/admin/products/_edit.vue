<template>
  <div>
    <div>
      <img :src="preview" />
      <input type="file" @change="onFileChange" />
      <input v-model="product.productcode" type="text" />
      <input v-model="product.name" type="text" />
      <input v-model="product.price" type="number" />
      <input v-model="product.description" type="text" />
      <input v-model="product.stock" type="number" />
      <select v-model="product.brandname">
        <option v-for="brand in brands" :key="brand.id" :value="brand.id">
          {{ brand.brandname }}
        </option>
      </select>
      <button @click="editProduct">Change</button>
      <button @click="deleteProduct">Delete</button>
    </div>
  </div>
</template>
<script>
export default {
  async asyncData({ $axios, params }) {
    const product = await $axios.$get(`/products/${params.edit}`)
    const brands = await $axios.$get('/brand/')
    const preview = product.img
    return { product,brands,preview}
  },
  data() {
    return {
      product: {
        id:'',
        productcode: '',
        name: '',
        price: '',
        img: '',
        description: '',
        brand: '',
      },
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
    async editProduct() {
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      const formData = new FormData();
      for (const data in this.product) {
        formData.append(data, this.product[data]);
      }
      try {
        await this.$axios.$post("/productadminview/",formData,config);
        this.$router.push('/admin/products/'+this.product.productcode)
      } catch (e) {
      }
    },
    async deleteProduct() {
      try {
        await this.$axios.$delete("/productadminview/",
          { data: { productid: this.product.id } }
        );
        this.$router.push('/admin/products/');
      } catch (e) {
        console.log(e);
      }
    }
  }
}
</script>
