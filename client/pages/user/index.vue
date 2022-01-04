<template>
  <div>
    {{user.user}}
    <div>{{user.username}}</div>
    <button v-if="isediting===false" type="button" @click="usereditinfo('useremail')">Chỉnh sửa</button>
    <button v-else type="button" @click="usereditinfo('useremail')">Lưu</button>
    <div>
      <input id="useremail" type="email" v-model='user.email' :disabled="isediting">
      
      
    </div>
    
  </div>
</template>
<script>

export default{
  async asyncData({$axios}){
    let user = await $axios.$get('/user/')
    user = user.user
    return { user}
  },
  data() {
    return {
      user: {
        username:'',
        first_name: '',
        last_name: '',
        email: '',
        img: '',
      },
      isediting: false,
    }
  },
    methods: {
        usereditinfo(){
            this.isediting = !this.isediting;
        },

    }
}
</script>
