<template>
  <div>
    <phone-header></phone-header>
    <img class="mode-tutorial" src="../assets/tutorial.png" />
    <router-link class="admit-btn" to="easy_menu"
      ><img src="../assets/admit-btn.png"
    /></router-link>
  </div>
</template>

<script>
import PhoneHeader from "@/components/PhoneHeader.vue";
export default {
  components: { PhoneHeader },
};
</script>

<style>
.mode-tutorial {
  width: 320px;
  margin-top: 40px;
}

.admit-btn {
  position: relative;
  bottom: 145px;
}
</style>
