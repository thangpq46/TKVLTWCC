<template>
  <div>
    <Header/>
    <div class="app flex-row align-items-center">
      <div class="container">
        <b-row class="justify-content-center login">
          <b-col md="6">
            <b-card-group>
              <b-card no-body class="p-4">
                <b-card-body>
                  <h1>Login</h1>
                  <Notification v-if="error" :message="error" />
                  <p class="text-muted">Sign In to your account</p>
                  <b-input-group class="mb-3">
                    <b-input-group-prepend>
                      <b-input-group-text
                        ><i class="icon-user"></i
                      ></b-input-group-text>
                    </b-input-group-prepend>
                    <input
                      v-model="user.username"
                      type="text"
                      class="form-control"
                      placeholder="username"
                    />
                  </b-input-group>

                  <b-input-group class="mb-4">
                    <b-input-group-prepend>
                      <b-input-group-text
                        ><i class="icon-lock"></i
                      ></b-input-group-text>
                    </b-input-group-prepend>
                    <input
                      v-model="user.password"
                      type="password"
                      class="form-control"
                      placeholder="Password"
                    />
                  </b-input-group>

                  <b-row>
                    <b-col cols="6">
                      <b-button variant="primary" class="px-4" @click="login"
                        >Login</b-button
                      >
                    </b-col>
                  </b-row>
                </b-card-body>
              </b-card>
            </b-card-group>
          </b-col>
        </b-row>
      </div>
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
        username: 'admin',
        password: '@t04062001',
      },
      error: null,
    }
  },

  methods: {
    async login() {
      const response = await this.$auth.loginWith('local', { data: this.user })
      this.$auth.$storage.setUniversal('username', response.data.username)
      console.log(response)
    },
  },
}
</script>
