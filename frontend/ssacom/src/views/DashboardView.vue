<template>
  <h1>여기는 대시보드</h1>
  <p>아래에 컴포넌트들을 만들어주세요 ㅎㅎ</p>
  <time-graph></time-graph>
  <day-graph></day-graph>
</template>

<script>
import TimeGraph from '@/components/dashboard/TimeGraph.vue'
import DayGraph from '../components/dashboard/DayGraph.vue'

export default {
    name: 'DashboardView',
    components: {
        TimeGraph,
        DayGraph
    },
    data() {

    }
  }
</script>

<style>

</style>