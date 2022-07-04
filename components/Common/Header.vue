<script lang="ts" setup>
import Cookies from 'js-cookie'

import { useUserStore } from "~/store/user";
import { useCartStore } from "~/store/cart";
import { useFavoriteStore } from "~/store/favorite";

const favoriteStore = useFavoriteStore()
const userStore = useUserStore()
const cart = useCartStore()

const emit = defineEmits([
    'openLocation',
    'openCategories',
    'openAuthModal'
])

const handleOpenLocation = () => {
  emit('openLocation')
}

const handleShowCategories = () => {
  emit('openCategories')
}

const handleShowAuthModal = () => {
  emit('openAuthModal')
}

const getTotalCountProductInCart = computed(() => cart.count)
const getTotalCountProductInFavorite = computed(() => favoriteStore.count)

const logout = () => {
  Cookies.remove('token')
  location.reload()
}

onMounted(() => {
  if (Cookies.get('token')) {
    userStore.isAuthorized = true
  }
})
</script>
<template>
 <div class="header">
   <el-row class="mb-20">
     <el-col :span="12">
       <el-button class="header__search" @click="handleOpenLocation">
         <img
             class="header__search-icon"
             src="../../assets/icons/location-icon.svg"
             alt="location"
         />
         <span>Новосибирск</span>
       </el-button>
     </el-col>
   </el-row>
   <el-row>
     <el-col :span="2">
       <nuxt-link to="/">
         <img class="header__logo" src="../../assets/icons/logo-icon.svg" alt="logo" />
       </nuxt-link>
     </el-col>
     <el-col :span="2">
       <el-button type="primary" @click="handleShowCategories">
         Categories
       </el-button>
     </el-col>
     <el-col :span="11" class="mr-12">
       <common-search />
     </el-col>
     <el-col :span="8">
       <el-row class="jc-flex-end">
         <el-col :span="4" v-if="userStore.isAuthorized">
           <el-dropdown trigger="hover">
             <div class="header__profile">
                <img :src="userStore.user.avatar" alt="profile" />
             </div>
             <template #dropdown>
               <el-dropdown-menu>
                 <el-dropdown-item>
                  <nuxt-link to="/profile">Личный кабинет</nuxt-link>
                 </el-dropdown-item>
                 <el-dropdown-item>Уведомления</el-dropdown-item>
                 <el-dropdown-item>Сообщения</el-dropdown-item>
                 <el-dropdown-item>Сравнение</el-dropdown-item>
                 <el-dropdown-item divided>
                   <el-button size="small" @click="logout" class="header__logout">
                    Выход
                   </el-button>
                 </el-dropdown-item>
               </el-dropdown-menu>
             </template>
           </el-dropdown>
         </el-col>
         <el-col :span="4" v-else>
           <el-button
               class="header__profile"
               @click="handleShowAuthModal"
           >
             <img src="../../assets/images/kuriyama.jpg" alt="profile" />
           </el-button>
         </el-col>
         <el-col :span="4">
           <div class="header__icon">
             <nuxt-link to="/">
               <common-icon svg="orders-icon" className="header__icon" />
             </nuxt-link>
           </div>
         </el-col>
         <el-col :span="4">
           <div class="header__icon">
             <nuxt-link to="/">
               <el-badge :value="getTotalCountProductInFavorite" type="primary">
                 <common-icon svg="favorite-icon" className="header__icon" />
               </el-badge>
             </nuxt-link>
           </div>
         </el-col>
         <el-col :span="4">
           <div class="header__icon">
             <nuxt-link to="/cart">
               <el-badge :value="getTotalCountProductInCart" type="primary">
                 <common-icon svg="cart-icon" className="header__icon" />
               </el-badge>
             </nuxt-link>
           </div>
         </el-col>
       </el-row>
     </el-col>
   </el-row>
 </div>
</template>
<style lang="scss">
.header {
  &__search,
  &__profile {
    background: none;
    border: none;
    outline: none;
    padding: 0;

    &-icon {
      width: 24px;
      height: 24px;
    }

    &:hover,
    &:focus,
    &:focus-visible{
      background: none;
      border: none;
      outline: none;
    }
  }

  &__logo,
  &__icon {
    width: 32px;
    height: 32px;

    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }

  &__profile {
    width: 32px;
    height: 32px;

    img {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      object-fit: cover;
    }
  }
}
</style>
