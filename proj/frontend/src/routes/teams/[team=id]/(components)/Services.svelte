<script lang="ts">
	import type { Team } from '../../../../types';
	import Service from './Service.svelte';

	export let team: Team;
</script>

{#if team.services.length === 0}
	<span class="text-lg text-slate-500">There are no services deployed for this team.</span>
{:else}
	<div class="flex flex-col gap-3">
		{#each team.services as service (`service-${service.id}`)}
			<Service {service} />
		{/each}
	</div>
{/if}
