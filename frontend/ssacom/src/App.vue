<template>
<<<<<<< HEAD
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/login">Login</router-link> |
    <router-link to="/dashboard">Dashboard</router-link>
  </nav>
=======
  <NavBar />

>>>>>>> develop
  <router-view/>
</template>

<script>
import NavBar from "./components/NavBar.vue"

export default {
  components: {NavBar},

  setup() {
    
  },
}
</script>

<style>

</style>
