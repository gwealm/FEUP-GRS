import type { RequestHandler } from '@sveltejs/kit';
import { teams } from '../data';
import { API_BASE_URL } from '$env/static/private';

export const DELETE: RequestHandler = async ({ params: { team } }) => {
	console.log(`Deleting team ${team}`);

	delete teams[team!];

	return new Response();
};

export const GET: RequestHandler = async ({ fetch, params: { team: teamId } }) => {
	const endpoint = `${API_BASE_URL}/team/${teamId}`

	return await fetch(endpoint);
};
