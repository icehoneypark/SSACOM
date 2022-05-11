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
    v-model="state.title"
    placeholder="제목">

    <textarea
      type="text"
      v-model="state.content"
      placeholder="내용입력"
    ></textarea>
  </div>



</template>

<script>
import axios from 'axios'
import { useRouter } from "vue-router"
import { reactive } from "vue"

export default {
  name : 'NoticeCreate',
  setup() {
    const router = useRouter()
    const token = localStorage.getItem('jwt')
    const state = reactive({
      title: null,
      content: null,
    })

    const create = () => {
      const noticeData = {
        title: state.title,
        content: state.content,
      }
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/notices/',
        data: noticeData,
        headers: {Authorization : `JWT ${token}`},
      })
        .then(res => {
            console.log(res)
          })
          .catch(err => {
            console.log(err)
          })
      router.push("/notice")
    }

    return { state, create }
  }
}
</script>