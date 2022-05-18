<template>
  <h1>update</h1>
  <div class="container">
    <p>제목</p>
    <input 
    type="text"
    class="form-control"
    v-model="state.posts.title">

    <p>내용</p>
    <textarea
      type="text"
      rows="5"
      class="form-control"
      v-model="state.posts.content"
    ></textarea>
    <button @click="update">수정</button>
  </div>
</template>

<script>
import axios from 'axios'
import { useRouter, useRoute } from "vue-router";
import { onMounted, reactive, } from "vue";

// const baseURL = 'http://127.0.0.1:8000/'
const baseURL = 'http://k6s105.p.ssafy.io:8004/'

export default {
  name : 'NoticeUpdate',
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
        url: `${baseURL}notices/${state.id}`,
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

      const noticeData = {
        id : state.posts.id,
        title: state.posts.title,
        content: state.posts.content,
      }
      axios({
        method: 'put',
        url: `${baseURL}notices/${state.id}/`,
        data: noticeData,
        headers: {Authorization : `JWT ${token}`},
      })
        .then(res => {
            console.log(res)
          })
          .catch(err => {
            console.log(err)
          })
      router.push({
        name: 'noticedetail',
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