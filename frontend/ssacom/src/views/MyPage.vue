<template>
  <div class="mypage">
    <div class="wrapper">
      <img src="../assets/DefaultProfile.png" alt="" width="50" style="border-radius:30px;">
      <span>{{state.username}}님의 마이페이지</span>
      <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
      개인정보 수정
    </button>
      <br>
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
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary" onclick="saveChange()">Save changes</button>
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
import VueJwtDecode from 'vue-jwt-decode';


export default ({
  components: {ShopList},

  setup() {
    const hash = localStorage.getItem('jwt')
    const info = VueJwtDecode.decode(hash)

    const state = reactive({
      username: '',
      phonenumber: '',
      address: ''
    })
    // 유저 데이터 입력
    const onTel = (e) => {
      state.phonenumber = e.target.value
    }

    const onAddress = (e) => {
      state.phonenumber = e.target.value
    }

    // 함수 부분

    const saveChange = () => {
      const data = {
        phonenumber: state.phonenumber,
        address: state.address,
      }
      axios({
        method: 'put',
        url: `userchange/${info.user_id}/`, // 1에다가 pk 이름 따서 넣기 (jwt decode해서 정보있으면 그걸로 넣고 없으면 pk 받아오는 api 새로 만들거나 `store`에 저장하거나)
        data,
      })
      .then((res) => console.log(res))
      .catch((res) => console.log(res))
    }

    const userDelete = () => {
      if(confirm('정말 탈퇴하시겠습니까?')){
        axios({
          method: 'DELETE',
          url: `http://localhost:8000/accounts/userdelete/${info.user_id}`,
        })
      }
    }

    // 라이프 사이클
    onMounted(() => {
      axios({
        method: 'get',
        url: `http://localhost:8000/accounts/${info.user_id}/` // pk 넣기
      })
      .then((res) => {
        console.log(res)
        state.username = res.data.username
        state.phonenumber = res.data.phonenumber
        // state.address = res.data.address
      })
      .catch((res) => {
        console.log(res)
      })
    })

    return {state, saveChange, onTel, onAddress, userDelete}
  },
})
</script>

<style lang="scss" scoped>

  .mypage{ 
    padding: 20px

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
