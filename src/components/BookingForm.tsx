"use client";

import { Send } from "lucide-react";
import { useMemo, useState } from "react";

import { siteCopy } from "@/content/site";
import { inquirySchema, topicOptions, type InquiryPayload } from "@/lib/inquiry-schema";

type Errors = Partial<Record<keyof InquiryPayload, string>>;

const eventTypes = ["Keynote", "Workshop", "Panel", "Retreat", "Virtual/Hybrid", "Coaching"];
const locationTypes = ["In person", "Virtual", "Hybrid", "Not sure yet"];
const budgetRanges = ["Custom proposal", "Under $2,500", "$2,500-$5,000", "$5,000-$10,000", "$10,000+"];

function getFormPayload(form: HTMLFormElement) {
  const data = new FormData(form);
  return {
    fullName: String(data.get("fullName") ?? ""),
    email: String(data.get("email") ?? ""),
    phone: String(data.get("phone") ?? ""),
    organization: String(data.get("organization") ?? ""),
    role: String(data.get("role") ?? ""),
    eventType: String(data.get("eventType") ?? ""),
    preferredDate: String(data.get("preferredDate") ?? ""),
    alternateDate: String(data.get("alternateDate") ?? ""),
    locationType: String(data.get("locationType") ?? ""),
    cityVenue: String(data.get("cityVenue") ?? ""),
    expectedAudienceSize: String(data.get("expectedAudienceSize") ?? ""),
    budgetRange: String(data.get("budgetRange") ?? ""),
    topicsOfInterest: data.getAll("topicsOfInterest").map(String),
    eventGoals: String(data.get("eventGoals") ?? ""),
    consent: data.get("consent") === "on",
    website: String(data.get("website") ?? ""),
  };
}

function toMailto(payload: InquiryPayload) {
  const body = [
    `Full name: ${payload.fullName}`,
    `Email: ${payload.email}`,
    `Phone: ${payload.phone || "Not provided"}`,
    `Organization: ${payload.organization}`,
    `Title / role: ${payload.role || "Not provided"}`,
    `Event type: ${payload.eventType}`,
    `Preferred date: ${payload.preferredDate || "Not provided"}`,
    `Alternate date: ${payload.alternateDate || "Not provided"}`,
    `Location type: ${payload.locationType}`,
    `City / venue: ${payload.cityVenue || "Not provided"}`,
    `Audience size: ${payload.expectedAudienceSize}`,
    `Budget range: ${payload.budgetRange || "Not provided"}`,
    `Topics: ${payload.topicsOfInterest.join(", ")}`,
    "",
    "Event goals:",
    payload.eventGoals,
  ].join("\n");

  return `mailto:${siteCopy.contactEmail}?subject=${encodeURIComponent(
    `Booking inquiry for ${siteCopy.brandName}`,
  )}&body=${encodeURIComponent(body)}`;
}

