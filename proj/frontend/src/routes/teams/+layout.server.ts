import type { ServiceBase, Team } from '../../types';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async ({ fetch }) => {
	const [teams, services, defaultServices] = await Promise.all([
		fetch('/api/teams').then((response) => response.json()),
		fetch('/api/services').then((response) => response.json()),
		fetch('/api/services/default').then((response) => response.json())
	]);

	return { teams, services, defaultServices } as { teams: Team[]; services: Record<ServiceBase['tag'], ServiceBase[]>, defaultServices: { description: string, label: string }[] };
};
