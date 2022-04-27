<template>
  <div class="notice">
    <h1>This is an notice page</h1>
    <button @click="create" type="button">글작성</button>
  </div>
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
      <tr>
        <th scope="row">1</th>
        <td>Mark</td>
        <td>Otto</td>
        <td>@mdo</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  name : 'NoticeView',

  methods : {
    create () {
      this.$router.push('/notice/create')
    }
  }
}
</script>