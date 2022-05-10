<template>
  <div style="float: left; height:100vh">
    <nav-bar />
  </div>
  <div style="float: left;">
    <router-view/>
  </div>
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
