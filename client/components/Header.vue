<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container g-0">
      <a
        class="navbar-brand btn btn-outline-success"
        href="http://localhost:3000"
        >QT Store</a
      >
    </div>
    <div v-if="$auth.loggedIn">
      <div>Wellcome {{ $auth.user.username }}</div>
      <NuxtLink to="/">Logout</NuxtLink>
    </div>
    <div v-else>
      <NuxtLink to="/login">Login</NuxtLink>
      <NuxtLink to="/register">Register</NuxtLink>
    </div>
  </nav>
</template>
