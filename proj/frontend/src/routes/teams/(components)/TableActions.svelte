<script lang="ts">
	import Ellipsis from 'lucide-svelte/icons/ellipsis';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import { Button } from '$lib/components/ui/button';
	import { toast } from 'svelte-sonner';
	import type { Team } from '../../../types';
	import { goto } from '$app/navigation';
	import type { BodyRow } from 'svelte-headless-table';
	import { onMount } from 'svelte';
	import Icon from '../../(components)/Icon.svelte';

	export let team: Team;
	export let row: BodyRow<Team>;

	// TODO: figure out how to extract the row from the table data model.
	let elem: HTMLTableRowElement | null = null;
	onMount(() => {
		elem = document.querySelector(`#table-row-${row.id}`);
	});
</script>

<div class="flex w-min justify-between gap-2 px-2">
	<Button variant="ghost" size="icon" class="relative h-8 w-8 p-0" title="Open team page">
		<a href="/teams/{team.id}">
			<Icon name="external-link" height="2em" width="2em" />
		</a>
	</Button>
	<Button
		variant="ghost"
		size="icon"
		class="relative h-8 w-8 p-0 text-red-500 accent-red-500 hover:bg-red-500"
		title="Delete team"
		on:click={async () => {
			const toastId = toast.info(`Deleting ${team.name}`, {
				description: new Date().toLocaleString()
			});

			elem?.classList.toggle('blur');

			// TODO: Implement team deletion service/API call, dismiss on response.
			await new Promise((resolve) => setTimeout(resolve, 2000));

			toast.info(`Deleted ${team.name}`, {
				description: new Date().toLocaleString()
			});
			toast.dismiss(toastId);

			elem?.remove();
			// FIXME: is this needed?
			await goto('/');
		}}
	>
		<Icon name="trash" height="2em" width="2em" />
	</Button>
	<DropdownMenu.Root>
		<DropdownMenu.Trigger asChild let:builder>
			<Button variant="ghost" builders={[builder]} size="icon" class="relative h-8 w-8 p-0">
				<span class="sr-only">Other options</span>
				<Ellipsis class="h-4 w-4" />
			</Button>
		</DropdownMenu.Trigger>
		<DropdownMenu.Content>
			<DropdownMenu.Group>
				<DropdownMenu.Label>Actions</DropdownMenu.Label>
			</DropdownMenu.Group>
		</DropdownMenu.Content>
	</DropdownMenu.Root>
</div>
