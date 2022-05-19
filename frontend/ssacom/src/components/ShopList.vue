<template>
  <div class="shoplist">
    <p>업장 리스트</p>
    <hr>
    <ul>
      <li v-for="item in state.shoplist" :key="item"><router-link to="dashboard">{{item}}</router-link></li>
    </ul>
  </div>
</template>

<script>
import { reactive } from '@vue/reactivity'
// import { onMounted } from '@vue/runtime-core'
// import axios from 'axios'

export default {
  setup() {
    // 변수
    const state = reactive({
      shoplist: ["한솔 유치원", ],
    })
    // 라이프 사이클
    // onMounted(() => {
    //   axios.get('url', )
    //   .then((res) => state.shoplist = res.data)
    // })

    return {state}
  },
}
</script>
<style lang='scss' scoped>
  .shoplist {
    border: 1px solid rgb(150, 150, 150);
    padding: 20px;
    background-color: white;
    border-radius: 20px;
    // margin-top: 20px;
    width: 300px;
    height: 650px;
    p {
      text-align: center;
      font-size: 25px;
      font-weight: bold;
      margin-bottom: 35px;
      margin-top: 15px

    }
  }

  ul {
    list-style: none;
    overflow: auto;
    li{
      &:hover {
          color: red;
          list-style: disc;
        }
      a{
        text-decoration: none;
        color:rgb(75, 75, 75);
        font-weight: bold;
        transition: all 0.4s;
        &:hover {
          color: red;
        }
      }
    }
  }
</style>