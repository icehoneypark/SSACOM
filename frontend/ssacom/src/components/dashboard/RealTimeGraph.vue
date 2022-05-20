<template>
  <div>
    <div class="wrapper">
      <h5>재실 데이터 측정</h5>
      <img v-if="state.result <= 0.5" src="../../assets/bus_no.png" width="250" alt="">
      <img v-if="state.result > 0.5" src="../../assets/bus_yes.png" width="250" alt="">

      <span class="text">버스의 색깔을 통해 내부 재실 정보를 알 수 있습니다. 빨간 버스가 재실 중임을 나타냅니다.</span>
    </div>
    <apexchart type="line" height="350" :options="options" :series="series"></apexchart>
  </div>
</template>

<script>
import { reactive } from '@vue/reactivity'
import VueApexCharts from 'vue3-apexcharts'
import axios from 'axios'
import { onMounted, onUnmounted } from '@vue/runtime-core'

const baseURL = 'http://127.0.0.1:8000/'
// const baseURL = 'http://k6s105.p.ssafy.io:8004/'

const websocket = new WebSocket("ws://localhost:8000/ws/data/");


export default {
  components: {
    apexchart: VueApexCharts,
  },

  setup() {
    const state = reactive({
      isPerson: [],
      result: 0,
    })
    
    const series = reactive([
      {
        name: "온도",
        data: [15,32,22,45,11,22,33,44,8]
      },
      {
        name: "습도",
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
          show: true,
          offsetX: 0,
          offsetY: -10,
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
          text: '온습도'
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

    // const getData = () => {
    //   series[0].data = [15,22,23,24,25,36,24,28,14]
    //   // series[0].data = [state.data1]
    //   // console.log(series[0].data)
    // }

    const getTemp = () => {
      const token = localStorage.getItem('jwt')
      console.log('온습도 데이터 load')
      axios({
        method: 'get',
        url: `${baseURL}dashboard/temp/`,
        headers: {Authorization : `JWT ${token}`},
      })
      .then((res) => {
        console.log(res)
      })
      .catch((res) => {
        console.log(res)
      })
    }
    let intervalId = setInterval(() => getTemp(), 60000)

    onMounted(() => {
      
      // const websocket = new WebSocket("ws://localhost:8000/ws/data/");

      websocket.onmessage = function (event) {
        // console.log(event.data['message']);
        state.isPerson.push(event.data.substr(12,1)*1)
        if (state.isPerson.length > 5) {
          state.isPerson.shift()
        }
        const temp = state.isPerson.reduce(function add(sum, currValue) {
          return sum + currValue;
        }, 0);
        state.result = temp / state.isPerson.length;
        console.log(state.result)
      };

      websocket.onopen = function (event) {
        console.log(event);
        console.log("Successfully connected to the echo websocket server...");
      };
      getTemp()
      setInterval(() => getTemp(), 60000)
    })

    onUnmounted(() => {
      websocket.close()
      clearInterval(intervalId)
    })

          
          

    return {options, series, state}
  }
}
</script>

<style scoped>
h5 {
  font-weight: 900;

}

img {
  border-right: 1px solid gray
}
.text {
  margin-left: 30px;
  font-size: 15px;
  color: gray;
}
.wrapper {
  background-color: rgb(216, 216, 216);
  padding: 20px;
  margin-bottom: 20px;
  height: 330px
}

</style>