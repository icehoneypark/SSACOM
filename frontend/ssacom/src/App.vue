<template>
  <div style="float: left;">
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
