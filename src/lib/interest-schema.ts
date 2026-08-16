import { z } from "zod";

export const categoryInterestOptions = [
  "Hair Cleansing & Moisture",
  "Scalp & Hair Growth Oils",
  "Luxury Wigs & Clip-In Extensions",
  "Serums & Facial Treatments",
  "Body & Barrier Creams",
  "Primers & Complexion Glow",
] as const;

export const interestSchema = z.object({
  firstName: z
    .string()
    .trim()
    .min(1, "Please enter your first name.")
    .max(80, "First name is too long."),
  email: z
    .string()
    .trim()
    .email("Please enter a valid email address.")
    .max(120, "Email address is too long."),
  interests: z
    .array(z.string())
    .min(1, "Please select at least one product category of interest."),
  notes: z.string().trim().max(500).optional(),
  website: z.string().trim().max(120).optional(), // Honeypot field
});

export type InterestPayload = z.infer<typeof interestSchema>;
