<template>
  <div>
    <div class="login-form-body">
      <div class="login-box">
        <h2>Register</h2>
        <notifications position="top center" ignoreDuplicates width=400 height=700 group="foo" />
        <!-- <Notifi v-if="status!=''" :message="status" /> -->
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
export default {
  auth: 'guest',
  name: 'Login',
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
      status: "",
    }
  },

  methods: {
    async register() {
      try {
        const response = await this.$axios.post('register/', {
          user: this.user,
        })
        if (response.status == 201) {
          this.$router.push('/login/')
        }
      } catch (e) {
        console.log(e.status)
        if (e.response.status == 409) {
          this.status = 'Username or Email already exist!'
        } else if (e.response.status == 428) {
          this.status = 'Password not strong enough!'
        } else if (e.response.status == 204) {
          this.status = 'You must fill all the fields!'
        } else if (e.response.status == 510) {
          this.status = 'Password not Match!'
        }
        this.$notify({
            group: 'foo',
            type:'error',
            title: 'Error',
            text: this.status,
          })
      }
    },
  },
}
</script>
