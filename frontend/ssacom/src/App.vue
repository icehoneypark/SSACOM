<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/notice">Notice</router-link>
    <router-link to="/login">Login</router-link>
  </nav>
  <NavBar />

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
