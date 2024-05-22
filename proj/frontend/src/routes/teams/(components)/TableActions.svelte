<script lang="ts">
	import Ellipsis from 'lucide-svelte/icons/ellipsis';
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import { Button } from '$lib/components/ui/button';
	import { toast } from 'svelte-sonner';
	import type { Team } from '../../../types';
	import { goto } from '$app/navigation';

	export let team: Team;
</script>

<DropdownMenu.Root>
	<DropdownMenu.Trigger asChild let:builder>
		<Button variant="ghost" builders={[builder]} size="icon" class="relative h-8 w-8 p-0">
			<span class="sr-only">Open menu</span>
			<Ellipsis class="h-4 w-4" />
		</Button>
	</DropdownMenu.Trigger>
	<DropdownMenu.Content>
		<DropdownMenu.Group>
			<DropdownMenu.Label>Actions</DropdownMenu.Label>
			<DropdownMenu.Item
				on:click={async () => {
					const toastId = toast.info(`Deleting ${team.name}`, {
						description: new Date().toLocaleString()
					});

					// TODO: Implement team deletion service/API call, dismiss on response.
					await new Promise((resolve) => setTimeout(resolve, 2000));

					toast.info(`Deleted ${team.name}`, {
						description: new Date().toLocaleString()
					});
					toast.dismiss(toastId);

					// FIXME: is this needed?
					await goto('/');
				}}
				class="text-red-500 accent-red-500 hover:text-accent"
			>
				<!-- TODO: make the text change color to red when hovered -->
				Delete team
			</DropdownMenu.Item>
			<DropdownMenu.Item>
				<a href="/teams/{team.id}">Open team</a>
			</DropdownMenu.Item>
		</DropdownMenu.Group>
	</DropdownMenu.Content>
</DropdownMenu.Root>
