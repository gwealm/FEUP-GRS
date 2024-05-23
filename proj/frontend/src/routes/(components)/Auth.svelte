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
		<Button on:click={() => (loggedIn = true)}><a href="#">Sign Up</a></Button>
	{:else}
		<Button><a href="/login">Sign In</a></Button>
		<Separator orientation="vertical" />
		<Button on:click={() => (loggedIn = false)}><a href="#">Sign Out</a></Button>
	{/if}
</div>
