<template>
  <div class="notice">
    <h1>detail page</h1>
  </div>
  {{ index }}
</template>

<script>
import { mapState } from 'vuex';

export default {
  name : 'NoticeDetail',
  data : function () {
    return {
      index: this.$route.params.id
    }
  },
  computed: {
    ...mapState(["posts"]),
    post : function () {
      return this.posts.find(post => post.id === this.index)
    }
  },
}
</script>