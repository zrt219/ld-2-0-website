import { z } from "zod";

export const topicOptions = [
  "Keynotes & Speaking",
  "Mentorship & Youth Development",
  "Purpose & Resilience Coaching",
] as const;

export const inquirySchema = z.object({
  fullName: z.string().trim().min(2, "Please enter your full name."),
  email: z.string().trim().email("Please enter a valid email address."),
  phone: z.string().trim().optional(),
  organization: z.string().trim().min(2, "Please enter your organization."),
  role: z.string().trim().optional(),
  eventType: z.string().trim().min(2, "Please choose an event type."),
  preferredDate: z.string().trim().optional(),
  alternateDate: z.string().trim().optional(),
  locationType: z.string().trim().min(2, "Please choose a location type."),
  cityVenue: z.string().trim().optional(),
  expectedAudienceSize: z
    .string()
    .trim()
    .min(1, "Please enter the expected audience size."),
  budgetRange: z.string().trim().optional(),
  topicsOfInterest: z
    .array(z.string())
    .min(1, "Please select at least one topic."),
  eventGoals: z
    .string()
    .trim()
    .min(20, "Please share a few details about the event goals."),
  consent: z.literal(true, {
    error: "Please confirm consent to be contacted about this inquiry.",
  }),
  website: z.string().trim().max(120).optional(),
});

export type InquiryPayload = z.infer<typeof inquirySchema>;
