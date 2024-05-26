import type { Team } from '../../types';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ fetch }) => {
	const response = await fetch("/api/teams");

	const teams: Team[] = await response.json();

	return { teams };
};
