<template>
  <h1>테스트</h1>
  <div>
    <apexchart
      width="500"
      type="bar"
      :options="chartOptions"
      :series="series"
    ></apexchart>
  </div>

</template>

<script>
import VueApexCharts from "vue3-apexcharts";

export default {
  name: 'DayGraph',
  components: {
    apexchart: VueApexCharts,
  },
  data: function() {
    return {
      chartOptions: {
        chart: {
          id: "vuechart-example",
        },
        xaxis: {
          categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998],
        },
      },
      series: [
        {
          name: "series-1",
          data: [30, 40, 35, 50, 49, 60, 70, 91],
        },
      ],
    };
  },

}
</script>

<style>

</style>