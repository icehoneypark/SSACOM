<template>
  <div class="notice">
    <h1>> Notice - Detail</h1>
  </div>
  <div class="container">
    <p class="title">{{ state.post.title }}</p>
    <span :v-if="state.post" class="date">{{ state.post.created_at.substr(0, 10)}} {{ state.post.created_at.substr(11, 11)}}</span>
    <div class="area">
    <p class="content">{{ state.post.content}}</p>
    </div>
    <button class="btn btn-primary" @click="update">수정</button>
    <button class="btn btn-danger" @click="Delete">삭제</button>
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
      post: {'created_at': "11"},
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
 .title {
   font-size: 25px;
   font-weight: 600;
   margin-bottom: 10px;
 }

 .date {
   font-size: 13px;
   color: gray;
 }

 .area {
   background-color: white;
   height: 300px;
   border-radius: 5px;
   overflow: auto;
   padding: 20px;
 }
</style>