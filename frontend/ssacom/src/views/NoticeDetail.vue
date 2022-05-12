<template>
  <div class="notice">
    <h1>detail page</h1>
  </div>
  <div>
    <button @click="update">수정</button>
    <button @click="Delete">삭제</button>
  </div>
  <p>제목 : {{ state.post.title }}</p>
  <p>내용 : {{ state.post.content}}</p>
</template>

<script>
import axios from 'axios'
import { useRouter, useRoute } from "vue-router";
import { onMounted, reactive } from "vue";

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
        url: `http://127.0.0.1:8000/notices/${state.id}`,
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
        url: `http://127.0.0.1:8000/notices/${state.id}/`,
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
        url: `http://127.0.0.1:8000/notices/${state.id}/`,
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



  // data : function () {
  //   return {
  //     id: this.$route.params.id,
  //     posts: null,
  //     token : localStorage.getItem('jwt')
  //   }
  // },
  // computed: {
  //   post : function () {
  //     return this.posts.find(post => post.id === Number(this.id))
  //   }
  // },
  // methods: {
  //   Delete: function () {
  //     axios({
  //         method: 'delete',
  //         url: `http://127.0.0.1:8000/notices/${this.id}/`,
  //         headers: {Authorization : `JWT ${this.token}`},
  //       })
  //         .then(res => {
  //           console.log(res)
  //           this.$router.push("/notice")
  //         })
  //         .catch(err => {
  //           console.log(err)
  //         })
  //   },
  //   update: function () {
  //     axios({
  //       method: 'put',
  //       url: `http://127.0.0.1:8000/notices/${this.id}/`,
  //       data: this.post,
  //       headers: {Authorization : `JWT ${this.token}`},
  //     })
  //       .then(res => {
  //         console.log(res)
  //         this.$router.push({
  //       name: 'noticeupdate',
  //       params: {
  //         id: this.id,
  //       }
  //     })
  //       })

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
  //         })
  //         .catch(err => {
  //           console.log(err)
  //         })
  //   },
    
  // },
  // created: function () {
  //   this.getpost()
  // },
}
</script>