<template>
  <div class="wrapper">
    <p>업장 리스트</p>
    <ul >
      <li v-for="item in state.shoplist" :key="item"><a href="">{{item}}</a></li>
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
      shoplist: ["대림 목욕탕", "궁중 목욕탕", "테스트 목욕탕"],
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
  .wrapper {
    border: 1px solid rgb(150, 150, 150);
    border-radius: 20px;
    margin-top: 20px;
    width: 300px;
    height: 300px;
    p {
      font-size: 18px;
      font-weight: bold;

    }
  }

  ul {
    list-style: none;
    li{
      &:hover {
          color: red;
          list-style: disc;
        }
      a{
        text-decoration: none;
        color:rgb(75, 75, 75);
        font-weight: bold;
        &:hover {
          color: red;
        }
      }
    }
  }
</style>