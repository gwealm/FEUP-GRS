import { z } from 'zod';
import { ServiceBaseSchema } from '../../types';

const CreateTeamSchema = z.object({
	name: z.string().min(3),
	description: z.string().min(3).optional(),
	services: z.array(ServiceBaseSchema.shape.id).min(1)
});

export { CreateTeamSchema };
