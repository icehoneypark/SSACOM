<template>
  <nav>
    <!-- 로그인 -->
    <ul v-if="isLogin">
      <li><a href="/"><img src="../assets/logo.png" alt="x" width="30"></a></li>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/about">About</router-link></li>
      <li><router-link to="/mypage">MyPage</router-link></li>
      <li><router-link to="/dashboard">DashBoard</router-link></li>
      <li><a href="" @click="logout">logout</a></li>
    </ul>
    <!-- 비로그인 -->
    <ul v-if="!isLogin">
      <li><a href="/"><img src="../assets/logo.png" alt="x" width="30"></a></li>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/login">로그인</router-link></li>
      <li><router-link to="/signup">회원가입</router-link></li>
    </ul>
  </nav>
</template>

<script>
import { useStore } from "vuex"
import { computed } from 'vue'



export default {
  setup() {
    const store = useStore();
    const isLogin = computed(() => store.state.isLogin);
    console.log(store.state);

    const logout = (e) => {
      e.preventDefault()
      localStorage.removeItem('jwt')
      alert('로그아웃되었습니다.')
      store.dispatch('logout')
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
    padding: 30px;
    border-bottom: 1px solid gray;
    
    a {
      float: left
    }

    ul {
      list-style: none;

      li {
        float: left;
        margin-left: 20px;
        // 비활성화  탭
        a {
          text-decoration: none;
          font-weight: bold;
          color: #2c3e50;
        }
        // 활설화 탭
        a.router-link-exact-active{
          color: #42b983;
        }
      }
    }
  }

</style>