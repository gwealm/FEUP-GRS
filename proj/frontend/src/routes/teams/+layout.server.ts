import type { ServiceBase, Team } from '../../types';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ fetch }) => {
	const [teams, services] = await Promise.all([
		fetch('/api/teams').then((response) => response.json()),
		fetch('/api/services').then((response) => response.json())
	]);

	return { teams, services } as { teams: Team[]; services: ServiceBase[] };
};
