<script lang="ts">
	import * as Form from '$lib/components/ui/form';
	import { Input } from '$lib/components/ui/input';
	import { Checkbox } from '$lib/components/ui/checkbox';
	import { LoginSchema } from './schemas';
	import { superForm } from 'sveltekit-superforms';
	import { zodClient } from 'sveltekit-superforms/adapters';
	import type { PageData } from './$types.js';

	export let data: PageData;

	const form = superForm(data.form, {
		validators: zodClient(LoginSchema),
		taintedMessage: true
	});

	const { form: formData, enhance } = form;
</script>

<div class="flex h-full w-full items-center justify-center">
	<form method="POST" use:enhance action="?/login" class="w-[20em]">
		<Form.Field {form} name="username">
			<Form.Control let:attrs>
				<Form.Label>Username</Form.Label>
				<Input {...attrs} bind:value={$formData.username} required />
			</Form.Control>
			<Form.FieldErrors />
		</Form.Field>
		<Form.Field {form} name="password">
			<Form.Control let:attrs>
				<Form.Label>Password</Form.Label>
				<Input type="password" {...attrs} bind:value={$formData.password} required />
			</Form.Control>
			<Form.FieldErrors />
		</Form.Field>
		<Form.Field {form} name="rememberMe">
			<Form.Control let:attrs>
				<Form.Label>Remember me</Form.Label>
				<Checkbox {...attrs} bind:checked={$formData.rememberMe} />
				<input name={attrs.name} value={$formData.rememberMe} hidden />
			</Form.Control>
			<Form.FieldErrors />
		</Form.Field>
		<Form.Button>Submit</Form.Button>
	</form>
</div>
