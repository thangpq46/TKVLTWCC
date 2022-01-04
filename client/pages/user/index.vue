<template>
  <div>
    {{ user.user }}
    <div>{{ user.username }}</div>
    <button
      v-if="isediting === false"
      type="button"
      @click="usereditinfo('useremail')"
    >
      Chỉnh sửa
    </button>
    <button v-else type="button" @click="submituser()">Lưu</button>
    <div>
      <img :src="preview" />
      <input v-if="isediting === true" type="file" @change="onFileChange" />
      <input type="email" v-model="user.email" :disabled="!isediting" />
      <input type="text" v-model="user.first_name" :disabled="!isediting" />
      <input type="text" v-model="user.last_name" :disabled="!isediting" />
    </div>
    <div>
      <span v-if="status != ''">{{status}}</span>
      <button type="button" @click="changepassword">Đổi Mật Khẩu</button>
      <input type="text" v-model="password">
      <input type="text" v-model="new_password">
      <input type="text" v-model="rnew_password">
    </div>
  </div>
</template>
<script>
export default {
  async asyncData({ $axios }) {
    let user = await $axios.$get('/user/')
    user = user.user
    const preview = user.img
    return { user, preview }
  },
  data() {
    return {
      user: {
        username: '',
        first_name: '',
        last_name: '',
        email: '',
        img: '',
      },
      password:'',
      new_password: '',
      rnew_password: '',
      preview: '',
      status: '',
      isediting: false,
    }
  },
  methods: {
    onFileChange(e) {
      const files = e.target.files || e.dataTransfer.files
      if (!files.length) {
        return
      }
      this.user.img = files[0]
      this.createImage(files[0])
    },
    createImage(file) {
      const reader = new FileReader()
      const vm = this
      reader.onload = (e) => {
        vm.preview = e.target.result
      }
      reader.readAsDataURL(file)
    },
    usereditinfo() {
      this.isediting = !this.isediting
    },
    async submituser() {
      const config = {
        headers: { 'content-type': 'multipart/form-data' },
      }
      const formData = new FormData()
      for (const data in this.user) {
        formData.append(data, this.user[data])
      }
      try {
        await this.$axios.$post('/updateuser/', formData, config)
        this.usereditinfo()
      } catch (e) {}
    },
    async changepassword(){
            const config = {
        headers: { 'content-type': 'multipart/form-data' },
      }
      const formData = new FormData()
        formData.append('password', this.password)
        formData.append('new_password', this.new_password)
        formData.append('rnew_password', this.rnew_password)
      const response= await this.$axios.$post('/changepass/',formData,config)
      this.status = response.status;
    }
  },
}
</script>
