<template>
  <h2>여기는 월별 그래프_지원</h2>

  <div>
    <apexchart width="1000" type="bar"
    :options="options" :series="series">
    </apexchart>
  </div>
</template>

<script>
import VueApexCharts from "vue3-apexcharts"

export default {
  name: 'MonthGraph',
  components:{
    apexchart: VueApexCharts
  },
  setup() {
    const options = {
      chart: { id: 'vuechart-example'},
      xaxis: {
        categories: [
          "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
      }
    }

    const series = [
      { name: 'male',
        data: [230, 220, 210, 198, 172, 196, 241, 287, 269, 210, 202, 221]
      },
      { name: 'female',
        data: [228, 230, 198, 172, 188, 230, 270, 271, 254, 230, 212, 189]
      }
    ]
    return {options, series}
  }

}
</script>

<style>

</style>