<template>
  <div class="notice">
    <h1>This is an notice page</h1>
    <button @click="create" type="button">글작성</button>
    <button @click="getpost" type="button">새로고침</button>
  </div>
  <!-- {{ state.test }} -->
  <!-- {{ state.posts }} -->
  <div>
    <table class="table container" >
      <thead>
        <tr>
          <th scope="col">게시판 순서</th>
          <th scope="col">제목</th>
          <th scope="col">내용</th>
          <th scope="col">글 주소</th>
        </tr>
      </thead>
      <tbody>
        <tr :key="index" v-for="(post, index) in state.posts" @click="detail(post.id)">
          <td>{{ index }}</td>
          <td>{{ post.title }}</td>
          <td>{{ post.content }}</td>
          <td>{{ post.id }}</td>
        </tr>
      </tbody>
    </table>
  </div>


</template>

<script>
import axios from 'axios'
import { useRouter } from 'vue-router';
import { onMounted, reactive, } from "vue";

export default {
  name : 'NoticeView',
  
  setup() {
    const router = useRouter()
    const token = localStorage.getItem('jwt')

    const state = reactive({
      posts: [],
      num: 0,
      test : {},
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
        url: 'http://127.0.0.1:8000/notices/',
        headers: {Authorization : `JWT ${token}`},
      })
        .then(res => {
          console.log(res.data)
          state.posts = res.data
          state.num = state.posts.length
          // for (let i = 0; i < state.num; i++) {
          //   state.test[i] = state.posts[i]
          // }
          // console.log(state.test)
        })
        .catch(err => {
          console.log(err)
        })

    }

    onMounted(() => {
      getpost()
    })
    return {getpost, create, detail, state,}
  },


















  // data : function() {
  //   return {
  //     posts : null,
  //     token : localStorage.getItem('jwt')
  //   }
  // },
  // methods : {
  //   create () {
  //     this.$router.push('/notice/create')
  //   },
  //   detail : function (index) {
  //     this.$router.push({
  //       name: 'noticedetail',
  //       params: {
  //         id: index,
  //       }
  //     })
  //   },
  //   getpost : function () {
  //     axios({
  //       method: 'get',
  //       url: 'http://127.0.0.1:8000/notices/',
  //       headers: {Authorization : `JWT ${this.token}`},
  //     })
  //       .then(res => {
  //           console.log(res)
  //           this.posts = res.data
  //           console.log(this.posts)
  //         })
  //         .catch(err => {
  //           console.log(err)
  //         })
  //   },
  // },
  // created: function () {
  //   this.getpost()
  // }








}
</script>