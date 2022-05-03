<template>
  <div class="notice">
    <h1>detail page</h1>
  </div>
  <div>
    <button
    @click="create">작성</button>
  </div>
  <div>
    <p>{{ post.title}}</p>
    <p>{{ post.content}}</p>
  </div>



</template>

<script>
export default {
  name : 'NoticeDetail',
  data : function() {
    return {
      title : null,
      content : null,
    }
  },
  methods : {
    create: function () {
      const noticeData = {
        title: this.title,
        content: this.content,
      }
      this.$store.dispatch("createNotice", noticeData),
      this.$router.push("/notice")
    }
  }
}
</script>