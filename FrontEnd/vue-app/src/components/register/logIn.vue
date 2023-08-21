<template>
    <v-card elevation="5" id="v-card_login" >
        <img src="../../assets/logoBook.png" alt="" class="img_logo" />
        <h2 class="v-card_title">Welcome Back!</h2>
        <h6 class="v-cart_title">Please enter your details</h6>
        <v-form @submit.prevent="submit" v-model="valid" ref="formLogIn">
          <v-text-field
            v-model="user.username"
            label="E-mail"
            required
            :rules="emailRules"
          ></v-text-field>
          <v-text-field
            v-model="user.password"
            label="Password"
            required
            :rules="passwordRules"
          ></v-text-field>

          <v-btn
            id="v-form_button"
            class="mr-4"
            @click="submit"
            block
            style="background-color: rgba(15, 14, 14, 0.847; color: white;  text-transform: capitalize; "
          >
            Log In
          </v-btn>
          <v-btn
            id="v-form_button"
            class="mr-4"
            block
            style="text-transform: capitalize"
            >Log in With Google</v-btn
          >
          <p style="margin-top: 50px">
            Haven`t signed up?<a href="#" @click.prevent="changeStatus" >Click here</a>
          </p>
        </v-form>
      </v-card>
</template>

<script>
export default {
    data: () => ({
    valid: false,
    user:{
      username:"",
      password:"",
    },
    passwordRules: [
        v => !!v || 'Password is required',
        v => v.length>3 || 'Required 4 characters',
    ],
    emailRules: [
     v => !!v || 'E-mail is required',
     v => /^(([^<>()[\]\\.,;:\s@']+(\.[^<>()\\[\]\\.,;:\s@']+)*)|('.+'))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(v) || 'E-mail must be valid',
   ],
  }),

  methods: {
    changeStatus(){
      this.$emit('changeStatus');
    },
    submit() {
     if( this.$refs.formLogIn.validate()){
      console.log("Funciona")
      //Aqui poner codigo de la peticion http
      this.$http.post("http://127.0.0.1:8000/api/login/",this.user).then(
        response=>{
          console.log(response)
          this.$router.push({name: 'home'})
        }
      ).catch(error=>{
        console.log(error)
      })
     }
    },
   
  },
};
</script>

<style>
#v-card_login {
    border-radius: 20px;
    margin: 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .img_logo {
    width: 60px;
    height: 60px;
    margin: 10px;
  }
  .v-card_title {
    font-family: sans-serif;
  }
  #v-form_button {
    margin-top: 10px;
    border-radius: 20px;
    font-size: 13px;
  }
  .align-bottom{
    align-self: flex-end;
  }
  .content_img{
    width: 100%;
    height: 100%;
    object-fit: contain;
  }
</style>