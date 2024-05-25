<script lang="ts">
	import * as AlertDialog from '$lib/components/ui/alert-dialog';
	import { Button } from '$lib/components/ui/button/';
	import * as Form from '$lib/components/ui/form';
	import { Input } from '$lib/components/ui/input';
	import { superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import Icon from '../(components)/Icon.svelte';
	import type { PageData } from './$types';
	import DataTable from './(components)/Table.svelte';
	import { CreateTeamSchema } from './schemas';

	export let data: PageData;

	const form = superForm(data.form, {
		validators: zodClient(CreateTeamSchema)
	});

	const { form: formData, enhance } = form;

	$: teams = data.teams;
</script>

<header class="mb-5 flex w-full justify-between">
	<h1 class="text-xl">Your organization's teams:</h1>
	<AlertDialog.Root>
		<AlertDialog.Trigger asChild let:builder>
			<Button
				variant="outline"
				size="sm"
				color="red"
				builders={[builder]}
				class="bg-red-500 text-white hover:bg-red-700"
				title="Create new team"
			>
				<Icon name="plus" />
			</Button>
		</AlertDialog.Trigger>
		<AlertDialog.Content>
			<AlertDialog.Header>
				<AlertDialog.Title>Create new team</AlertDialog.Title>
			</AlertDialog.Header>
			<form method="POST" use:enhance action="/teams?/create">
				<Form.Field {form} name="name">
					<Form.Control let:attrs>
						<Form.Label>Name</Form.Label>
						<Input {...attrs} bind:value={$formData.name} required />
					</Form.Control>
					<Form.FieldErrors />
				</Form.Field>
				<Form.Field {form} name="description">
					<Form.Control let:attrs>
						<Form.Label>Password</Form.Label>
						<Input {...attrs} bind:value={$formData.description} />
					</Form.Control>
					<Form.FieldErrors />
				</Form.Field>
				<!-- FIXME: this looks weird -->
				<AlertDialog.Footer>
					<AlertDialog.Cancel>Cancel</AlertDialog.Cancel>
					<AlertDialog.Action
						on:click={async () => {
							console.log('boas');
						}}
						asChild><Form.Button>Create</Form.Button></AlertDialog.Action
					>
				</AlertDialog.Footer>
			</form>
		</AlertDialog.Content>
	</AlertDialog.Root>
</header>
<DataTable {teams} />
