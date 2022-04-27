<template>
  <div class="mypage">
    <div class="wrapper">
      <img src="../assets/DefaultProfile.png" alt="" width="50" style="border-radius:30px;">
      <span>{{state.username}}님의 마이페이지</span>
      <button type="button" class="btn btn-primary">edit</button>
      <br>
      <p>Tel. {{state.phonenumber}}</p>
    </div>
    <my-component />
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
      Launch demo modal
    </button>

    <!-- 개인정보 수정 폼 -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">개인정보 수정</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <span>ID: </span>
            <input type="text" placeholder="홍길동" disabled>
            <br>
            <span>PW: </span>
            <input type="text" placeholder="*********" disabled>
            <br>
            <span>Tel: </span>
            <input type="text" placeholder="전화번호를 입력하세요" @input="onTel()">
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
import MyComponent from "../components/MyComponent.vue";
import axios from 'axios';
import { onMounted, reactive } from "vue";


export default ({
  components: {MyComponent},

  setup() {
    const state = reactive({
      username: '홍길동',
      phonenumber: '123-456-789',
      address: '황상동 123-2'
    })
    // 유저 데이터 입력
    const onTel = (e) => {
      state.phonenumber = e.target.value
    }

    const onAddress = (e) => {
      state.phonenumber = e.target.value
    }
    // 그 외 함수 부분
    const saveChange = () => {
      axios.post(
        'url',

      )
    }

    // 라이프 사이클
    onMounted(() => {
      console.log(state.test)
      axios.get(
        '/accounts/'
      )
      .then((res) => state.username = res.data)
    })

    return {state, saveChange, onTel, onAddress}
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
