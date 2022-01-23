<template>
  <div class="login-form-body">
    <div class="login-box">
      <h2>Login</h2>
      <Notification v-if="error" :message="error" />
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
      error: null,
    }
  },

  methods: {
    async login() {
      try {
        const response = await this.$auth.loginWith('local', {
          data: this.user,
        })
        this.$auth.$storage.setUniversal('username', response.data.username)
        if (this.$auth.user.is_staff) {
          this.$router.push('/admin')
        }
      } catch (e) {
        this.error = 'Incored Username or Password'
      }
    },
  },
}
</script>
