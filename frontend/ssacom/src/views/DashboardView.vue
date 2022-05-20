<template>
  <h1>> Dashboard</h1>
<div class="body">
  <div class="tempgraph">
    <real-time-graph></real-time-graph>
  </div>
  <!-- <month-graph></month-graph>
  <time-graph></time-graph>
  <day-graph></day-graph> -->
</div>
</template>

<script>
// import TimeGraph from '@/components/dashboard/TimeGraph'
// import DayGraph from '../components/dashboard/DayGraph.vue'
// import MonthGraph from '@/components/dashboard/MonthGraph'
import RealTimeGraph from "../components/dashboard/RealTimeGraph.vue"

export default {
    name: 'DashboardView',
    components: {
        // TimeGraph,
        // DayGraph,
        // MonthGraph,
        RealTimeGraph
    },
    data() {

    }
  }
</script>

<style lang="scss" scoped>
  h1{
    background-color: #0C4DA2;
   text-align: left;
   padding: 20px;
   padding-left: 150px;
   margin-bottom: 1em;
   margin-top: 0;
   color: white;
   font-size: 23px;
   border-bottom-right-radius: 40px;
   margin-right: 20px;
 }

  .tempgraph {
    width: 100%;
  }

  .body {
    width: 100%;
    height: 80vh;
    padding: 40px
  }
  
</style>

