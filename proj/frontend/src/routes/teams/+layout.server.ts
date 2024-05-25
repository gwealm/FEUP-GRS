import type { Team } from '../../types';
import type { LayoutServerLoad } from './$types';

export const load: LayoutServerLoad = async () => {
	const teams: Team[] = [
		{
			id: 2134,
			name: 'HR',
			description: 'Human Resources',
			services: [
				{
					id: 234,
					name: 'Proxy',
					ipAddress: '192.168.0.1'
				}
			],
			cidr: '192.168.0.0/24'
		},
		{
			id: 23455634,
			name: 'UI/UX',
			services: [
				{
					id: 45674,
					name: 'Proxy',
					ipAddress: '192.168.1.1'
				},
				{
					id: 23907,
					name: 'Git',
					ipAddress: '192.168.1.2'
				}
			],
			cidr: '192.168.1.0/24'
		},
		{
			id: 23456576,
			name: 'DevOps',
			services: [],
			cidr: '192.168.2.0/24'
		}
	];

	return { teams };
};
