<template>
  <div class="notice">
    <h1>> Notice</h1>
  </div>
  <div class="container" style="overflow: auto;">
    <button class="btn btn-primary" @click="create" type="button"><i class="fa-solid fa-pencil"></i> 글작성</button>
    <button class="btn btn-secondary" @click="getpost" type="button"><i class="fa-solid fa-arrows-rotate"></i> 새로고침</button>
    <table class="table table-striped table-hover"  >
      <thead>
        <tr>
          <th scope="col" style="width: 10%">#</th>
          <th scope="col" style="width: 60%">제목</th>
          <th scope="col" style="width: 30%">작성날짜</th>
        </tr>
      </thead>
      <tbody>
        <tr :key="index" v-for="(post, index) in state.posts" @click="detail(post.id)">
          <td>{{ index+1 }}</td>
          <td>{{ post.title }}</td>
          <td>{{ post.created_at.substr(0, 10) }}</td>
        </tr>
      </tbody>
    </table>
  </div>


</template>

<script>
import axios from 'axios'
import { useRouter } from 'vue-router';
import { onMounted, reactive, } from "vue";

// const baseURL = 'http://127.0.0.1:8000/'
const baseURL = 'http://k6s105.p.ssafy.io:8004/'

export default {
  name : 'NoticeView',
  
  setup() {
    const router = useRouter()
    const token = localStorage.getItem('jwt')

    const state = reactive({
      posts: '',
    })


    const create = () => {
      router.push('/notice/create')
    }
    const detail = (index) => {
      router.push({
        name: 'noticedetail',
        params: {
          id: index,
        }
      })

    }

    const getpost = () => {
      axios({
        method: 'get',
        url: `${baseURL}notices/`,
        headers: {Authorization : `JWT ${token}`},
      })
        .then(res => {
          console.log(res)
          state.posts = res.data
          console.log(state.posts[0].created_at)
        })
        .catch(err => {
          console.log('getpost error')
          console.log(err)
        })

    }

    onMounted(() => {
      getpost()
    })
    return {getpost, create, detail, state,}
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