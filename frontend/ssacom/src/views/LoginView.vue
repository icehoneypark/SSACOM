<template>
  <h2>로그인</h2>
  <div>
    <div>
      <label for="username">이름</label>
      <input type="text"
        id="username"
        v-model="content.username"
      >
    </div>
  </div>
  <div>
    <div>
      <label for="password">비번</label>
      <input type="password"
        id="password"
        v-model="content.password"
        @keyup.enter="login"
        autocomplete="off"
      >
    </div>
  </div>
  <button class="btn btn-sm btn-primary m-1" @click="login">로그인</button>



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

</style>