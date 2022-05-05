<template>
  <!-- 아이디 찾을 때 필요한 것 : 이름, 전화번호 -->
  <h2>아이디 찾기</h2>
  <div>
    <div>
      <label for="name">이름 입력</label>
      <!-- 이름 어디 쓰는지 알아보고 고칠 것임 -->
      <input type="text" id="name" v-model="idFinder.name">
    </div>
    <div>
      <label for="phonenumber">전화번호 입력</label>
      <input type="text" v-model="idFinder.phonenumber">
    </div>
    <button class="btn btn-primary m-2" @click="findId">찾기</button>
  </div>
  <div v-if="myid">
    <h5>해당 사용자의 아이디는 {{ myid }} 입니다.</h5>
  </div>
  <br>
  
  <!-- 비밀번호 찾을 때 필요한 것 : 이름, 아이디, 전화번호, 이메일 -->
  <!-- 이메일로 임시 비밀번호 날려주기? -->
  <h2>비밀번호 찾기</h2>
  <div>
    <div>
      <label for="username">아이디</label>
      <input type="text" id="username">
    </div>
    <div>
      <label for="phonenumber">전화번호</label>
      <input type="text" id="phonenumber">
    </div>
    <div>
      <label for="email">이메일</label>
      <input type="text" id="email">
    </div>
    <button class="btn btn-primary m-2" @click="findPw">찾기</button>
  </div>

</template>

<script>
import axios from 'axios';
const baseURL = 'http://127.0.0.1:8000/'

export default {
  name: 'FindinfoView',
  data() {
    return {
      idFinder:{
        name:'',
        phonenumber:''
      },
      pwFinder:{
        name:'',
        username:'',
        phonenumber:'',
        email:''
      },
      myid:''
    }
  },
  methods: {
    findId: function() {
      console.log(this.idFinder)
      axios({
        methods: 'get',
        url: `${baseURL}accounts/username/`,
      })
      .then(res => {
        console.log(res.data)
        for (let info in res.data) {
          console.log(res.data[info])
          if (res.data[info].first_name == this.idFinder.name) {
            console.log(res.data[info].username)
            console.log(res.data[info].email)
            this.myid = res.data[info].username
          }
        }
      })
      .catch(err => {
        console.log(err)
        alert(err)
      })
    },
    findPw: function() {}
  }

}
</script>

<style>

</style>