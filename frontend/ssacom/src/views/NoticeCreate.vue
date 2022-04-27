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
export default {
  name : 'NoticeCreate',
  data : function() {
    return {
      title : null,
      content : null,
    }
  },
  methods : {
    create: function () {
      // const noticedata = {
      //   title: this.title,
      //   content: this.content,
      // }
      // this.$store.dispatch("createNotice", noticeData),
      this.$router.push("/notice")
    }
  }
}
</script>