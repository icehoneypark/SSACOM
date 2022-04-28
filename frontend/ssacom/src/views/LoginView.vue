<template>
  <h3>loginpage</h3>
  <div>
    <input-group>
      <input-text>이메일</input-text>
      <input type="text">
    </input-group>
  </div>
  <div>
    <input-group>
      <input-text>비번</input-text>
      <input type="text">
    </input-group>
  </div>
  <button type="submit" class="btn btn-sm btn-primary m-1">로그인</button>



</template>

<script>
import axios from 'axios';
import EmailValidator from "email-validator";
import { assertExpressionStatement } from "@babel/types";
const baseURL = 'http://localhost:8000/'

export default {
  name: 'LoginView',
  data() {
    return {
      credentials:{
        email:'',
        password:''
      },
      isCheck:false,
      isAlert:false,

    }
  },
  components:{},
  created() {},
  watch : {
    email: function() {
      this.email = this.email.trim().toLowerCase(); //대문자 방지
    }
  },
  methods: {
    login: function() {
      axios({
        method: 'post',
        url: "accounts/login/", 
        data: this.credentials
      })
      .then(res => {
        if (res.data.Success){
          if (res.data.is_active) {
            this.$store.dispatch('login', this.credentials)
            this.$emit('login')
            if(this.$route.path!=='/Home') this.$router.push('/')
          }else{
            alert('관리자의 승인을 기다려주세요.')
          }
        }else{
          alert(res.data.error)
        }
      })
      .catch(err => {
        alert(err.response.data)
      })
    }
  }


}
</script>

<style>

</style>