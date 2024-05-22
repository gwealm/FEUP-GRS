<script lang="ts">
	import type { Service as IService } from '../../../types';
	import Service from './ServiceIcon.svelte';

	export let services: IService[] = [];
</script>

{#if services.length === 0}
	<span class="text-gray-500">No services deployed for this team</span>
{:else}
	<div class="flex gap-3">
		{#each services as service}
			<Service {service} />
		{/each}
	</div>
{/if}
