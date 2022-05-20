<template>
  <h1>> My Page</h1>
  <div class="mypage">
    <div class="wrapper">
      <div class="profile">
        <img src="../assets/DefaultProfile.png" alt="" width="100" style="border-radius:100px;">
        <p>{{state.fullname}}</p>
      </div>
      <p class="title">회원 정보</p>
      <p class="smallTitle">아이디</p>
      <input class="info" type="text" :value="state.username" readonly>
      <p class="smallTitle">이름</p>
      <input class="info" type="text" :value="state.fullname" readonly>
      <p class="smallTitle">전화번호</p>
      <input class="info" type="text" :value="state.phonenumber" readonly>
      <p class="smallTitle">이메일</p>
      <input class="info" type="text" :value="state.email" readonly>
      <br>
      <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
      개인정보 수정
      </button>
      <button type="button" class="btn btn-danger" @click="userDelete">회원탈퇴</button>
      <br>
      <!-- 지금은 state에서 받아오도록 돼있는데, 개인정보 수정 후에 api요청으로 가져오도록 고칠 예정 -->
    </div>
    <shop-list />
    

    <!-- 개인정보 수정 폼 모달 -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">개인정보 수정</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p class="smallTitle">아이디</p>
            <input type="text" :placeholder="state.username" disabled>
            <br>
            <p class="smallTitle">비밀번호</p>
            <input type="text" placeholder="*********" disabled>
            <br>
            <p class="smallTitle">이름</p>
            <input type="text" placeholder="이름을 입력하세요" @input="onFullname" :value="state.fullname">
            <br>
            <p class="smallTitle">전화번호</p>
            <input type="text" placeholder="전화번호를 입력하세요" @input="onTel" :value="state.phonenumber">
            <!-- <br>
            <span>Address: </span>
            <input type="text" placeholder="주소를 입력하세요" @input="onAddress"> -->
            <br>
            <p class="smallTitle">이메일</p>
            <input type="text" placeholder="Email을 입력하세요" @input="onEmail" :value="state.email">
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
            <button type="button" class="btn btn-primary" @click="saveChange" data-bs-dismiss="modal">저장</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ShopList from "../components/ShopList.vue";
import axios from 'axios';
import { onMounted, reactive } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import VueJwtDecode from 'vue-jwt-decode';

// const baseURL = 'http://127.0.0.1:8000/'
const baseURL = 'http://k6s105.p.ssafy.io:8004/'

export default ({
  components: {ShopList},

  setup() {
    const router = useRouter()
    const store = useStore()
    const hash = localStorage.getItem('jwt')
    const info = VueJwtDecode.decode(hash)

    const state = reactive({
      username: '',
      phonenumber: '',
      address: '',
      fullname: '',
      email: '',
    })
    let inputData = {
      username: '',
      phonenumber: '',
      fullname: '',
      email: '',
    }
    // 유저 데이터 입력
    const onTel = (e) => {
      inputData.phonenumber = e.target.value
    }

    const onAddress = (e) => {
      inputData.address = e.target.value
    }

    const onFullname = (e) => {
      inputData.fullname = e.target.value
    }

    const onEmail = (e) => {
      inputData.email = e.target.value
    }

    // 함수 부분

    const saveChange = () => {
      const data = {
        // username: 'test1',
        // password: '1234567',
        phonenumber: inputData.phonenumber,
        email: inputData.email,
        fullname: inputData.fullname,
        // address: state.address,
      }
      axios({
        method: 'put',
        url: `${baseURL}accounts/userchange/${info.user_id}/`,
        data: data
      })
      .then((res) => {
        console.log(res)

        axios({
          method: 'get',
          url: `${baseURL}accounts/${info.user_id}/`
        })
        .then((res) => {
          console.log(res)
          state.phonenumber = res.data.phonenumber
          state.fullname = res.data.fullname
          state.email = res.data.email
        })
        })
      .catch((res) => console.log(res))
      alert("개인정보 수정이 완료되었습니다.")
    }

    const userDelete = () => {
      if(confirm('정말 탈퇴하시겠습니까?')){
        axios({
          method: 'delete',
          url: `${baseURL}accounts/userdelete/${info.user_id}`,
        })
        .then(() => {
          store.dispatch('logout')
          localStorage.removeItem('jwt')
          router.push({ name : "login" })
        })
        .catch(() => {
          alert('알 수 없는 이유로 회원탈퇴에 실패하였습니다.')
        })
      }
    }

    // 라이프 사이클
    onMounted(() => {
      const test = [{id: 0}, {id: 1},{id: 2}]
      console.log(test)
      console.log(typeof(test))
      axios({
        method: 'get',
        url: `${baseURL}accounts/${info.user_id}/`
      })
      .then((res) => {
        console.log(res)
        state.phonenumber = res.data.phonenumber
        state.username = res.data.username
        state.fullname = res.data.fullname
        state.email = res.data.email
        inputData.phonenumber = res.data.phonenumber
        inputData.username = res.data.username
        inputData.fullname = res.data.fullname
        inputData.email = res.data.email
      })
      .catch((res) => {
        console.log(res)
      })
    })

    return {state, onTel, onAddress, onFullname, onEmail, userDelete, saveChange }
  },
})
</script>

<style lang="scss" scoped>
  h1{
    background-color: #0C4DA2;
   text-align: left;
   padding: 20px;
   padding-left: 150px;
  //  margin-bottom: 1em;
   margin-top: 0;
  //  border-bottom: 1px solid gray;
   color: white;
   font-size: 23px;
   border-bottom-right-radius: 40px;
   margin-right: 20px;
 }
  .mypage{ 
    padding: 20px;
    width: 100%;
    display: flex;
    justify-content: center;
    // background-color: rgb(221, 221, 221);
    min-height: 100%;
  }
  .wrapper {
    border: 1px solid rgb(150, 150, 150);
    border-radius: 20px;
    padding: 30px;
    background-color: white;
    width: 700px;
    height: 650px;
    span:first-of-type {
      font-weight: bold;
      font-size: 20px;
    }
  }

  .profile {
    text-align: center;
    margin-top: 15px;
    p {
      margin-top: 15px;
      font-size: 23px;
      font-weight: 700;
    }
  }

  .title {
    font-size: 18px;
    font-weight: 600;
  }

  .smallTitle {
    font-size: 12px;
    font-weight: 400;
    color: gray;
    margin-bottom: 5px;
    margin-top: 22px;
  }

  .info {
    margin-top: 0px;
    border: 0;
    border-bottom: 1px solid gray;
    width: 97%;
  }

  .btn {
    margin-top: 40px;
  }

  .modal-title {
    font-weight: 600;
  }

  .modal-body {
    input {
      width: 100%;
      border: 0;
      border-bottom: 1px solid gray;
    }
  }
</style>
