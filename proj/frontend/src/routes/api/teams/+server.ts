import type { RequestHandler } from '@sveltejs/kit';
import { sleep } from '../../../services/helper';

export const GET: RequestHandler = async ({ fetch, url }) => {
	await sleep(2000);

	return new Response();
};
