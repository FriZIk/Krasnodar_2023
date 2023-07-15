<template>

  <div class="row justify-content-center">
    <div class="col-lg-4">
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
    </div>
    <div class="col-lg-4">
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
    </div>
    <div class="col-lg-4">
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
    </div>
    <div class="col-lg-4">
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
    </div>
    <div class="col-lg-4">
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
    </div>
    <div class="col-lg-4">
      <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
    </div>
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import { Colors } from 'chart.js';

ChartJS.register(Colors);
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
  data() {
    return {
      chartData: {
        labels: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Августа', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
        datasets: [{ data: [40, 20, 12] }],
        backgroundColor: ["red", "blue", "green"]
      },
      chartOptions: {
        responsive: true
      }
    }
  }
}
</script>