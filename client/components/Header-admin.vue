<template>
  <div>
    <div class="section header-adm">
      <div class="container-fluid">
        <div class="row align-items-center row-top-adm">
          <div class="col-12 dp-flex">
            <div class="logo-adm">
              <i class="bi bi-person-square"></i>
              <NuxtLink to="/admin">
                <span>Admin</span>
              </NuxtLink>
            </div>
            <div class="logout-adm mg-right-20">
              <a class="cursor-poin" @click="logout">
                <i class="bi bi-box-arrow-right"></i>
                <span>Logout</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  methods: {
    async logout() {
      await this.$auth.logout(/* .... */)
      window.localStorage.clear()
      // console.log($cookies.keys());
    },
  }
  
}
</script>