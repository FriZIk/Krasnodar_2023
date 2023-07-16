<script setup>
// import AppLayout from '@/Layouts/AppLayout.vue';
import * as bootstrap from 'bootstrap';
// import { Head, Link, useForm } from '@inertiajs/inertia-vue3';
import { reactive, onMounted } from 'vue'

const state = reactive({
  modal_demo: null,
  clients: [],

  client_editing: null,
  client: {
    name: null
  },
})


onMounted(() => {
  state.modal_demo = new bootstrap.Modal('#modal_demo', {})

  state.modal_demo._element.addEventListener('hide.bs.modal', () => {
    state.client_editing = null
    state.client = { name: null }
  })
})


function createClient_init() {
  state.client_editing = null
  state.client = { name: null }

  state.modal_demo.show()
}

function closeModal() {
  state.modal_demo.hide()
}
</script>


<template>
  <div class="home">
    <!-- <h1>Список клиентов</h1> -->

    <section id="hero" class="d-flex align-items-center">

      <div class="container">
        <div class="row">
          <div class="col-lg-6 d-flex flex-column justify-content-center pt-4  pt-lg-0 order-2 order-lg-2"
            data-aos="fade-up" data-aos-delay="200">
            <h1>Адаптивная рекомендательная система</h1>

            <h2>Эффективное планирование и оптимизация процессов на железнодорожном транспорте</h2>
            <!-- <a href="#about" class="btn-get-started scrollto ">Рассчитать стоимость поездки</a> -->
            <button type="button" href="#about" class="btn-get-started scrollto" @click="createClient_init">
              Рассчитать стоимость поездки
            </button>
          </div>
          <div class="col-lg-6 order-1 order-lg-2 hero-img" data-aos="zoom-in" data-aos-delay="200">
            <img src="../assets/train.png" class="img-fluid animated" alt="">
          </div>
        </div>
      </div>
    </section>
  </div>



  <!-- ======= Footer ======= -->
  <footer id="footer">
    <div class="footer-newsletter">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-4">
            <h4>Кроссплатформенность<img src="../assets/pic1.png" width="150" height="150"
                class="d-inline-block alighn-top" alt=""></h4>
            <p>Рассчитанная стоимость поездки по выбранному маршруту</p>
          </div>
          <div class="col-lg-4">
            <h4>Автоматизированная аналитика<img src="../assets/pic2.png" width="150" height="150"
                class="d-inline-block alighn-top" alt=""></h4>
            <p>Рассчитанная стоимость поездки по выбранному маршруту</p>
          </div>
          <div class="col-lg-4">
            <h4>Анализ данных из открытых источников<img src="../assets/pic3.png" width="150" height="150"
                class="d-inline-block alighn-top" alt=""></h4>
            <p>Рассчитанная стоимость поездки по выбранному маршруту</p>
          </div>
          <div class="col-lg-4">
            <h4>Масштабируемость<img src="../assets/pic4.png" width="150" height="150" class="d-inline-block alighn-top"
                alt=""></h4>
            <p>Рассчитанная стоимость поездки по выбранному маршруту</p>
          </div>
        </div>
      </div>
    </div>


  </footer>
  <AppLayout title="Modal Demo">

    <!-- Modal -->
    <div class="modal fade" id="modal_demo" tabindex="-1" aria-labelledby="modal_demo_label" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="modal_demo_label">
              <span>Расчёт</span>
            </h5>
          </div>
          <div class="row justify-content-center">
            <div class="col-lg-5">


              <form class="form" id="Calculation">
                <div class="form-content">
                  <label for="Data">Дата</label><br>
                  <input type="date" id="date" />
                </div>
                <div>
                  <label for="From">Откуда</label><br>
                  <input type="text" id="from" width="200%" />
                </div>
                <div>
                  <label for="To">Куда</label><br>
                  <input type="text" id="to" />
                </div>
                <div>
                  <label for="Class">Выбирите класс обслуживания</label><br>
                  <select name="select" id="Class" width="200%">
                    <option value="s1">Плацкарт</option>
                    <option value="s2">Купе</option>
                    <option value="s3">СВ</option>
                  </select>
                </div>
                <div>
                  <label for="Count">Количество билетов</label><br>
                  <input type="number" id="count" />
                </div>
              </form>

            </div>
            <div class="col-lg-5">
              <!-- <h4>Результат вычислений</h4> -->
              <p>Рассчитанная стоимость поездки по выбранному маршруту</p>
              <form action="" method="post">
                <input type="email" name="email" id="result">
              </form>
            </div>
          </div>
          <div class="modal-body">


          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" v-on:click="closeModal">Отмена</button>
            <button type="button" class="btn btn-primary" refs="my_input" v-on:click="GetConfigurationFile()">Провести
              расчёт </button>
          </div>
        </div>
      </div>
    </div>

  </AppLayout>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      tickets: [],        // Список клиентов
    }
  },

  methods: {
    GetConfigurationFile() {
      var date = document.getElementById("date");
      var from = document.getElementById("from");
      var to = document.getElementById("to");
      var Class = document.getElementById("Class");
      var count = document.getElementById("count");

      console.log(date.value);
      console.log(from.value);
      console.log(to.value);
      console.log(Class.value);
      console.log(count.value);

      axios.get("http://83.221.202.194:2500/backapi/get_configuration_file?date=" + date.value + "&from=" + from.value + "&to=" + to.value + "&Class=" + Class.value + "&count=" + count.value)
        .then((response) => {
          console.log(response);
          var result = document.getElementById("result");
          result.value = response.data;
          console.log(result.value)
        })
        .catch((errors) => {
          console.log(errors); // Errors
        });
    }
  },

  computed: {
  }
};
</script>