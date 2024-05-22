<script lang="ts">
	import type { PageData } from './$types';
	import * as Tabs from '$lib/components/ui/tabs';
	import TeamDetails from './(components)/Details.svelte';
	import TeamServices from './(components)/Services.svelte';
	import { Button } from '$lib/components/ui/button';
	import { toast } from 'svelte-sonner';
	import { goto } from '$app/navigation';
	import * as AlertDialog from '$lib/components/ui/alert-dialog';

	export let data: PageData;

	$: team = data.team!;
</script>

<div class="mx-2 my-10 px-2 py-10 lg:mx-28 lg:px-28">
	<header class="flex justify-between">
		<div class="flex flex-col">
			<h2 class="text-2xl">
				{team.name}
			</h2>
			{#if team.description}
				<p class="text-slate-500">{team.description}</p>
			{/if}
		</div>
		<div class="">
			<AlertDialog.Root>
				<AlertDialog.Trigger asChild let:builder>
					<Button
						variant="outline"
						size="sm"
						color="red"
						builders={[builder]}
						class="bg-red-500 text-white hover:bg-red-700">Delete</Button
					>
				</AlertDialog.Trigger>
				<AlertDialog.Content>
					<AlertDialog.Header>
						<AlertDialog.Title>Are you absolutely sure?</AlertDialog.Title>
						<AlertDialog.Description>
							<p>
								This action cannot be undone. This will permanently delete this team and tear down
								its associated services and resources.
							</p>
							<p>You can re-create it at a later time.</p>
						</AlertDialog.Description>
					</AlertDialog.Header>
					<AlertDialog.Footer>
						<AlertDialog.Cancel>Cancel</AlertDialog.Cancel>
						<AlertDialog.Action
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

								await goto('/');
							}}>Continue</AlertDialog.Action
						>
					</AlertDialog.Footer>
				</AlertDialog.Content>
			</AlertDialog.Root>
		</div>
	</header>
	<Tabs.Root value="details" class="flex-1">
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
</div>
