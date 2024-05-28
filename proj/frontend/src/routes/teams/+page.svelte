<script lang="ts">
	import * as AlertDialog from '$lib/components/ui/alert-dialog';
	import { Button } from '$lib/components/ui/button/';
	import * as Form from '$lib/components/ui/form';
	import { Input } from '$lib/components/ui/input';
	import * as Select from '$lib/components/ui/select';
	import { Textarea } from '$lib/components/ui/textarea';
	import { superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import Icon from '../(components)/Icon.svelte';
	import type { PageData } from './$types';
	import DataTable from './(components)/Table.svelte';
	import { CreateTeamSchema } from './schemas';

	export let data: PageData;

	let openDialog = false;

	const form = superForm(data.form, {
		validators: zodClient(CreateTeamSchema),
		dataType: 'json'
	});

	const { form: formData, enhance } = form;

	$: teams = data.teams;
	$: services = data.services;

	$: flattenedServices = Object.values(services).flat();

	$: selectedServices = $formData.services.map((s) => ({
		value: s,
		label: flattenedServices.find((service) => service.id === s)!.name
	}));
</script>

<header class="mb-5 flex w-full justify-between">
	<h1 class="text-xl">Your organization's teams:</h1>
	<AlertDialog.Root open={openDialog} closeOnEscape closeOnOutsideClick>
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
			<form
				method="POST"
				use:enhance={{
					onSubmit: () => {
						openDialog = false;
					}
				}}
				action="/teams?/create"
			>
				<Form.Field {form} name="name">
					<Form.Control let:attrs>
						<Form.Label>Name</Form.Label>
						<Input {...attrs} bind:value={$formData.name} required />
					</Form.Control>
					<Form.FieldErrors />
				</Form.Field>
				<fieldset class="flex w-full gap-3">
					<Form.Field {form} name="baseAddress" class="flex-1">
						<Form.Control let:attrs>
							<Form.Label>Base Address</Form.Label>
							<Input
								{...attrs}
								bind:value={$formData.baseAddress}
								required
								placeholder={"Your address must end with '.0'"}
							/>
						</Form.Control>
						<Form.FieldErrors />
					</Form.Field>
					<Form.Field {form} name="maskLength">
						<Form.Control let:attrs>
							<Form.Label>Mask Length</Form.Label>
							<Input
								type="number"
								max={32}
								min={1}
								{...attrs}
								bind:value={$formData.maskLength}
								required
							/>
						</Form.Control>
						<Form.FieldErrors />
					</Form.Field>
				</fieldset>
				<Form.Field {form} name="description">
					<Form.Control let:attrs>
						<Form.Label>Description</Form.Label>
						<Textarea {...attrs} bind:value={$formData.description} />
					</Form.Control>
					<Form.FieldErrors />
				</Form.Field>
				<Form.Field {form} name="services">
					<Form.Control let:attrs>
						<Form.Label>Select additional services to deploy</Form.Label>
						<Select.Root
							multiple
							selected={selectedServices}
							onSelectedChange={(serviceSelection) => {
								if (serviceSelection) {
									$formData.services = serviceSelection.map(
										(selectedService) => selectedService.value
									);
								} else {
									$formData.services = [];
								}
							}}
						>
							{#each $formData.services as service}
								<input name={attrs.name} hidden value={service} />
							{/each}
							<Select.Trigger {...attrs}>
								<Select.Value placeholder="Select services" />
							</Select.Trigger>
							<Select.Content>
								{#each Object.entries(services) as [category, serviceGroup]}
									<Select.Group>
										<Select.Label>
											{category}
										</Select.Label>
										{#each serviceGroup as service}
											<Select.Item value={service.id} label={service.name} />
										{/each}
										<Select.Separator />
									</Select.Group>
								{/each}
							</Select.Content>
						</Select.Root>
					</Form.Control>
					<Form.FieldErrors />
				</Form.Field>

				<!-- FIXME: this looks weird -->
				<AlertDialog.Footer>
					<AlertDialog.Cancel>Cancel</AlertDialog.Cancel>
					<AlertDialog.Action asChild><Form.Button>Create</Form.Button></AlertDialog.Action>
				</AlertDialog.Footer>
			</form>
		</AlertDialog.Content>
	</AlertDialog.Root>
</header>
{#if teams.length}
	<DataTable {teams} />
{:else}
	<div class="flex h-full items-center justify-center">
		<div class="flex flex-col gap-5">
			<p>You don't have any teams yet.</p>
			<Button
				on:click={() => {
					openDialog = true;
				}}>Create one</Button
			>
		</div>
	</div>
{/if}
