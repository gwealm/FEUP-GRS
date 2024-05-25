import { default as z } from 'zod';

const CIDRRegex = /^([0-9]{1,3}\.){3}[0-9]{1,3}($|\/\d{ 1,2})$/g;

const ServiceSchema = z.object({
	id: z.number().min(0),
	name: z.string(),
	description: z.string().optional(),

	deployedAt: z.date().optional(),
	ipAddress: z.string().ip({
		version: 'v4'
	})
});

const TeamSchema = z.object({
	id: z.string().min(0),
	name: z.string().min(3).max(20),
	description: z.string().optional(),

	cidr: z.string().regex(CIDRRegex, { message: 'Invalid CIDR block representation' }),

	services: ServiceSchema.array(),

	createdAt: z.date().optional(),
	updatedAt: z.date().optional()
});

type Team = z.infer<typeof TeamSchema>;
type Service = z.infer<typeof ServiceSchema>;

export { TeamSchema, type Team, ServiceSchema, type Service };
