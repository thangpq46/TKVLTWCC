<template>
  <div>
    <div><input type="text"  :value='$auth.user.username' disabled></div>
    <div>
      <input id="useremail" type="email" :value='$auth.user.email' disabled>
      <button type="button" @click="usereditinfo('useremail')">Chỉnh sửa</button>
    </div>
  </div>
</template>
<script>

export default{
// asyncData({ auth}){
//     const user = auth.user;
//     return user
// },
  data() {
    return {
      user: {
        username:'',
        first_name: '',
        last_name: '',
        email: '',
        img: '',
      },
    }
  },
    methods: {
        usereditinfo(typeinfo){
            document.getElementById(typeinfo).disabled = false;
        }
    }
}
</script>
