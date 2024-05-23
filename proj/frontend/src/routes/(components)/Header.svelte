<script lang="ts">
	import Icon from './Icon.svelte';
	import { page } from '$app/stores';
	import Auth from './Auth.svelte';
</script>

<header class="flex h-20 items-center justify-between bg-gray-500 p-5">
	<div class="flex items-center gap-5">
		<Icon name="cloud" height="2em" width="2em" />
	</div>
	<Auth />
</header>
