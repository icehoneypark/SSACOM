<template>
  <div>
    <input @input="onUsername" type="text" placeholder="username">
    <br>
    <input @input="onPassword" type="password" placeholder="password">
    <br>
    <input @input="onPasswordConfirmation" type="password" placeholder="passwordConfirmation">
    <br>
    <input @input="onEmail" type="text" placeholder="email">
    <br>
    <input @input="onPhonenumber" type="text" placeholder="phonenumber">
    <br>
    <input @input="onAddress" type="text" placeholder="address">
    <br>
    <button @click="signup">회원가입</button>
  </div>
</template>

<script>
import router from '@/router'
import { reactive } from '@vue/reactivity'
import axios from 'axios'
export default {
  setup() {
    const state = reactive({
      username: '',
      email: '',
      phonenumber: '',
      address: '',
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
    const onAddress = (e) => {
      state.address = e.target.value
    }
    const onPassword = (e) => {
      state.password = e.target.value
    }
    const onPasswordConfirmation = (e) => {
      state.passwordConfirmation = e.target.value
    }

    const signup = (e) => {
      e.preventDefault()
      const credentials = {
        username: state.username,
        password: state.password,
        passwordConfirmation: state.passwordConfirmation,
        phonenumber: state.phonenumber,
        address: state.address,
        email: state.email,
      }
      // 조건문 다시작성해야 할듯
      if (state.username !== '' && state.password !== '' && state.password_confirmation !== '' && state.email !== '' && state.phonenumber !== ''){
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/accounts/signup/',
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

    return {state, onUsername, onEmail, onPhonenumber, onAddress, onPassword, onPasswordConfirmation, signup}
  }
}
</script>

<style>

</style>