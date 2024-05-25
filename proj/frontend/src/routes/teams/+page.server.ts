import type { Actions } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { CreateTeamSchema } from './schemas';
import { fail, superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';

export const load: PageServerLoad = async () => {
	const form = await superValidate(zod(CreateTeamSchema));

	return { form };
};

export const actions: Actions = {
	create: async (event) => {
		const form = await superValidate(event, zod(CreateTeamSchema));

		if (!form.valid) {
			return fail(400, {
				form,
				message: 'Invalid credentials.'
			});
		}

		console.log("aaa");


		// TODO: validate creds;

		// TODO: set cookie;

		return {
			form
		};
	}
};
