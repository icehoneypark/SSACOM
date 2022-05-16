<template>
  <h1>update</h1>
  <button @click="update">작성</button>
  <div>
    <input 
    type="text"
    v-model="state.posts.title">

    <textarea
      type="text"
      v-model="state.posts.content"
    ></textarea>
  </div>
</template>

<script>
import axios from 'axios'
import { useRouter, useRoute } from "vue-router";
import { onMounted, reactive, } from "vue";

const baseURL = 'http://127.0.0.1:8000/'
// const baseURL = 'http://k6s105.p.ssafy.io:8004/'

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

</style>