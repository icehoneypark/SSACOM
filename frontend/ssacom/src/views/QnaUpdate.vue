<template>
  <h1>> QnA - Update</h1>
  <div class="container">
    
    <p>제목</p>
    <input 
    type="text"
    class="form-control"
    v-model="state.posts.title">

    <p>내용</p>
    <textarea
      type="text"
      rows="11"
      class="form-control"
      v-model="state.posts.content"
    ></textarea>

    <p>카테고리</p>
    <textarea
      type="text"
      rows="1"
      class="form-control"
      v-model="state.posts.category"
      placeholder="내용을 입력해 주세요"
    ></textarea>
    <button class="btn btn-success" @click="update">수정</button>
  </div>
</template>

<script>
import axios from 'axios'
import { useRouter, useRoute } from "vue-router";
import { onMounted, reactive, } from "vue";

const baseURL = 'http://127.0.0.1:8000/'
// const baseURL = 'http://k6s105.p.ssafy.io:8004/'

export default {
  name : 'QnaUpdate',
  setup() {
    const router = useRouter()
    const route = useRoute()
    const token = localStorage.getItem('jwt')
    const state = reactive({
      id: route.params.id,
      posts: {},
    })


    const getpost = () => {
      axios({
        method: 'get',
        url: `${baseURL}qna/${state.id}`,
        headers: {Authorization : `JWT ${token}`},
      })
        .then(res => {
          // console.log(res)
          state.posts = res.data
        })
        .catch(err => {
          console.log(err)
        })

    }


    const update = () => {

      const qnaData = {
        id : state.posts.id,
        title: state.posts.title,
        content: state.posts.content,
        category: state.posts.category,
      }
      axios({
        method: 'put',
        url: `${baseURL}qna/${state.id}/`,
        data: qnaData,
        headers: {Authorization : `JWT ${token}`},
      })
        .then(res => {
            console.log(res)
          })
          .catch(err => {
            console.log(err)
          })
      router.push({
        name: 'qnadetail',
        params: {
          id: state.posts.id,
        }
      })
    }

    onMounted(() => {
      getpost()
    })
    return { state, getpost, update }

  }
}
</script>

<style lang="scss" scoped>
 
 .container{
   border: 1px solid aliceblue;
   border-radius: 15px;
   width: 50em;
   min-height: 500px;
   height: auto;
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
 input {
   margin-bottom: 20px;
 }

 textarea {
   margin-bottom: 20px;
 }

 p {
   font-weight: 700;
 }
</style>