<template>
  <div class="notice">
    <h1>detail page</h1>
  </div>
  <div>
    <button @click="update">수정</button>
    <button @click="Delete">삭제</button>
  </div>
  {{ $route.params.id }}
  <p>제목 : {{ post.title }}</p>
  <p>내용 : {{ post.content}}</p>
</template>

<script>
import axios from 'axios'

export default {
  name : 'NoticeDetail',
  data : function () {
    return {
      id: this.$route.params.id,
      posts: null,
    }
  },
  computed: {
    post : function () {
      return this.posts.find(post => post.id === Number(this.id))
    }
  },
  methods: {
    Delete: function () {
      axios({
          method: 'delete',
          url: `http://127.0.0.1:8000/notices/${this.id}/`,
        })
          .then(res => {
            console.log(res)
            this.$router.push("/notice")
          })
          .catch(err => {
            console.log(err)
          })
    },
    update: function () {
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/notices/${this.id}/`,
        data: this.post,
      })
        .then(res => {
          console.log(res)
          this.$router.push({
        name: 'noticeupdate',
        params: {
          id: this.id,
        }
      })
        })

    },
    getpost : function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/notices/',
      })
        .then(res => {
            console.log(res)
            this.posts = res.data
          })
          .catch(err => {
            console.log(err)
          })
    },
    
  },
  created: function () {
    this.getpost()
  },
}
</script>