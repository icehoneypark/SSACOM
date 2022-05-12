<template>
  <h1>update</h1>
  <button @click="update">작성</button>
  {{ index }}
  {{ post }}
  <div>
    <input 
    type="text"
    v-model="title"
    placeholder="제목">

    <textarea
      type="text"
      v-model="content"
      placeholder="내용입력"
    ></textarea>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name : 'NoticeUpdate',
  data: function() {
    return {
      index : this.$route.params.id,
      title: null,
      content: null,
      posts: null,
      token : localStorage.getItem('jwt')
    }
  },
  computed: {
    post: function () {
      return this.posts.find(post => post.id === Number(this.index))
    } 
  },
  created: function () {
    this.getpost()
  },
  methods: {
    getpost : function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/notices/',
        headers: {Authorization : `JWT ${this.token}`},
      })
        .then(res => {
            console.log(res)
            this.posts = res.data
          })
          .catch(err => {
            console.log(err)
          })
    },
    // update: function () {
    //   const noticeData = {
    //     id : this.index,
    //     title: this.title,
    //     content: this.content,
    //   }
    //   this.$store.dispatch("updateNotice", noticeData),
    //   this.$router.push({
    //     name: 'NoticeDetail',
    //   })
    // },
  }
}
</script>

<style>

</style>