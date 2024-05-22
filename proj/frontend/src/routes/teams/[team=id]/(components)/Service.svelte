<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import Button from '$lib/components/ui/button/button.svelte';
	import { toast } from 'svelte-sonner';

	import type { Service } from '../../../../types';

	export let service: Service;
</script>

<Card.Root>
	<Card.Header>
		<Card.Title>{service.name}</Card.Title>

		{#if service.description}
			<Card.Description>{service.description}</Card.Description>
		{/if}
	</Card.Header>
	<Card.Content>
		<ul class="flex flex-col">
			{#if service.deployedAt}
				<li class="">
					<span class="text-slate-500 opacity-75">Deployed at</span>
					<span class="font-bold text-gray-500">{service.ipAddress}</span>
				</li>
			{/if}
			<li class="">
				<span class="text-slate-500 opacity-75">Deployed at</span>
				<span class="font-bold text-gray-500">{service.ipAddress}</span>
			</li>
		</ul>
	</Card.Content>
	<Card.Footer class="justify-end"
		><Button
			variant="outline"
			size="sm"
			color="red"
			class="bg-red-500 text-white hover:bg-red-700"
			on:click={() => {
				const toastId = toast.info(`Tearing down service ${service.name}`, {
					description: new Date().toLocaleString()
				});

				// TODO: Implement tearing down service/API call, dismiss on response.
				setTimeout(() => {
					toast.info(`Torn down service ${service.name}`, {
						description: new Date().toLocaleString()
					});
					toast.dismiss(toastId);
				}, 2000);
			}}>Tear down</Button
		></Card.Footer
	>
</Card.Root>
