<template>
  <div class="qna">
    <h1>detail page</h1>
  </div>
  <div class="container">
  <button class="btn btn-primary" @click="update">수정</button>
  <button class="btn btn-danger" @click="Delete">삭제</button>
  <p class="title">{{ state.post.title }}</p>
  <span :v-if="state.post" class="date">{{ state.post.created_at.substr(0, 10)}} {{ state.post.created_at.substr(11, 8)}}</span>
  <div class="area">
  <p class="content">{{ state.post.content}}</p>
  </div>
  <p>카테고리: {{ state.post.category }}</p>
  <br>
  <p style="font-weight: 600; margin-bottom:5px;">댓글</p>
  <ul :key="index" v-for="(comm, index) in state.comment">
    <li>
      {{ comm.content }}
      <!-- <button @click="commentUpdate(comm.id)">수정</button> -->
      <button type="button" class="btn-close" aria-label="Close" @click="commentDelete(comm.id)"></button>
    </li>
  </ul>
    <textarea
      type="text"
      rows="1"
      class="form-control"
      v-model="state.content"
      placeholder="댓글을 입력해 주세요"
    ></textarea>
    <button class="btn btn-secondary" @click="commentCreate">댓글작성</button>
  <!-- {{ state.comment }} -->
  
  </div>
</template>

<script>
import axios from 'axios'
import { useRouter, useRoute } from "vue-router";
import { onMounted, reactive } from "vue";

const baseURL = 'http://127.0.0.1:8000/'
// const baseURL = 'http://k6s105.p.ssafy.io:8004/'

export default {
  name : 'QnaDetail',
  setup() {
    const router = useRouter()
    const route = useRoute()
    const token = localStorage.getItem('jwt')
    const state = reactive({
      id: route.params.id,
      post: {'created_at': '11'},
      comment: null,
      content: null,
    })

    const getpost = () => {
      axios({
        method: 'get',
        url: `${baseURL}qna/${state.id}`,
        headers: {Authorization : `JWT ${token}`},
      })
        .then(res => {
          // console.log(res)
          state.post = res.data
        })
        .catch(err => {
          console.log(err)
        })

    }
    const getcomment = () => {
      axios({
        method: 'get',
        url: `${baseURL}qna/${state.id}/review/`,
        headers: {Authorization : `JWT ${token}`},
      })
        .then(res => {
          // console.log(res)
          state.comment = res.data
        })
        .catch(err => {
          console.log(err)
        })

    }

    const Delete = () => {
      axios({
        method: 'delete',
        url: `${baseURL}qna/${state.id}/`,
        headers: {Authorization : `JWT ${token}`},
      })
      .then(res => {
        console.log(res)
        router.push("/qna")
      })
      .catch(err => {
        console.log(err)
      })

    }
    const update = () => {
      axios({
        method: 'put',
        url: `${baseURL}qna/${state.id}/`,
        data: state.post,
        headers: {Authorization : `JWT ${token}`},
      })
      .then(res => {
        console.log('실행')
        console.log(res)
        router.push({
          name: 'qnaupdate',
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
    const commentCreate = () => {
      const commentData = {
        content: state.content,
        qna: state.id
      }
      axios({
        method: 'post',
        url: `${baseURL}qna/${state.id}/review/`,
        data: commentData,
        headers: {Authorization : `JWT ${token}`},
      })
      .then(res => {
        router.go(0)
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })

    }
    const commentDelete = (reviewid) => {
      axios({
        method: 'delete',
        url: `${baseURL}qna/${state.id}/review/${reviewid}`,
        headers: {Authorization : `JWT ${token}`},
      })
      .then(res => {
        console.log(res)
        router.go(0)
      })
      .catch(err => {
        console.log(err)
      })

    }
    const commentUpdate = (reviewid) => {
      axios({
        method: 'put',
        url: `${baseURL}qna/${state.id}/review/${reviewid}`,
        data: state.post,
        headers: {Authorization : `JWT ${token}`},
      })
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
    }

    onMounted(() => {
      getpost()
      getcomment()
    })
    return { state, Delete, update, getpost, getcomment, commentUpdate, commentDelete, commentCreate, }
  }

}
</script>
<style lang="scss" scoped>
 .container{
   border: 1px solid aliceblue;
   border-radius: 15px;
   width: 50em;
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
   height: 250px;
   border-radius: 5px;
   overflow: auto;
   padding: 20px;
 }
</style>