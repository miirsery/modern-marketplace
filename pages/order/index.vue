<template>
  <div class="step-1">
    <h1>Order step 1</h1>
    <v-row>
      <v-col cols="7">
        <v-col>
          <v-row class="step-1__top">
            <h3 class="step-1__text">
              Payment method
            </h3>
            <v-btn
                class="ma-2"
                outlined
                color="indigo"
            >
              All
            </v-btn>
          </v-row>
        </v-col>
        <div class="step-1__cards">
          <div class="step-1__card">
            <div>Sber</div>
            <div>
              <span>** 1234</span>
              <span>VISA</span>
            </div>
          </div>
          <div class="step-1__card">
            <span>New card</span>
          </div>
          <div class="step-1__card">
            <span>More</span>
          </div>
        </div>
        <div class="step-1__delivery">
          <h3>Delivery</h3>
          <div class="step-1__top">
            <h3 class="step-1__text">
              Method of obtaining
            </h3>
            <v-card-actions>
              <v-btn
                  class="ma-2"
                  outlined
                  color="indigo"
              >
                All
              </v-btn>
              <v-btn
                  class="ma-2"
                  outlined
                  color="indigo"
              >
                By courier
              </v-btn>
            </v-card-actions>

          </div>
        </div>
      </v-col>
      <v-col cols="4">
        <nuxt-link to="/order/step3">
          <v-btn
              depressed
              color="primary"
          >
            Pay online
          </v-btn>
        </nuxt-link>
      </v-col>
    </v-row>
  </div>
</template>
