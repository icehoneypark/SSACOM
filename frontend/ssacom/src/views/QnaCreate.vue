<template>
  <h1>QnA 작성</h1>
  <div class="container">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title"> 새로운 글 등록 </h5>
        <form>
          <div>
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
        
            <p>카테고리</p>
            <textarea
              type="text"
              rows="2"
              class="form-control"
              v-model="state.category"
              placeholder="내용을 입력해 주세요"
            ></textarea>
          </div>
          <div>
          
            <button class="btn btn-secondary" @click="qna"><i class="fa-solid fa-rectangle-list"></i> 목록</button>
            <button class="btn btn-success" @click="create"><i class="fa-solid fa-pencil"></i> 작성</button>
          </div>

        </form>
      </div>
    </div>
  </div>



</template>

<script>
import axios from 'axios'
import { useRouter } from "vue-router"
import { reactive } from "vue"
import VueJwtDecode from 'vue-jwt-decode'

// const baseURL = 'http://127.0.0.1:8000/'
const baseURL = 'http://k6s105.p.ssafy.io:8004/'

export default {
  name : 'QnaCreate',
  setup() {
    const router = useRouter()
    const token = localStorage.getItem('jwt')
    const info = VueJwtDecode.decode(token)
    const state = reactive({
      title: null,
      content: null,
      category: null,
    })

    const create = () => {
      const qnaData = {
        title: state.title,
        content: state.content,
        category: state.category,
        user: info.username,
      }
      axios({
        method: 'post',
        url: `${baseURL}qna/`,
        data: qnaData,
        headers: {Authorization : `JWT ${token}`},
      })
        .then(res => {
          console.log(res)
          })
          .catch(err => {
            console.log(err)
          })
      router.push("/qna")
    }

    const qna = () => {
      router.push("/qna")
    }

    return { state, create, qna, info }
  }
}
</script>
<style lang="scss" scoped>
 .container{
   border: 1px solid aliceblue;
   border-radius: 15px;
   width: 50em;
   height: 500px;
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
   border-bottom: 1px solid gray;
   color: white;
   font-size: 23px;
   border-bottom-right-radius: 40px;
   margin-right: 20px;
 }
</style>