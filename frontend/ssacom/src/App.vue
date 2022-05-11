<template>
  <div class="nav">
    <nav-bar />
  </div>
  <div class="router">
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

<style lang="scss" scoped>
  .nav {
    float: left; 
    height:100vh;
    width: 15vw;
  }
  
  .router {
    margin-left: 15vw; 
    width:85vw;
    height: 100vh;
    overflow: auto;
  }
</style>
