import type { RequestHandler } from '@sveltejs/kit';
import { teams } from './data';

export const GET: RequestHandler = async () => {
	const body = JSON.stringify(Object.values(teams));

	return new Response(body);
};
