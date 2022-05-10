<template>
  <div class="notice">
    <h1>create page</h1>
  </div>
  <div>
    <button
    @click="create">작성</button>
  </div>
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
  name : 'NoticeCreate',
  data : function() {
    return {
      title : null,
      content : null,
      token : localStorage.getItem('jwt'),
    }
  },
  methods : {
    create: function () {
      const noticeData = {
        title: this.title,
        content: this.content,
      }
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/notices/',
        data: noticeData,
        headers: {Authorization : `JWT ${this.token}`},
      })
        .then(res => {
            console.log(res)
          })
          .catch(err => {
            console.log(err)
          })
      this.$router.push("/notice")
    }
  }
}
</script>