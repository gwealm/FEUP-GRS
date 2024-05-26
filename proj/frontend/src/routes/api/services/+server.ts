import type { RequestHandler } from '@sveltejs/kit';
import type { ServiceBase } from '../../../types';

export const GET: RequestHandler = async () => {
	const services: ServiceBase[] = [
		{
			id: 1,
			name: 'GIT',
			description: 'Custom GIT remote repository'
		},
		{
			id: 2,
			name: 'Squid Proxy',
			description: 'Proxy server'
		},
		{
			id: 3,
			name: 'DNS',
			description: 'Custom sub-DNS server'
		}
	];

	const body = JSON.stringify(services);

	return new Response(body);
};
