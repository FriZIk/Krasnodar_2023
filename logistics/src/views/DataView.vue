<template>
  <!-- Таблица с клиентами и их параметрами -->
  <h1>Данные</h1>

  <!-- Кнопки для обновления  клиентов -->
  <div style="text-align:right; margin-bottom: 10px;  margin-bottom: 10px;">
    <div class="d-grid gap-2 d-md-block ">
      <a class="btn btn-warning mr-2 me-md-2" href="#" id="navbarDarkDropdownMenuLink" role="button" aria-expanded="false"
        data-bs-toggle="modal" data-bs-target="#addData">
        Добавить
      </a>
      <a class="btn btn-danger mr-2 me-md-2" href="#" id="navbarDarkDropdownMenuLink" role="button" aria-expanded="false"
        data-bs-toggle="modal" data-bs-target="#updateModal">
        Удалить
      </a>
      <a class="btn btn-success mr-2 me-md-2" href="#" id="navbarDarkDropdownMenuLink" role="button" aria-expanded="false"
         v-on:click="fileExport()">
        Экспорт
      </a>
      <a class="btn btn-info mr-2 me-md-2" href="#" id="navbarDarkDropdownMenuLink" role="button" aria-expanded="false"
        data-bs-toggle="modal" data-bs-target="#updateModal">
        Импорт
      </a>
    </div>
  </div>

  <div class="form-group">
    <table class="table table-bordered">
      <thead>
        <tr>
          <th scope="col">Класс обслуживания</th>
          <th scope="col">Дата отбытия</th>
          <th scope="col">Станция отбытия</th>
          <th scope="col">Станция прибытия</th>
          <th scope="col">Количество мест</th>
          <th scope="col">Номер поезда</th>
          <th scope="col">Расстоние</th>
          <th scope="col">Стоимость билета</th>
          <th scope="col">Стоимость плацкарта</th>
          <th scope="col">Стоимость обслуживания</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="ticket in tickets" :key="ticket.id">
          <td>{{ ticket.serviceClass }}</td>
          <td>{{ ticket.departureDate }}</td>
          <td>{{ ticket.departureStation }}</td>
          <td>{{ ticket.arrivalStation }}</td>
          <td>{{ ticket.seatNumber }}</td>
          <td>{{ ticket.trainNumber }}</td>
          <td>{{ ticket.totalDistance }}</td>
          <td>{{ ticket.costTicket }}</td>
          <td>{{ ticket.costPlatzcard }}</td>
          <td>{{ ticket.id }}</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- Модальное окно для функции обновления -->
  <div class="modal fade" id="addData" tabindex="-1" aria-labelledby="ModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Подтверждение обновления</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <!-- <div class="modal-body">
          Вы действительно хотите обновить программное обеспечение? Пожалуйста подтвердите.
        </div> -->


        <form class="form" id="Calculation">
          <div class="form-content">
            <label for="Data">Класс обслуживания</label><br>
            <select name="select" id="Class" width="200%">
              <option value="s1">Плацкарт</option>
              <option value="s2">Купе</option>
              <option value="s3">СВ</option>
            </select>
          </div>
          <div>
            <label for="From">Дата отбытия</label><br>
            <input type="date" id="date" />
          </div>
          <div>
            <label for="To">Станция отбытия</label><br>
            <input type="text" id="from" />
          </div>
          <div>
            <label for="Class">Станция прибытия</label><br>
            <input type="text" id="to" />
          </div>
          <div>
            <label for="Count">Количество мест</label><br>
            <input type="number" id="count" />
          </div>
          <div>
            <label for="Count">Номер поезда</label><br>
            <input type="number" id="number" />
          </div>
          <div>
            <label for="Count">Расстоние</label><br>
            <input type="number" id="distance" />
          </div>
          <div>
            <label for="Count">Стоимость билета</label><br>
            <input type="number" id="cost" />
          </div>
          <div>
            <label for="Count">Стоимость плацкарта</label><br>
            <input type="number" id="count" />
          </div>
          <div>
            <label for="Count">Стоимость обслуживания</label><br>
            <input type="number" id="count" />
          </div>
        </form>

        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
          <button type="button" v-on:click="addNewData()" class="btn btn-primary"
            data-bs-dismiss="modal">Добавить</button>
        </div>
      </div>
    </div>
  </div>
</template>



<script>
import axios from 'axios'

export default {
  data() {
    return {
      tickets: [],        // Список клиентов
    }
  },

  // Получение клиентов с сервера
  created() {
    axios.get(`http://83.221.202.194:2500/backapi/tickets/`)
      .then(response => {
        this.tickets = response.data
        console.log(response.data)
        // console.log(this.getElementById("checkboxUpdater").value);
      })
      .catch(e => {
        this.errors.push(e)
      })
  },

  methods: {
    fileExport() {
      window.open('http://83.221.202.194:2500/backapi/export_exel/', '_blank', 'noreferrer');
    },
  },
}

</script>