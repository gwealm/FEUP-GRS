import { goto } from '$app/navigation';
import type { PageLoad } from './$types';

export const ssr = false;

export const load: PageLoad = async () => {
	await goto('/teams');
};
