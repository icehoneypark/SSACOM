<template>
  <nav>
    <!-- 상단 로고를 어떻게 해야할지.. -->
    <router-link to="/dashboard"><button class="btn btn-danger">SSACOM X 에스원</button></router-link>
    <br><br>
    <!-- 로그인 -->
    <ul v-if="isLogin">
      <router-link to="/notice"><div class="nav_link"><i class="fa-solid fa-bullhorn"></i><span> Notice</span></div></router-link>
      <hr>
      <router-link to="/dashboard"><div class="nav_link"><i class="fa-solid fa-chart-line"></i><span> DashBoard</span></div></router-link>
      <router-link to="/mypage"><div class="nav_link"><i class="fa-solid fa-user"></i><span> MyPage</span></div></router-link>
      <hr>
      <router-link to="/faq"><div class="nav_link"><i class="fa-solid fa-circle-question"></i><span> FAQ</span></div></router-link>
      <router-link to="/qna"><div class="nav_link"><i class="fa-brands fa-quora"></i><span> QnA</span></div></router-link>
    </ul>
    <!-- 비로그인 -->
    <ul v-if="!isLogin">
      <router-link to="/notice"><div class="nav_link"><i class="fa-solid fa-bullhorn"></i><span> Notice</span></div></router-link>
      <hr>
      <router-link to="/login"><div class="nav_link"><i class="fa-solid fa-key"></i><span> 로그인</span></div></router-link>
      <router-link to="/signup"><div class="nav_link"><i class="fa-solid fa-user-plus"></i><span>회원가입</span></div></router-link>
    </ul>
    <ul class="user">
      <a href="" @click="logout"><div class="nav_link"><i class="fa-solid fa-right-to-bracket"></i> <span>logout</span></div></a>
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
  @media screen and (max-width: 1100px) { 
    span { display: none; } 
  }

  nav {
    // position: fixed;
    width: 100%;
    padding: 30px;
    // border-right: 1px solid gray;
    height: 100%;
    background-color: #0C4DA2;
    overflow: auto;

    ul {
      list-style: none;
      padding: 0px;
      margin-top: 20px;
      // 비활성화  탭
      a {
        text-decoration: none;
        font-weight: bold;
        color: rgb(206, 206, 206);
        .nav_link {
          transition: all 0.4s;
          padding: 5px;
          margin-bottom: 15px;
          border-radius: 15px;
          width: 100%;
          i {
            margin-right: 15px;
          }
        }

        .nav_link:hover {
          color: white;
          background-color: #1e62b9;
          box-shadow: 5px 5px 5px black;
        }
      }

      // 활설화 탭
      a.router-link-exact-active{
        color: white;
        .nav_link {
          background-color: #2376e2;
          padding: 5px;
          margin-bottom: 15px;
          width: 100%;
        }
      }
    }

    .user {
      border-radius: 15px;
      position:fixed;
      bottom:15px;
    }
  }

</style>