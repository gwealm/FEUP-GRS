import type { Actions } from "@sveltejs/kit";

export const actions: Actions = {
    login: async ({ request, cookies }) => {
        const formData = await request.formData();


    }
}