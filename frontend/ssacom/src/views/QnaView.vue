<template>
  <div class="qna">
    <h1>This is an qna page</h1>
    <button @click="create" type="button">글작성</button>
    <button @click="getpost" type="button">새로고침</button>
  </div>
  <div class="container d-flex justify-content-center">
    <table class="table">
      <thead>
        <tr>
          <th scope="col">게시판 순서</th>
          <th scope="col">제목</th>
          <th scope="col">내용</th>
          <th scope="col">작성자</th>
        </tr>
      </thead>
      <tbody>
        <tr :key="index" v-for="(post, index) in state.posts" @click="detail(post.id)">
          <td>{{ index+1 }}</td>
          <td>{{ post.title }}</td>
          <td>{{ post.content }}</td>
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
          // console.log(res)
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