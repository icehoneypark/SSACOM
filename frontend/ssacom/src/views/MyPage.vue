<template>
  <div class="mypage">
    <div class="wrapper">
      <img src="../assets/DefaultProfile.png" alt="" width="50" style="border-radius:30px;">
      <span>{{state.username}}님의 마이페이지</span>
      <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
      개인정보 수정
    </button>
      <br>
      <!-- 지금은 state에서 받아오도록 돼있는데, 개인정보 수정 후에 api요청으로 가져오도록 고칠 예정 -->
      <p>Tel. {{state.phonenumber}}</p>
    </div>
    <shop-list />
    <button type="button" class="btn btn-danger" @click="userDelete">회원탈퇴</button>

    <!-- 개인정보 수정 폼 모달 -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">개인정보 수정</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <span>ID: </span>
            <input type="text" :placeholder="state.username" disabled>
            <br>
            <span>PW: </span>
            <input type="text" placeholder="*********" disabled>
            <br>
            <span>Tel: </span>
            <input type="text" placeholder="전화번호를 입력하세요" @input="onTel">
            <br>
            <span>Address: </span>
            <input type="text" placeholder="주소를 입력하세요" @input="onAddress">
            <br>
            <span>fullname: </span>
            <input type="text" placeholder="이름을 입력하세요" @input="onFullname">
            <br>
            <span>Email: </span>
            <input type="text" placeholder="Email을 입력하세요" @input="onEmail">
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary" @click="saveChange">Save changes</button>
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
        url: `http://localhost:8000/accounts/userchange/${info.user_id}/`,
        data: data
      })
      .then((res) => {
        console.log(res)

        axios({
          method: 'get',
          url: `http://localhost:8000/accounts/${info.user_id}/`
        })
        .then((res) => {
          console.log(res)
          state.phonenumber = res.data.phonenumber
          state.fullname = res.data.fullname
          state.email = res.data.email
        })
        })
      .catch((res) => console.log(res))
    }

    const userDelete = () => {
      if(confirm('정말 탈퇴하시겠습니까?')){
        axios({
          method: 'delete',
          url: `http://localhost:8000/accounts/userdelete/${info.user_id}`,
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
        url: `http://localhost:8000/accounts/${info.user_id}/`
      })
      .then((res) => {
        console.log(res)
        state.phonenumber = res.data.phonenumber
        state.username = res.data.username
        state.fullname = res.data.fullname
        state.email = res.data.email
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
  .mypage{ 
    padding: 20px;
    width: 100%;
  }
  .wrapper {
    border: 1px solid rgb(150, 150, 150);
    border-radius: 20px;
    padding: 20px;

    span:first-of-type {
      font-weight: bold;
      font-size: 20px;
    }
  }
</style>
