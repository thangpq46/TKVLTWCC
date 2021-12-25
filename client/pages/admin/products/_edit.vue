<template>
  <div>
    <div>{{product}}</div>
    <div>
        <img :src="product.img">
        <div>
            <input v-model="product.productcode" type="text" >
            <input v-model="product.name" type="text" >
            <input v-model="product.description" type="text" >
            <input v-model="product.stock" type="textarea" >
            <input v-model="product.brandname" type="text" >
            <input type="file" name="file" @change="onFileChange">
            <button @click="editproduct">Change</button>
        </div>
    </div>
    <span>{{product}}</span>
  </div>
</template>
<script>
export default {
  async asyncData({ $axios, params }) {
    const product = await $axios.$get(`/products/${params.edit}`)
    return { product }
  },
  data() {
    return {
      product: {
        productcode: '',
        name: '',
        price: '',
        img: '',
        description: '',
        brand: '',
      },
      fileselected: null,
      status: 'no error',
      preview: ''
    }
  },
  methods: {
    onFileChange(e) {
      const files = e.target.files || e.dataTransfer.files;
      console.log(files[0])
      if (!files.length) {
        return;
      }
      this.product.img = files[0];
      this.createImage(files[0]);
    },
    createImage(file) {
      // let image = new Image();
      const reader = new FileReader();
      const vm = this;
      reader.onload = e => {
        vm.preview = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    async editproduct() {
      this.product.img =this.fileselected
      await this.$axios.post('adminproductsview/')
    }
  },
}
</script>
