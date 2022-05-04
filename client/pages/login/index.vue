<template>
  <div class="login-form-body">
    <notifications position="top center" ignoreDuplicates width=400 height=700 group="foo" />
    <div class="login-box">
      <h2>Login</h2>
      
      <!-- <Notifi v-if="status != ''" :message="status" /> -->
      <form>
        <div class="user-box">
          <input v-model="user.username" type="text" name="" required="" />
          <label>Username</label>
        </div>
        <div class="user-box">
          <input v-model="user.password" type="password" name="" required="" />
          <label>Password</label>
        </div>
        <a @click="login()">
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
import Vue from 'vue'
import Notifi from '../../components/Notifi.vue'
export default {
  components: { Notifi },
  name: 'Login',
  layout: 'clean',

  data() {
    return {
      user: {
        username: '',
        password: '',
      },
      status: '',
    }
  },

  methods: {
    async login() {
      try {
        const response = await this.$auth.loginWith('local', {
          data: this.user,
        })
        console.log(response)
        if (this.$auth.user.is_staff) {
          this.$router.push('/admin')
          this.$notify({
            group: 'foo',
            title: 'Important message',
            text: 'Hello user! This is a notification!',
            duration: 10000
          })
          console.log(response)
        } else if (response.status === 200) {
          
          this.$router.push('/')
        }
      } catch (e) {
        console.log(e)
        if (e.response.status === 204) {
          this.status = 'Please fill all fields!'
        } else if (e.response.status === 404) {
          this.status = 'Username does not exist!'
        } else if (e.response.status === 401) {
          this.status = 'Incorrect password!'
        }
        this.$notify({
            group: 'foo',
            type:'error',
            title: 'Error',
            text: this.status,
          })
      }
      this.$nuxt.refresh()
    },
    doNotifi() {
      this.$notify({
            group: 'foo',
            type:'error',
            position:'top',
            title: 'Important message',
            text: 'Hello user! This is a notification!',
          })
    },
  },
}
</script>
