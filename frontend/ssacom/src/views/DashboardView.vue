<template>
  <h1>여기는 대시보드</h1>
  <p>아래에 컴포넌트들을 만들어주세요 ㅎㅎ</p>
  <time-graph></time-graph>
  <day-graph></day-graph>
  <month-graph></month-graph>
</template>

<script>
import TimeGraph from '@/components/dashboard/TimeGraph'
import DayGraph from '../components/dashboard/DayGraph.vue'
import MonthGraph from '@/components/dashboard/MonthGraph'

export default {
    name: 'DashboardView',
    components: {
        TimeGraph,
        DayGraph,
        MonthGraph
    },
    data() {

    }
  }
</script>

<style>

</style>