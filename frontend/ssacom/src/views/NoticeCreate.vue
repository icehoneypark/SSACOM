<template>
  <div class="notice">
    <h1>> Notice - Create</h1>
  </div>
  <div>
    </div>
  <div class="container">
    <p>제목</p>
    <input 
    type="text"
    class="form-control"
    v-model="state.title"
    placeholder="제목을 입력해 주세요">
    <br>
    <p>내용</p>
    <textarea
      type="text"
      rows="11"
      class="form-control"
      v-model="state.content"
      placeholder="내용을 입력해 주세요"
    ></textarea>
    <button class="btn btn-secondary" @click="notice"><i class="fa-solid fa-rectangle-list"></i> 목록</button>
    <button class="btn btn-success" @click="create"><i class="fa-solid fa-pencil"></i> 작성</button>
  </div>



</template>

<script>
import axios from 'axios'
import { useRouter } from "vue-router"
import { reactive } from "vue"

const baseURL = 'http://127.0.0.1:8000/'
// const baseURL = 'http://k6s105.p.ssafy.io:8004/'

export default {
  name : 'NoticeCreate',
  setup() {
    const router = useRouter()
    const token = localStorage.getItem('jwt')
    const state = reactive({
      title: null,
      content: null,
    })

    const create = () => {
      const noticeData = {
        title: state.title,
        content: state.content,
      }
      axios({
        method: 'post',
        url: `${baseURL}notices/`,
        data: noticeData,
        headers: {Authorization : `JWT ${token}`},
      })
        .then(res => {
            console.log(res)
          })
          .catch(err => {
            console.log(err)
          })
      router.push("/notice")
    }

    const notice = () => {
      router.push("/notice")
    }

    return { state, create, notice }
  }
}
</script>
<style>
 .container{
   border: 1px solid aliceblue;
   border-radius: 15px;
   width: 50em;
   height: 530px;
   background-color: aliceblue;
   padding: 30px;
   box-shadow: 2px 2px 5px gray;
 }
  h1{
    background-color: #0C4DA2;
   text-align: left;
   padding: 20px;
   padding-left: 150px;
   margin-bottom: 1em;
   margin-top: 0;
   color: white;
   font-size: 23px;
   border-bottom-right-radius: 40px;
   margin-right: 20px;
 }
</style>