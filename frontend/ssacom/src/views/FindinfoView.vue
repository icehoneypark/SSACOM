<template>
  <div class="container-fluid px-5 pt-5" style="width:30rem">
    <div class="d-flex justify-content-center">
      <div class="row">
        <!-- 아이디 찾을 때 필요한 것 : 이름, 전화번호 -->
        <h2 class="d-flex justify-content-center my-3">아이디 찾기</h2>
        <div>
          <div class="input-group">
            <span class="input-group-text">이름</span>
            <!-- <label for="name">이름 입력</label> -->
            <!-- 이름 어디 쓰는지 알아보고 고칠 것임 -->
            <input type="text" class="form-control" v-model="idFinder.fullname">
          </div>
          <div class="input-group">
            <span class="input-group-text">전화번호</span>
            <!-- <label for="phonenumber">전화번호 입력</label> -->
            <input type="text" class="form-control" v-model="idFinder.phonenumber">
          </div>
          <div>
            <button style="width:100%;" class="btn btn-primary mt-1 mb-3" @click="findId">아이디 찾기</button>
          </div>
          
        </div>
        <div v-if="myid">
          <h5>해당 사용자의 아이디는 {{ myid }} 입니다.</h5>
        </div>
        <hr>
        <!-- 비밀번호 찾을 때 필요한 것 : 이름, 아이디, 전화번호, 이메일 -->
        <!-- 이메일로 임시 비밀번호 날려주기? -->
        <h2 class="d-flex justify-content-center mt-5 mb-3">비밀번호 찾기</h2>
        <div>
          <div class="input-group">
            <span class="input-group-text">아이디</span>
            <!-- <label for="username">아이디</label> -->
            <input type="text" id="username" class="form-control">
          </div>
          <div class="input-group">
            <span class="input-group-text">전화번호</span>
            <!-- <label for="phonenumber">전화번호</label> -->
            <input type="text" id="phonenumber" class="form-control">
          </div>
          <div class="input-group">
            <span class="input-group-text">이메일</span>
            <!-- <label for="email">이메일</label> -->
            <input type="text" id="email" class="form-control">
          </div>
          <button style="width:100%" class="btn btn-primary my-1" @click="findPw">비밀번호 찾기</button>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { reactive } from '@vue/reactivity';
const baseURL = 'http://127.0.0.1:8000/'

export default {
  name: 'FindinfoView',
  setup() {
    const idFinder = reactive({
      fullname:'',
      phonenumber:''
    })
    const pwFinder = reactive({
      fullname:'',
      username:'',
      phonenumber:'',
      email:''
    })
    const findId = (e) => {
      e.preventDefault()
      const idInfo = {
        fullname: idFinder.fullname,
        phonenumber: idFinder.phonenumber,
      }
      axios({
        methods: 'get',
        url: `${baseURL}accounts/username/`,
      })
      .then(res => {
        console.log(res.data)
        for (let info in res.data) {
          console.log(res.data[info])
          if (res.data[info].phonenumber == idInfo.phonenumber) {
            console.log(res.data[info].fullname)
            console.log(res.data[info].email)
            this.myid = res.data[info].username
          }
        }
      })
      .catch(err => {
        console.log(err)
        alert(err)
      })
    }

    return { idFinder, pwFinder, findId}
  },
  // data() {
  //   return {
  //     idFinder:{
  //       name:'',
  //       phonenumber:''
  //     },
  //     pwFinder:{
  //       name:'',
  //       username:'',
  //       phonenumber:'',
  //       email:''
  //     },
  //     myid:''
  //   }
  // },
  methods: {
    // findId: function() {
    //   console.log(this.idFinder)
    //   axios({
    //     methods: 'get',
    //     url: `${baseURL}accounts/username/`,
    //   })
    //   .then(res => {
    //     console.log(res.data)
    //     for (let info in res.data) {
    //       console.log(res.data[info])
    //       if (res.data[info].first_name == this.idFinder.name) {
    //         console.log(res.data[info].username)
    //         console.log(res.data[info].email)
    //         this.myid = res.data[info].username
    //       }
    //     }
    //   })
    //   .catch(err => {
    //     console.log(err)
    //     alert(err)
    //   })
    // },
    findPw: function() {}
  }

}
</script>

<style>

span {
  width: 6rem;
}

</style>