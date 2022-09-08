<template>
  <div class="login">
    <body>
      <form class="box" action="login.html" method="POST">
        <h1>Login</h1>
        <input type="email" name="" placeholder="Enter Email" id="email" />
        <input
          type="password"
          name=""
          placeholder="Enter password"
          id="password"
        />
        <input type="submit" name="" value="Login" />
        <!-- <a href="{{url_for('register')}}">Don't have an account? Sign up</a><br> -->
      </form>
    </body>
  </div>
</template>
<script>
export default {
  name: "LoginVue",
};
</script>
<style lang="scss">
body {
  margin: 0;
  padding: 0;
  font-family: 1.6rem/1.25 "Helvetica Neue", Helvetica, Arial, sans-serif;
  background-color: #f5f5f5;
}

.box {
  width: 300px;
  padding: 30px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: rgba(0, 0, 0, 0.4);
  text-align: center;
}

.box h1 {
  color: white;
  text-transform: uppercase;
  font-weight: 700;
}

.box input[type="text"],
.box input[type="password"] {
  border: 0;
  background: none;
  display: block;
  margin: 20px auto;
  text-align: center;
  border: 3px solid #0367fd;
  padding: 14px 10px;
  width: 220px;
  outline: none;
  color: white;
  border-radius: 24px;
  transition: 0.25px;
}

.box input[type="text"]:focus,
.box input[type="password"]:focus {
  width: 270px;
  border-color: #ffc400ec;
}

.box input[type="submit"] {
  border: 0;
  background: none;
  display: block;
  margin: 20px auto;
  text-align: center;
  border: 3px solid #ffc400ec;
  padding: 14px 35px;
  outline: none;
  color: white;
  border-radius: 24px;
  transition: 0.25px;
  cursor: pointer;
}

.box input[type="submit"]:hover {
  background: #ffc400ec;
}
</style>
