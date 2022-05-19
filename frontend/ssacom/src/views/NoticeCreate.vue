<template>
  <div class="notice">
    <h1>create page</h1>
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
    <p>내용</p>
    <textarea
      type="text"
      rows="5"
      class="form-control"
      v-model="state.content"
      placeholder="내용을 입력해 주세요"
    ></textarea>
    <button @click="create">작성</button>
    <button @click="notice">목록</button>
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
   border: 1px solid rgb(150, 150, 150);
   width: 50em;
   height: 500px;
   background-color: aliceblue;
 }
 h1{
   text-align: center;
   margin-top: 1em;
   margin-bottom: 1em;
 }
</style>