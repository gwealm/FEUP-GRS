import type { Team } from "../../../types";

const teams: Record<Team['id'], Team> = {
    "2134": {
        id: '2134',
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
    '23455634': {
        id: '23455634',
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
    '23456576': {
        id: '23456576',
        name: 'DevOps',
        services: [],
        cidr: '192.168.2.0/24'
    }
};

export { teams }