<script setup>
    import Sidebar from './components/Sidebar.vue'
	import Header from './components/Header.vue'
</script>

<template>
    <div class="app">
		
        <Sidebar v-if="this.$route.name != 'Login'"/>
		<div class="w-100">
			<Header v-if="this.$route.name != 'Login'"/>
			<router-view/>
		</div>
    </div>
</template>

<style lang= "scss">
:root {
	--primary: #4ade80;
	--primary-alt: #22c55e;
	--grey: #64748b;
	--grey-alt: #5f6b7c;
	--dark: #1e293b;
	--dark-alt: #334155;
	--light: #f1f5f9;
	--sidebar-width: 300px;
}

* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	font-family: 'Fira sans', sans-serif;
}

body {
	background: var(--light);
}

button {
	cursor: pointer;
	appearance: none;
	border: none;
	outline: none;
	background: none;
}

.app {
	display: flex;

	main {
		flex: 1 1 0;
		padding: 2rem;

		@media (max-width: 1024px) {
			padding-left: 6rem;
		}
	}
}

</style>
