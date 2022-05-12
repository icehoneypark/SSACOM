<template>
  <h2>여기는 시간별 그래프_지원</h2>

  <div class="d-flex justify-content-center">
    <apexchart width="500" type="line" 
      :options="options" :series="series">
    </apexchart>  
  </div>
</template>

<script>
import VueApexCharts from "vue3-apexcharts";

export default {
  name: 'TimeGraph',
  props: {},
  components: {
    apexchart: VueApexCharts
  },
  data: () => ({
    options: {
      chart: {
        id: 'vuechart-example'
      },
      xaxis: {
        categories: [ // 카테고리는 하드코딩 오케이(시간은 정해져있으니까)
          "자", "축", "인", "묘", "진", "사",
          "오", "미", "신", "유", "술", "해"
        ]
      }
    },
    series: [{
      name: 'male',
      data: [55, 62, 89, 66, 98, 72, 101, 75, 94, 120, 117, 139]
    },
    { name: 'female',
      data: [44, 23, 55, 66, 77, 99, 29, 44, 68, 130, 121, 93]
    }
    ]
  }),
  created: function(){},    // 나중에 대시보드 페이지 열릴 때 계산해서 값을 집어넣을 예정
  // seires 자체를 수정하는 방식으로 그래프를 그려야 함
  
}
</script>

<style>

</style>