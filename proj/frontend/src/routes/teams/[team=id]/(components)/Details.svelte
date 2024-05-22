<script lang="ts">
	import type { Team } from '../../../../types';

	export let team: Team;
</script>

<article class="flex flex-col">
	<div class="flex gap-4">
		{#if team.createdAt}
			<span>
				Created at: {team.createdAt}
			</span>
		{/if}
		{#if team.updatedAt}
			<span>
				Last updated at: {team.updatedAt}
			</span>
		{/if}
	</div>
	<p class="text-lg">
		<span class="text-slate-500 opacity-75">Number of services:</span>
		<span class="font-bold text-gray-500">{team.services.length}</span>
	</p>
	<p class="text-lg">
		<span class="text-slate-500 opacity-75">Internal Company CIDR block:</span>
		<span class="font-bold text-gray-500">{team.cidr}</span>
	</p>
</article>
