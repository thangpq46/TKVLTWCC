<template>
  <div class="login-form-body">
    <div class="login-box">
      <h2>Login</h2>
      <Notification v-if="status" :message="status" />
      <form>
        <div class="user-box">
          <input v-model="user.username" type="text" name="" required="" />
          <label>Username</label>
        </div>
        <div class="user-box">
          <input v-model="user.password" type="password" name="" required="" />
          <label>Password</label>
        </div>
        <a @click="login">
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          Submit
        </a>
      </form>
    </div>
  </div>
</template>

<script>
import Notification from '~/components/Notification'

export default {
  name: 'Login',
  components: {
    Notification,
  },
  layout: 'clean',

  data() {
    return {
      user: {
        username: '',
        password: '',
      },
      status: null,
    }
  },

  methods: {
    async login() {
      try {
        const response = await this.$auth.loginWith('local', {
          data: this.user,
        })
        if (this.$auth.user.is_staff) {
          this.$router.push('/admin')
        }
      } catch (e) {
        console.log(e.response.status)
        if(e.response.status==204){
          this.status = "Please fill all fields!"
        }
        else if(e.response.status==404){
          this.status = "Username does not exist!"
        }
        else if(e.response.status==401){
          this.status = "Incorrect password!"
        }
      }
      this.$nuxt.refresh()
    },
  },
}
</script>
