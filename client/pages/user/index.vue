<template>
  <div>
    <div>
        {{user}}
      <span><img :src="$auth.user.img"></span>
      <button type="button" @click="changelastname">Chỉnh sửa</button>
    </div>
    <div><input type="text" v-model="$auth.user.username" disabled></div>
    <div>
      <input id="useremail" type="email" v-model="$auth.user.email" disabled>
      <button type="button" @click="usereditinfo('useremail')">Chỉnh sửa</button>
    </div>
    <div>
      <span>Firstname: {{ $auth.user.first_name }}</span>
      <button type="button" @click="changefirstname">Chỉnh sửa</button>
    </div>
    <div>
      <span>Firstname: {{ $auth.user.last_name }}</span>
      <button type="button" @click="changelastname">Chỉnh sửa</button>
    </div>
        <div>
      <span>Password: {{ $auth.user.last_name }}</span>
      <button type="button" @click="changelastname">Đổi Mật Khẩu</button>
    </div>
  </div>
</template>
<script>

export default{
asyncData({ auth}){
    const user = auth.user;
    return user
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
    }
  },
    methods: {
        usereditinfo(typeinfo){
            document.getElementById(typeinfo).disabled = false;
        }
    }
}
</script>
