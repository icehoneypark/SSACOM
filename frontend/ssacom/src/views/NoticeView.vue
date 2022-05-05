<template>
  <div class="notice">
    <h1>This is an notice page</h1>
    <button @click="create" type="button">글작성</button>
    <button @click="getpost" type="button">새로고침</button>
  </div>

  <div>
    <table class="table container" >
      <thead>
        <tr>
          <th scope="col">글번호</th>
          <th scope="col">제목</th>
          <th scope="col">작성자</th>
          <th scope="col">작성일자</th>
        </tr>
      </thead>
      <tbody>
        <tr :key="index" v-for="(post, index) in posts" @click="detail(post.id)">
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

export default {
  name : 'NoticeView',
  data : function() {
    return {
      posts : null
    }
  },
  methods : {
    create () {
      this.$router.push('/notice/create')
    },
    detail : function (index) {
      this.$router.push({
        name: 'noticedetail',
        params: {
          id: index,
          test: 'qqq'
        }
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
  }
}
</script>