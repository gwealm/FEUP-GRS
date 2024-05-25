import { z } from 'zod';

const CreateTeamSchema = z.object({
	name: z.string().min(3),
	description: z.string().min(3).optional()
});

export { CreateTeamSchema };
