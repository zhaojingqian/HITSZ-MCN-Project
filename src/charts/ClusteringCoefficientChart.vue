<template>
    <v-chart
      class="clustering_coefficient_chart"
      :option="updateOption(clusteringCoefficientData)"
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
  const clusteringCoefficientData = computed(() => dataStore.getClusteringCoefficientData())
  
  const updateOption = (clusteringCoefficientData) => {
    return {
      title: {
        text: 'Clustering Coefficient Distribution',
        left: 'center',
        top: '5px'
      },
      tooltip: {
        trigger: 'item',
        formatter: '{b} : {c}'
      },
      xAxis: {
        type: 'category',
        name: 'Clustering Coefficient',
        nameLocation: 'middle',
        nameGap: 30,
        data: clusteringCoefficientData.clustering_coefficient
      },
      yAxis: {
        type: 'value',
        name: 'Number of Nodes',
        nameLocation: 'middle',
        nameGap: 40
      },
      series: [
        {
          name: 'Clustering Coefficient',
          type: 'bar',
          data: clusteringCoefficientData.count
        }
      ]
    }
  }
  </script>
  