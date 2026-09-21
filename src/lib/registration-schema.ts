import { z } from "zod";

export const registrationSchema = z.object({
  firstName: z.string().min(1, "First name is required"),
  lastName: z.string().min(1, "Last name is required"),
  email: z.string().email("Invalid email address"),
  phone: z.string().min(1, "Phone number is required"),
  cityState: z.string().min(1, "City & State/Province is required"),
  hearAbout: z.string().min(1, "Please tell us how you heard about this"),
  cohortInterest: z.enum(["next", "future", "unsure"], {
    message: "Please select your cohort interest",
  }),
  handicapIndex: z.string().min(1, "Handicap Index is required"),
  competitiveRole: z.string().min(1, "Please select your primary competitive role"),
  homeClub: z.string().min(1, "Home club or facility is required"),
  notes: z.string().optional().default(""),
  clubCode: z.string().optional().default(""),
  website: z.string().optional().default(""),
});

export type RegistrationFormValues = z.infer<typeof registrationSchema>;
