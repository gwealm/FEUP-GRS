<script lang="ts">
	let loggedIn = false;
	import Icon from './Icon.svelte';
	import { Button } from '$lib/components/ui/button';

	import { Separator } from '$lib/components/ui/separator';
</script>

<div class="flex items-center gap-2">
	{#if loggedIn}
		<p>You are logged in!</p>
		<Separator orientation="vertical" />
		<Button on:click={() => (loggedIn = true)}>Sign Up</Button>
	{:else}
		<Button on:click={() => (loggedIn = true)}>Sign In</Button>
		<Separator orientation="vertical" />
		<Button on:click={() => (loggedIn = false)}>Sign Out</Button>
	{/if}
</div>
