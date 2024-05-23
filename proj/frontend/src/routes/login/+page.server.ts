import type { Actions } from "@sveltejs/kit";
import { LoginSchema } from "./schemas";
import type { PageServerLoad } from "./$types";
import { fail, superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';

export const load: PageServerLoad = async () => {
    const form = await superValidate(zod(LoginSchema));

    return { form };
}

export const actions: Actions = {
    login: async (event) => {

        const { cookies } = event;

        const form = await superValidate(event, zod(LoginSchema));

        if (!form.valid) {
            return fail(400, {
                form,
                message: "Invalid credentials."
            });
        }

        // TODO: validate creds;

        // TODO: set cookie;

        return {
            form,
        };
    }
}