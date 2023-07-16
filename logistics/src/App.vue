<template>
  <div class="span-col-10" styles="padding: 0 20px; box-sizing: border-box;">
    <nav class="navbar navbar-dark bg-dark">
      <div>
        <a class="navbar-brand" href="">
          <img src="../src/assets/new_rgd.png" width="100" height="40" class="d-inline-block alighn-top" alt="">
          <!-- --<strong> Веб-интерфейс рекомендательной системы</strong> -->
        </a>
        <a ><img src="../src/assets/new_icon_comand.png" width="160" height="40" class="d-inline-block alighn-top"
            alt=""></a>
      </div>

      <b-nav-item><i class="fa fa-user fa-lg" style="color:white"></i><router-link to="/"> Расчёт
        </router-link> </b-nav-item>
      <b-nav-item><i class="fa fa-list fa-lg" style="color:white"></i><router-link to="/data"> Данные
        </router-link> </b-nav-item>
      <b-nav-item><i class="fa fa-book fa-lg" style="color:white"></i><router-link to="/analytics"> Аналитика
        </router-link> </b-nav-item>
      <b-nav-item><i class="fa fa-book fa-lg" style="color:white"></i><router-link to="/about"> О нас
        </router-link> </b-nav-item>


      <form class="form-inline my-2 my-lg-0">
        <input class="form-control mr-sm-2" type="search" placeholder="Поиск билета" aria-label="Search">
      </form>

    </nav>


  </div>

  <router-view />
</template>

<style>
#hero .btn-get-started {
  font-family: "Jost", sans-serif;
  font-weight: 500;
  font-size: 16px;
  letter-spacing: 1px;
  display: inline-block;
  padding: 10px 28px 11px 28px;
  border-radius: 50px;
  transition: 0.5s;
  margin: 10px 0 0 0;
  color: #fff;
  background: #47b2e4;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #FFFFFF;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #D77D31;
}
</style>

