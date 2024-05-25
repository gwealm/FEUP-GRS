import { z } from 'zod';

const LoginSchema = z.object({
	username: z.string().min(3),
	password: z.string(),
	rememberMe: z.boolean().optional().default(false)
});

type Login = typeof LoginSchema;

export { LoginSchema, type Login };
