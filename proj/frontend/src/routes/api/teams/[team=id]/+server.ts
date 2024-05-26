import type { RequestHandler } from '@sveltejs/kit';
import { sleep } from '../../../../services/helper';
import { teams } from '../data';

export const DELETE: RequestHandler = async ({ params: { team } }) => {
	console.log(`Deleting team ${team}`);

	await sleep(2000);
	delete teams[team!];

	return new Response();
};

export const GET: RequestHandler = async ({ params: { team: teamId } }) => {
	await sleep(2000);

	const team = teams[teamId!];

	const body = JSON.stringify(team);

	return new Response(body);
};
