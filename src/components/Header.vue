<template>
    
  <nav class="navbar navbar-expand-lg custom-navbar w-100">
    <div class="container-fluid">
      <a class="navbar-brand text-light" href="#">{{ currentRoute }}</a>
    </div>
  </nav>
</template>
<script>
export default {
  computed: {
    currentRoute() {
      return this.$route.name;
    }
  }
}
</script>
<style>
.custom-navbar {
  background-color:var(--dark); /* Replace with your desired color */
}
</style>