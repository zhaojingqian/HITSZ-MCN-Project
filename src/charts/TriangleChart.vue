<template>
  <v-chart
    class="triangle_chart"
    :option="updateOption(triangleData)"
    autoresize
  />
</template>

<script setup>
import {computed} from 'vue'
import { use } from 'echarts/core'
import { BarChart } from 'echarts/charts'
import { TitleComponent, TooltipComponent, GridComponent } from 'echarts/components'
import { CanvasRenderer } from 'echarts/renderers'
import VChart from 'vue-echarts'
import { useDataStore } from '../stores/data.js'
use([TitleComponent, TooltipComponent, GridComponent, BarChart, CanvasRenderer])

const dataStore = useDataStore()
const triangleData = computed(() => dataStore.getTriangleData())

const updateOption = (triangleData) => {
  return {
    title: {
      text: 'Triangle Distribution',
      left: 'center',
      top: '5px'
    },
    tooltip: {
      trigger: 'item',
      formatter: '{b} : {c}'
    },
    xAxis: {
      type: 'category',
      name: 'Triangle',
      nameLocation: 'middle',
      nameGap: 30,
      data: triangleData.triangle
    },
    yAxis: {
      type: 'value',
      name: 'Number of Nodes',
      nameLocation: 'middle',
      nameGap: 40
    },
    series: [
      {
        name: 'Triangle',
        type: 'bar',
        data: triangleData.count
      }
    ]
  }
}
</script>
