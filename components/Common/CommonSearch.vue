<template>
  <div class="common-search">
    <input class="common-search__input" type="text" placeholder="Start a search..." />
  </div>
</template>

<style scoped lang="scss">
.common-search {
  width: 100%;
  margin: 0 5px;
  height: 40px;
  border: 2px solid $color-accent;

  &__input {
    padding-left: 8px;
    width: 100%;
    height: 100%;
    outline: none;

    &::placeholder {
      padding-left: 8px;
    }
  }
}
</style>