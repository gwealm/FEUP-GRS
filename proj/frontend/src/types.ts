import { default as z } from "zod";

const ServiceSchema = z.object({
    id: z.number().min(0),
    name: z.string(),
});

const TeamSchema = z.object({
    id: z.number().min(0),
    name: z.string().min(3).max(20),
    description: z.string().optional(),
    services: ServiceSchema.array(),
});

type Team = z.infer<typeof TeamSchema>;
type Service = z.infer<typeof ServiceSchema>;

export { TeamSchema, type Team, ServiceSchema, type Service };