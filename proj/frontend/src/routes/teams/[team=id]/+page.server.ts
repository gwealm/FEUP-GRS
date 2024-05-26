import type { PageServerLoad } from './$types';
import type { Team } from '../../../types';
// import { fail } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ fetch, params: { team: teamId } }) => {
	const response = await fetch(`/api/teams/${teamId}`);

	// TODO: add error history

	const team: Team = await response.json();

	return { team };
};
