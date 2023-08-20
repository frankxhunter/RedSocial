<template>
  <div class="content">
    <v-sheet
      class="sheet"
      color="grey darken-1"
      elevation="18"
      height="500"
      width="900"
    >
      <div class="content_img"></div>

      <v-row justify="center" >
        <v-col cols="12" sm="12" class="mx-1" >
          <v-card elevation="5" id="v-card_login" height="95%">
            <img src="../assets/logoBook.png" alt="" class="img_logo" />
            <h2 class="v-card_title">Welcome Back!</h2>
            <h6 class="v-cart_title">Please enter your details</h6>
                <form>
                  <v-text-field
                    v-model="email"
                    :error-messages="emailErrors"
                    label="E-mail"
                    required
                    @input="$v.email.$touch()"
                    @blur="$v.email.$touch()"
                  ></v-text-field>
                  <v-text-field
                    v-model="email"
                    :error-messages="emailErrors"
                    label="Password"
                    required
                    @input="$v.email.$touch()"
                    @blur="$v.email.$touch()"
                  ></v-text-field>

                  <v-btn
                    id="v-form_button"
                    class="mr-4"
                    @click="submit"
                    block
                    style="background-color: rgba(15, 14, 14, 0.847; color: white;  text-transform: capitalize "
                  >
                    Log In
                  </v-btn>
                  <v-btn
                    id="v-form_button"
                    block
                    style="text-transform: capitalize"
                    >Log in With Google</v-btn
                  >
                  <p>Haven`t signed up?<a href="" style="margin-top: 50px;">Clic here</a></p>
                </form>
          </v-card>
        </v-col>
      </v-row>
    </v-sheet>
  </div>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, maxLength, email } from "vuelidate/lib/validators";

export default {
  mixins: [validationMixin],

  validations: {
    email: { required, email },
    select: { required },
  },

  data: () => ({
    email: "",
    select: null,
  }),

  computed: {
    selectErrors() {
      const errors = [];
      if (!this.$v.select.$dirty) return errors;
      !this.$v.select.required && errors.push("Item is required");
      return errors;
    },
    nameErrors() {
      const errors = [];
      if (!this.$v.name.$dirty) return errors;
      !this.$v.name.maxLength &&
        errors.push("Name must be at most 10 characters long");
      !this.$v.name.required && errors.push("Name is required.");
      return errors;
    },
    emailErrors() {
      const errors = [];
      if (!this.$v.email.$dirty) return errors;
      !this.$v.email.email && errors.push("Must be valid e-mail");
      !this.$v.email.required && errors.push("E-mail is required");
      return errors;
    },
  },

  methods: {
    submit() {
      this.$v.$touch();
    },
    clear() {
      this.$v.$reset();
      this.name = "";
      this.email = "";
      this.select = null;
      this.checkbox = false;
    },
  },
};
</script>

<style>
.content {
  border: 1px solid rgb(15, 14, 14);
  height: 100%;
  width: 100%;
  background-color: rgba(15, 14, 14, 0.847);
  display: flex;
}

.sheet {
  margin: auto;
  border-radius: 20px;
  margin-top: 50px;
  margin-bottom: 50px;
  display: grid;
  grid-template-columns: minmax(150px, 2fr) minmax(200px, 1.3fr);
}

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
  font-family: "Ace Sans";
}
#v-form_button {
  margin-top: 10px;
  border-radius: 20px;
  font-size: 13px;
}
</style>