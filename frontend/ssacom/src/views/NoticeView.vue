<template>
  <div class="notice">
    <h1>This is an notice page</h1>
    <button @click="create" type="button">글작성</button>
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
        <tr :key="index" v-for="(post, index) in posts" @click="detail(index)">
          <td>{{ index }}</td>
          <td>{{ post.title }}</td>
          <td>{{ post.content }}</td>
          <td>{{ post.created }}</td>
        </tr>
      </tbody>
    </table>
  </div>


</template>

<script>
export default {
  name : 'NoticeView',
  data : function() {
    return {
      posts : this.$store.state.posts
    }
  },
  methods : {
    create () {
      this.$router.push('/notice/create')
    },
    detail : function (index) {
      console.log(123)
      console.log(index)

      this.$router.push({
        name: 'NoticeDetail',
        params: {
          id: index
        }
      })
    },
  }
}
</script>