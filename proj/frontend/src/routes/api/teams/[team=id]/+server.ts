import type { RequestHandler } from '@sveltejs/kit';
import { sleep } from '../../../../services/helper';

export const DELETE: RequestHandler = async ({ fetch, url, params: { team } }) => {
	console.log(`Deleting team ${team}`);

	await sleep(2000);

	return new Response();
};
