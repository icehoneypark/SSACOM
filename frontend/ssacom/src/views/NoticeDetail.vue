<template>
  <div class="notice">
    <h1>detail page</h1>
  </div>
  <div>
    <button @click="update">수정</button>
    <button @click="Delete">삭제</button>
  </div>
  <div class="container">
    <p>제목 : {{ state.post.title }}</p>
    <p>내용 : {{ state.post.content}}</p>
  </div>
</template>

<script>
import axios from 'axios'
import { useRouter, useRoute } from "vue-router";
import { onMounted, reactive } from "vue";

const baseURL = 'http://127.0.0.1:8000/'
// const baseURL = 'http://k6s105.p.ssafy.io:8004/'

export default {
  name : 'NoticeDetail',
  setup() {
    const router = useRouter()
    const route = useRoute()
    const token = localStorage.getItem('jwt')
    const state = reactive({
      id: route.params.id,
      post: {},
    })

    const getpost = () => {
      axios({
        method: 'get',
        url: `${baseURL}notices/${state.id}`,
        headers: {Authorization : `JWT ${token}`},
      })
        .then(res => {
          console.log(res)
          state.post = res.data
        })
        .catch(err => {
          console.log(err)
        })

    }

    const Delete = () => {
      axios({
        method: 'delete',
        url: `${baseURL}notices/${state.id}/`,
        headers: {Authorization : `JWT ${token}`},
      })
      .then(res => {
        console.log(res)
        router.push("/notice")
      })
      .catch(err => {
        console.log(err)
      })

    }
    const update = () => {
      axios({
        method: 'put',
        url: `${baseURL}notices/${state.id}/`,
        data: state.post,
        headers: {Authorization : `JWT ${token}`},
      })
      .then(res => {
        console.log('실행')
        console.log(res)
        router.push({
          name: 'noticeupdate',
          params: {
            id: state.id,
          }
        })
      })
      .catch(err => {
        console.log('에러')
        console.log(err)
      })
    }

    onMounted(() => {
      getpost()
    })
    return { state, Delete, update, getpost }
  }
}
</script>
<style>
 .container{
   border: 1px solid rgb(150, 150, 150);
   width: 50em;
   height: 500px;
 }
</style>