export function BookingForm() {
  const [errors, setErrors] = useState<Errors>({});
  const [status, setStatus] = useState<"idle" | "loading" | "success" | "fallback" | "error">("idle");
  const [message, setMessage] = useState("");
  const [mailtoHref, setMailtoHref] = useState("");

  const fieldClass = useMemo(
    () =>
      "mt-2 min-h-12 w-full border border-[var(--line)] bg-white px-4 text-base text-[var(--ink)] transition focus:border-[var(--champagne)]",
    [],
  );

  async function onSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (status === "loading") return;

    const payload = getFormPayload(event.currentTarget);
    const parsed = inquirySchema.safeParse(payload);

    if (!parsed.success) {
      const flattened = parsed.error.flatten().fieldErrors;
      setErrors(
        Object.fromEntries(
          Object.entries(flattened).map(([key, value]) => [key, value?.[0] ?? "Invalid value"]),
        ) as Errors,
      );
      setStatus("error");
      setMessage("Please correct the highlighted fields.");
      return;
    }

    setErrors({});
    setStatus("loading");
    setMessage("");
    setMailtoHref("");

    try {
      const response = await fetch("/api/inquiry", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(parsed.data),
      });
      const result = (await response.json()) as {
        ok: boolean;
        fallbackRequired?: boolean;
        message?: string;
      };

      if (result.fallbackRequired) {
        setMailtoHref(toMailto(parsed.data));
        setStatus("fallback");
        setMessage(
          "Your inquiry has been prepared. Please send it through your email client.",
        );
        return;
      }

      if (!response.ok || !result.ok) {
        if (response.status >= 500) {
          setMailtoHref(toMailto(parsed.data));
          setStatus("fallback");
          setMessage(
            result.message ??
              "Email delivery is temporarily unavailable. Please use the prepared email instead.",
          );
          return;
        }

        setStatus("error");
        setMessage(result.message ?? "The inquiry could not be sent. Please try again.");
        return;
      }

      setStatus("success");
      setMessage("Thank you. Your inquiry has been sent.");
      event.currentTarget.reset();
    } catch {
      setMailtoHref(toMailto(parsed.data));
      setStatus("fallback");
      setMessage(
        "Your inquiry has been prepared. Please send it through your email client.",
      );
    }
  }

  function errorFor(field: keyof InquiryPayload) {
    return errors[field] ? (
      <p className="mt-2 text-sm text-[#8f231f]">{errors[field]}</p>
    ) : null;
  }

  return (
    <form onSubmit={onSubmit} className="grid gap-5" noValidate>
      <div className="grid gap-5 md:grid-cols-2">
        <div className="sr-only" aria-hidden="true">
          <label htmlFor="website">Website</label>
          <input id="website" name="website" tabIndex={-1} autoComplete="off" />
        </div>
        <div>
          <label htmlFor="fullName" className="text-sm font-semibold">
            Full name
          </label>
          <input id="fullName" name="fullName" autoComplete="name" className={fieldClass} />
          {errorFor("fullName")}
        </div>
        <div>
          <label htmlFor="email" className="text-sm font-semibold">
            Email
          </label>
          <input id="email" name="email" type="email" autoComplete="email" className={fieldClass} />
          {errorFor("email")}
        </div>
      </div>

      <div className="grid gap-5 md:grid-cols-2">
        <div>
          <label htmlFor="phone" className="text-sm font-semibold">
            Phone
          </label>
          <input id="phone" name="phone" type="tel" autoComplete="tel" className={fieldClass} />
        </div>
        <div>
          <label htmlFor="organization" className="text-sm font-semibold">
            Organization
          </label>
          <input id="organization" name="organization" autoComplete="organization" className={fieldClass} />
          {errorFor("organization")}
        </div>
      </div>

      <div className="grid gap-5 md:grid-cols-2">
        <div>
          <label htmlFor="role" className="text-sm font-semibold">
            Title / role
          </label>
          <input id="role" name="role" className={fieldClass} />
        </div>
        <div>
          <label htmlFor="eventType" className="text-sm font-semibold">
            Event type
          </label>
          <select id="eventType" name="eventType" defaultValue="" className={fieldClass}>
            <option value="" disabled>
              Select one
            </option>
            {eventTypes.map((item) => (
              <option key={item}>{item}</option>
            ))}
          </select>
          {errorFor("eventType")}
        </div>
      </div>

      <div className="grid gap-5 md:grid-cols-2">
        <div>
          <label htmlFor="preferredDate" className="text-sm font-semibold">
            Event date
          </label>
          <input id="preferredDate" name="preferredDate" type="date" className={fieldClass} />
        </div>
        <div>
          <label htmlFor="alternateDate" className="text-sm font-semibold">
            Alternate date
          </label>
          <input id="alternateDate" name="alternateDate" type="date" className={fieldClass} />
        </div>
      </div>

      <div className="grid gap-5 md:grid-cols-2">
        <div>
          <label htmlFor="locationType" className="text-sm font-semibold">
            Event location
          </label>
          <select id="locationType" name="locationType" defaultValue="" className={fieldClass}>
            <option value="" disabled>
              Select one
            </option>
            {locationTypes.map((item) => (
              <option key={item}>{item}</option>
            ))}
          </select>
          {errorFor("locationType")}
        </div>
        <div>
          <label htmlFor="cityVenue" className="text-sm font-semibold">
            City / venue
          </label>
          <input id="cityVenue" name="cityVenue" className={fieldClass} />
        </div>
      </div>

      <div className="grid gap-5 md:grid-cols-2">
        <div>
          <label htmlFor="expectedAudienceSize" className="text-sm font-semibold">
            Audience size
          </label>
          <input id="expectedAudienceSize" name="expectedAudienceSize" inputMode="numeric" className={fieldClass} />
          {errorFor("expectedAudienceSize")}
        </div>
        <div>
          <label htmlFor="budgetRange" className="text-sm font-semibold">
            Budget range
          </label>
          <select id="budgetRange" name="budgetRange" defaultValue="" className={fieldClass}>
            <option value="">Select if known</option>
            {budgetRanges.map((item) => (
              <option key={item}>{item}</option>
            ))}
          </select>
        </div>
      </div>

      <fieldset>
        <legend className="text-sm font-semibold">Topic interest</legend>
        <div className="mt-3 grid gap-3 sm:grid-cols-2">
          {topicOptions.map((topic) => (
            <label
              key={topic}
              className="flex min-h-12 items-center gap-3 border border-[var(--line)] bg-white px-4 text-sm"
            >
              <input type="checkbox" name="topicsOfInterest" value={topic} className="h-4 w-4" />
              {topic}
            </label>
          ))}
        </div>
        {errorFor("topicsOfInterest")}
      </fieldset>

      <div>
        <label htmlFor="eventGoals" className="text-sm font-semibold">
          Event goals
        </label>
        <textarea id="eventGoals" name="eventGoals" rows={6} className={`${fieldClass} py-3`} />
        {errorFor("eventGoals")}
      </div>

      <label className="flex items-start gap-3 text-sm leading-6">
        <input type="checkbox" name="consent" className="mt-1 h-4 w-4" />
        I consent to be contacted about this inquiry.
      </label>
      {errorFor("consent")}

      {message ? (
        <div
          className={`border px-4 py-3 text-sm ${
            status === "error"
              ? "border-[#e1b0aa] bg-[#fff7f4] text-[#7c211b]"
              : "border-[rgba(198,165,92,0.5)] bg-[#fffaf0] text-[#5d4414]"
          }`}
          aria-live="polite"
        >
          <p>{message}</p>
          {mailtoHref ? (
            <a className="mt-3 inline-flex font-bold underline" href={mailtoHref}>
              Open prepared email
            </a>
          ) : null}
        </div>
      ) : null}

      <button
        type="submit"
        disabled={status === "loading"}
        className="inline-flex min-h-12 w-full items-center justify-center gap-2 bg-[var(--ink)] px-5 py-3 text-sm font-bold uppercase text-[var(--ivory)] transition hover:bg-[var(--charcoal)] disabled:cursor-not-allowed disabled:opacity-60 sm:w-fit"
      >
        <Send size={17} aria-hidden="true" />
        {status === "loading" ? "Preparing inquiry" : "Inquire About Availability"}
      </button>
    </form>
  );
}
