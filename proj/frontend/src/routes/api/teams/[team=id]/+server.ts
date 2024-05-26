import type { RequestHandler } from '@sveltejs/kit';
import { teams } from '../data';

export const DELETE: RequestHandler = async ({ params: { team } }) => {
	console.log(`Deleting team ${team}`);

	delete teams[team!];

	return new Response();
};

export const GET: RequestHandler = async ({ params: { team: teamId } }) => {
	const team = teams[teamId!];

	const body = JSON.stringify(team);

	return new Response(body);
};
