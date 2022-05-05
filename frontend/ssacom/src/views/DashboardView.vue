<template>
  <h1>여기는 대시보드</h1>
  <p>아래에 컴포넌트들을 만들어주세요 ㅎㅎ</p>
  <time-graph></time-graph>
</template>

<script>
import TimeGraph from '@/components/dashboard/TimeGraph.vue'

export default {
    name: 'DashboardView',
    components: {
        TimeGraph,
    },
    data() {

    }


}
</script>

<style>

</style>