<template>
  <div>
    <div class="login-form-body">
      <div class="login-box">
        <h2>Register</h2>
        <Notification v-if="status" :message="status" />
        <form>
          <div class="user-box">
            <input v-model="user.username" type="text" name="" required />
            <label>Username</label>
          </div>
          <div class="user-box">
            <input v-model="user.email" type="email" name="" required />
            <label>Email</label>
          </div>
          <div class="user-box">
            <input v-model="user.first_name" type="text" name="" required />
            <label>Firstname</label>
          </div>
          <div class="user-box">
            <input v-model="user.last_name" type="text" name="" required />
            <label>Lastname</label>
          </div>
          <div class="user-box">
            <input
              v-model="user.password"
              type="password"
              name=""
              required=""
            />
            <label>Password</label>
          </div>
          <div class="user-box">
            <input
              v-model="user.rpassword"
              type="password"
              name=""
              required=""
            />
            <label>Retype Password</label>
          </div>
          <a @click="register()">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            Submit
          </a>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import Notification from '~/components/Notification'

export default {
  auth: 'guest',
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
        email: '',
        first_name: '',
        last_name: '',
        rpassword: '',
      },
      status: null,
    }
  },

  methods: {
    async register() {
      const response = await this.$axios.post('register/', {
      user: this.user,
      })
      if (response.status==201){
        this.$router.push('/login/')
      }
      else if (response.status==409){
          //trurng username or email
      }
      else if (response.status==428){
          // mk qua yeu
      }
      else if (response.status==510){
          //mk khong trung
      }
      // this.$nuxt.refresh()
      // this.status = response.status
      // if (this.status === 'register success') {
      //   this.$router.push('/login/')
      // }
    },
  },
}
</script>
