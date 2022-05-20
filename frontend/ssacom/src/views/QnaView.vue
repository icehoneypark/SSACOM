<template>
  <div class="qna">
    <h1>> Q&A</h1>
  </div>
  <div class="container">
    <!-- <button @click="create" type="button">글작성</button> -->
    <!-- <button @click="getpost" type="button">새로고침</button> -->
    <button class="btn btn-primary" @click="create" type="button"><i class="fa-solid fa-pencil"></i> 글작성</button>
    <button class="btn btn-secondary" @click="getpost" type="button"><i class="fa-solid fa-arrows-rotate"></i> 새로고침</button>
    <table class="table table-striped table-hover" >
      <thead>
        <tr>
          <th scope="col" style="width: 10%">#</th>
          <th scope="col" style="width: 60%">제목</th>
          <th scope="col" style="width: 20%">작성일</th>
          <th scope="col" style="width: 10%">작성자</th>
        </tr>
      </thead>
      <tbody>
        <tr :key="index" v-for="(post, index) in state.posts" @click="detail(post.id)">
          <td>{{ index+1 }}</td>
          <td>{{ post.title }}</td>
          <td>{{ post.created_at.substr(0, 10) }}</td>
          <td>{{ post.user }}</td>
        </tr>
      </tbody>
    </table>
  </div>


</template>

<script>
import axios from 'axios'
import { useRouter } from 'vue-router';
import { onMounted, reactive, } from "vue";
import VueJwtDecode from 'vue-jwt-decode'

const baseURL = 'http://127.0.0.1:8000/'
// const baseURL = 'http://k6s105.p.ssafy.io:8004/'

export default {
  name : 'QnaView',
  
  setup() {
    const router = useRouter()
    const token = localStorage.getItem('jwt')
    const info = VueJwtDecode.decode(token)
    const state = reactive({
      posts: '',
    })


    const create = () => {
      router.push('/qna/create')
    }
    const detail = (index) => {
      router.push({
        name: 'qnadetail',
        params: {
          id: index,
        }
      })

    }

    const getpost = () => {
      axios({
        method: 'get',
        url: `${baseURL}qna/`,
        headers: {Authorization : `JWT ${token}`},
      })
        .then(res => {
          console.log(res)
          state.posts = res.data
        })
        .catch(err => {
          console.log(err)
        })

    }

    onMounted(() => {
      getpost()
    })
    return {getpost, create, detail, state, info}
  },
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