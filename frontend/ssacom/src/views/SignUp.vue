<template>
  <div class="page">
    <div class="signform">
      <h3>계정정보</h3>
      <p>아이디</p>
      <input @input="onUsername" type="text" placeholder="">
      <!-- <button class="btn btn-primary">중복확인</button> -->
      <br>
      <p>비밀번호</p>
      <!-- <span class="pw-check">영문자와 숫자를 섞어주세요</span> -->
      <input @input="onPassword" type="password" placeholder="">
      <br>
      <p>비밀번호 확인</p>
      <!-- <span class="pw-confirm">비밀번호가 일치하지 않습니다.</span> -->
      <input @input="onPasswordConfirmation" type="password" placeholder="">
      <br>
      <hr>
      <h3>개인정보</h3>
      <p>이름</p>
      <input @input="onFullName" type="text" placeholder="">
      <br>
      <p>이메일</p>
      <input @input="onEmail" type="text" placeholder="">
      <select name="" id="mailDomain">
        <option value="@naver.com">@naver.com</option>
        <option value="@google.com">@google.com</option>
        <option value="@hanmail.net">@hanmail.net</option>
        <option value="@naver.com">@yahoo.co.kr</option>
        <option value="@naver.com">@nate.com</option>
      </select>
      <br>
      <p>전화번호</p>
      <input @input="onPhonenumber" type="text" placeholder="">
      <br>
      <button class="btn btn-success" @click="signup">회원가입</button>
    </div>
  </div>
</template>

<script>
import router from '@/router'
import { reactive } from '@vue/reactivity'
import axios from 'axios'

// const baseURL = 'http://127.0.0.1:8000/'
const baseURL = 'http://k6s105.p.ssafy.io:8004/'

export default {
  setup() {
    const state = reactive({
      username: '',
      email: '',
      phonenumber: '',
      fullName: '',
      password: '',
      password_confirmation: ''
    })

    const onUsername = (e) => {
      console.log(e.target.value)
      state.username = e.target.value
    }
    const onEmail = (e) => {
      state.email = e.target.value
    }
    const onPhonenumber = (e) => {
      state.phonenumber = e.target.value
    }
    const onFullName = (e) => {
      state.fullName = e.target.value
    }
    const onPassword = (e) => {
      state.password = e.target.value
    }
    const onPasswordConfirmation = (e) => {
      state.password_confirmation = e.target.value
    }

    const signup = (e) => {
      e.preventDefault()
      const mail = document.getElementById("mailDomain")
      const mailVal = mail.options[mail.selectedIndex].value
      const credentials = {
        username: state.username,
        password: state.password,
        passwordConfirmation: state.password_confirmation,
        phonenumber: state.phonenumber,
        // address: state.address,
        email: state.email + mailVal,
        fullname: state.fullName
      }
      console.log(credentials.email)
      if (credentials.username != '' && credentials.password != '' && credentials.passwordConfirmation != '' && credentials.email != '' && credentials.phonenumber != ''){
        axios({
          method: 'post',
          url: `${baseURL}accounts/signup/`,
          data: credentials
        })
        .then((res) => {
          console.log(res)
          router.push({ path: '/login'})
        })
        .catch((res) => {
          console.log(res)
        })
      } else {
        alert('작성이 덜 됐습니다')
      }
    }

    return {state, onUsername, onEmail, onPhonenumber, onFullName, onPassword, onPasswordConfirmation, signup}
  }
}
</script>

<style lang="scss" scoped>
  .page {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgb(221, 221, 221);
    min-height: 100%;
  }
  .signform {
    padding: 30px;
    text-align: left;
    background-color: white;
    width: 400px;
    border-radius: 15px;
    box-shadow: 3px 3px 5px;

    p {
      margin: 0;
      font-size: 12px;
    }

    input {
      margin-bottom: 15px;
    }

    select {
      height: 32px;
    }
  }
</style>