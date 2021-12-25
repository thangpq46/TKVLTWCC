<template>
  <div>
    <Header />
    <div class="app flex-row align-items-center">
      <div class="container">
        <b-row class="justify-content-center login">
          <b-col md="6">
            <b-card-group>
              <b-card no-body class="p-4">
                <b-card-body>
                  <h1>Register</h1>
                  <Notification v-if="status" :message="status" />
                  <p class="text-muted">Register your account</p>
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
                  <b-input-group class="mb-3">
                    <b-input-group-prepend>
                      <b-input-group-text
                        ><i class="icon-user"></i
                      ></b-input-group-text>
                    </b-input-group-prepend>
                    <input
                      v-model="user.email"
                      type="email"
                      class="form-control"
                      placeholder="email"
                    />
                  </b-input-group>
                  <b-input-group class="mb-3">
                    <b-input-group-prepend>
                      <b-input-group-text
                        ><i class="icon-user"></i
                      ></b-input-group-text>
                    </b-input-group-prepend>
                    <input
                      v-model="user.first_name"
                      type="text"
                      class="form-control"
                      placeholder="Firstname"
                    />
                  </b-input-group>

                  <b-input-group class="mb-3">
                    <b-input-group-prepend>
                      <b-input-group-text
                        ><i class="icon-user"></i
                      ></b-input-group-text>
                    </b-input-group-prepend>
                    <input
                      v-model="user.last_name"
                      type="text"
                      class="form-control"
                      placeholder="Lastname"
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
                  <b-input-group class="mb-4">
                    <b-input-group-prepend>
                      <b-input-group-text
                        ><i class="icon-lock"></i
                      ></b-input-group-text>
                    </b-input-group-prepend>
                    <input
                      v-model="user.rpassword"
                      type="password"
                      class="form-control"
                      placeholder="retype Password"
                    />
                  </b-input-group>

                  <b-row>
                    <b-col cols="6">
                      <b-button variant="primary" class="px-4" @click="register()"
                        >register</b-button
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
  asyncData({ redirect }) {
    // const status ='register success';
    // if(data.status==='register success'){
    //   return redirect('/login')
    // }
  },
  data() {
    return {
      user: {
        username: 'admin',
        password: '@t04062001',
        email: 'pqt4621@gmail.com',
        first_name: 'Phan Quang',
        last_name:'Thắng',
        rpassword:'@t04062001',
      },
      status: null,
    }
  },

  methods: {
    async register() {
      const response = await this.$axios.$post('register/', {
        user: this.user
      })
      this.$nuxt.refresh()
      this.status = response.status
    },
  },
}
</script>
