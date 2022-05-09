<template>
  <h1>여기는 대시보드</h1>
  <p>아래에 컴포넌트들을 만들어주세요 ㅎㅎ</p>
  <real-time-graph />
  <day-graph />
</template>

<script>
import RealTimeGraph from "@/components/dashboard/RealTimeGraph.vue"
import DayGraph from '../components/dashboard/DayGraph.vue'

export default {
  components: {RealTimeGraph, DayGraph}
}