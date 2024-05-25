import { fail } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ parent, params }) => {
	const { teams } = await parent();
	const { team: teamId } = params;

	for (const team of teams) {
		if (team.id === Number(teamId)) {
			return { team };
		}
	}

	return fail(403, { message: 'Unknown team id' });
};
