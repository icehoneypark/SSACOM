<template>
  <div class="container-fluid px-5" style="width:30rem">
    <div class="d-flex justify-content-center">
      <div class="row">
        <h2 class="d-flex justify-content-center my-3">로그인</h2>
        <div>
          <div class="input-group">
            <span class="input-group-text">아이디</span>
            <!-- <label for="username">아이디</label> -->
            <input type="text"
              class="form-control"
              v-model="content.username"
            >
          </div>
          <div class="input-group">
            <span class="input-group-text">비밀번호</span>
            <!-- <label for="password">비밀번호</label> -->
            <input type="password"
              class="form-control"
              v-model="content.password"
              @keyup.enter="login"
              autocomplete="off"
            >
          </div>          
        </div>
        <!-- login 버튼 -->
        <div>
          <button style="width:100%;" class="btn btn-primary my-1" @click="login">로그인</button>
        </div>
        <!-- 아이디/비밀번호 찾는 페이지 -->
        <div class="d-flex justify-content-end">
          <a href="/findinfo">아이디/비밀번호가 기억나지 않으세요?</a>
        </div>
      </div>
    </div>
  </div>

  



</template>

<script>
import axios from 'axios';
import { useStore } from "vuex"

const baseURL = 'http://127.0.0.1:8000/'

export default {
  name: 'LoginView',
  data() {
    return {
      content:{
        username:'',
        password:''
      },
      isCheck:false,
      isAlert:false,
      store: useStore()
    }
  },
  watch : {
    email: function() {
      this.email = this.email.trim().toLowerCase(); //대문자 방지
    }
  },
  methods: {
    login: function() {
      axios({
        method: 'post',
        url: `${baseURL}accounts/api-token-auth/`, 
        data: this.content
      })
      .then(res => {
        console.log(res)

        // const store = useStore()
        // store.dispatch('login')
        localStorage.setItem('jwt', res.data.token)
        this.$router.push({ name : 'mypage' })
        this.store.dispatch('login')
        // if (res.data.Success){
        //   if (res.data) {
        //     console.log('여기는 then')
        //     console.log(this.content)
        //     this.$store.dispatch('login', this.content)
        //     this.$emit('login')
        //     if(this.$route.path!=='/Home') this.$router.push('/') // 나중에 대시보드로 바꿔야지.
        //   }else{
        //     alert('등록되지 않은 계정입니다.')
        //   }
        // }else{
        //   alert(res.data.error)
        //   console.log('이거는 어디지')
        // }
      })
      .catch(err => {
        alert(err)
        console.log('여기는 캐치 에러')
      })
    }
  },
  created: function(){
    const token = localStorage.getItem('jwt')
    if (token){
      if (this.$route.path!=='/Home') this.$router.push('/')
    }
  }
}
</script>

<style>
span {
  width: 6rem;
}

</style>