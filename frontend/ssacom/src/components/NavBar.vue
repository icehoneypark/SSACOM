<template>
  <nav>
    <!-- 로그인 -->
    <router-link to="/dashboard"><button class="btn btn-danger">SSACOM</button></router-link>
    <ul v-if="isLogin">
      <li><router-link to="/notice"><i class="fa-solid fa-bullhorn"></i> Notice</router-link></li>
      <li><router-link to="/mypage">MyPage</router-link></li>
      <li><router-link to="/dashboard">DashBoard</router-link></li>
      <li><a href="" @click="logout">logout</a></li>
    </ul>
    <!-- 비로그인 -->
    <ul v-if="!isLogin">
      <li><router-link to="/notice"><i class="fa-solid fa-bullhorn"></i> Notice</router-link></li>
      <li><router-link to="/login"><i class="fa-solid fa-key"></i> 로그인</router-link></li>
      <li><router-link to="/signup"><i class="fa-solid fa-right-to-bracket"></i> 회원가입</router-link></li>
    </ul>
    <ul class="user">
      <li>1번</li>
      <li>2번</li>
    </ul>
  </nav>
</template>

<script>
import { useStore } from "vuex"
import { useRouter } from "vue-router"
import { computed } from 'vue'



export default {
  setup() {
    const store = useStore();
    const router = useRouter();
    const isLogin = computed(() => store.state.isLogin);
    console.log(store.state);

    const logout = (e) => {
      const token = localStorage.getItem('jwt')
      e.preventDefault()
      if(token){
        localStorage.removeItem('jwt')
        store.dispatch('logout')
        router.push({ name: "login" })
        alert('로그아웃되었습니다.')
      }else{
        alert('잘못된 접근입니다.')
      }
    }

    return {logout, isLogin}
  }
}
</script>

<style lang="scss" scoped>
  // #app {
  // font-family: Avenir, Helvetica, Arial, sans-serif;
  // -webkit-font-smoothing: antialiased;
  // -moz-osx-font-smoothing: grayscale;
  // text-align: center;
  // color: #2c3e50;
  // }

  nav {
    width: 15rem;
    padding: 30px;
    border-right: 1px solid gray;
    height: 100%;
    background-color: #0C4DA2;
    // a {
    //   float: left
    // }

    ul {
      list-style: none;
      padding: 0px;
      margin-top: 20px;
      li {
        margin-bottom: 15px;
        width: 100%;
        // 비활성화  탭
        a {
          text-decoration: none;
          font-weight: bold;
          color: white;
        }
        // 활설화 탭
        a.router-link-exact-active{
          color: #8cf7c7;
        }
      }
    }

    .user {
      border-radius: 5px;
      background-color: white;
      position:fixed;
      bottom:15px;
      width: 100%;
    }
  }

</style>