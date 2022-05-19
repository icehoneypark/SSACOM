<template>
  <div>
    <apexchart type="line" height="350" :options="options" :series="series"></apexchart>
  </div>
  <button type="button" class="btn btn-primary" @click="getData">데이터 변경</button>
</template>

<script>
import { reactive } from '@vue/reactivity'
import VueApexCharts from 'vue3-apexcharts'

export default {
  components: {
    apexchart: VueApexCharts,
  },

  setup() {
    // const state = reactive({
    //   data1: [15,32,22,45,11,22,33,44,8],
    //   data2: [23,11,33,4,5,6,4,8,4],
    // })
    const series = reactive([
      {
        name: "남자",
        data: [15,32,22,45,11,22,33,44,8]
      },
      {
        name: "여자",
        data: [23,11,33,4,5,6,4,8,4]
      }
    ])
    const options = {
      chart: {
        height: 350,
        type: 'line',
        dropShadow: {
          enabled: true,
          color: '#000',
          top: 18,
          left: 7,
          blur: 10,
          opacity: 0.2
        },
        toolbar: {
          show: false
        }
      },
      colors: ['#77B6EA', '#545454'],
      dataLabels: {
        enabled: true,
      },
      stroke: {
        curve: 'smooth'
      },
      title: {
        text: 'Temperature / Humidity',
        align: 'left'
      },
      grid: {
        borderColor: '#e7e7e7',
        row: {
          colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
          opacity: 0.5
        },
      },
      markers: {
        size: 1
      },
      xaxis: {
        categories: ['01시', '02시', '03시', '04시', '05시', '06시', '07시', '08시', '09시'],
        title: {
          text: '시각'
        }
      },
      yaxis: {
        title: {
          text: '방문자'
        },
        min: 0,
        max: 50
      },
      legend: {
        position: 'top',
        horizontalAlign: 'right',
        floating: true,
        offsetY: -25,
        offsetX: -5
      }
    }

    const getData = () => {
      series[0].data = [15,22,23,24,25,36,24,28,14]
      // series[0].data = [state.data1]
      // console.log(series[0].data)
    }

    
          
          

    return {options, series, getData}
  }
}
</script>

<style>

</style>