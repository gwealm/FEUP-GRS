import type { Team } from "../../types";
import type { LayoutServerLoad } from "./$types";

export const load: LayoutServerLoad = async () => {
    const teams: Team[] = [
        {
            id: 2134,
            name: 'HR',
            description: "Human Resources",
            services: [
                {
                    id: 234,
                    name: 'Proxy'
                }
            ]
        },
        {
            id: 23455634,
            name: 'UI/UX',
            services: [
                {
                    id: 45674,
                    name: 'Proxy'
                },
                {
                    id: 23907,
                    name: 'Git'
                }
            ]
        },
        {
            id: 23456576,
            name: 'DevOps',
            services: []
        }
    ];

    return { teams };
}