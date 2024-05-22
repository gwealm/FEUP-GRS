<script lang="ts">
	import type { PageData } from './$types';
	import * as Tabs from '$lib/components/ui/tabs';
	import TeamDetails from './(components)/Details.svelte';
	import TeamServices from './(components)/Services.svelte';

	export let data: PageData;

	$: team = data.team!;
</script>

<header>
	<h2 class="text-2xl">
		{team.name}
	</h2>
	{#if team.description}
		<p class="text-slate-500">{team.description}</p>
	{/if}
</header>
<Tabs.Root value="details" class="">
	<Tabs.List>
		<Tabs.Trigger value="details">Details</Tabs.Trigger>
		<Tabs.Trigger value="services">Services</Tabs.Trigger>
	</Tabs.List>
	<Tabs.Content value="details">
		<TeamDetails {team} />
	</Tabs.Content>
	<Tabs.Content value="services">
		<TeamServices {team} />
	</Tabs.Content>
</Tabs.Root>
