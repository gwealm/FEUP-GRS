import type { RequestHandler } from '@sveltejs/kit';
import { API_BASE_URL } from '$env/static/private';

export const DELETE: RequestHandler = async ({ fetch, params: { team: teamId } }) => {
	const endpoint = `${API_BASE_URL}/team/${teamId}`

	return await fetch(endpoint, {
		method: 'DELETE'
	});
};

export const GET: RequestHandler = async ({ fetch, params: { team: teamId } }) => {
	const endpoint = `${API_BASE_URL}/team/${teamId}`

	return await fetch(endpoint);
};
