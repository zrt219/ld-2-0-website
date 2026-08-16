"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import { Check, Mail, Sparkles, Send, AlertCircle } from "lucide-react";

import { categoryInterestOptions, InterestPayload } from "@/lib/interest-schema";
import { siteCopy } from "@/content/site";

interface InterestFormProps {
  initialSelectedCategory?: string;
}

export function InterestForm({ initialSelectedCategory }: InterestFormProps) {
  const [firstName, setFirstName] = useState("");
  const [email, setEmail] = useState("");
  const [selectedInterests, setSelectedInterests] = useState<string[]>(
    initialSelectedCategory
      ? [initialSelectedCategory]
      : ["Luxury Clothing & Apparel", "Bags, Jewelry & Accessories"]
  );
  const [notes, setNotes] = useState("");
  const [honeypot, setHoneypot] = useState("");

  const [loading, setLoading] = useState(false);
  const [statusMessage, setStatusMessage] = useState<string | null>(null);
  const [statusType, setStatusType] = useState<"success" | "error" | "fallback" | null>(null);
  const [mailtoHref, setMailtoHref] = useState<string | null>(null);
  const [fieldErrors, setFieldErrors] = useState<Record<string, string[]>>({});

  const toggleInterest = (category: string) => {
    setSelectedInterests((prev) =>
      prev.includes(category)
        ? prev.filter((item) => item !== category)
        : [...prev, category]
    );
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setStatusMessage(null);
    setStatusType(null);
    setMailtoHref(null);
    setFieldErrors({});

    const payload: InterestPayload = {
      firstName,
      email,
      interests: selectedInterests,
      notes: notes || undefined,
      website: honeypot || undefined,
    };

    try {
      const response = await fetch("/api/interest", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const result = await response.json();

      if (!response.ok || !result.ok) {
        if (result.fallbackRequired) {
          // Construct prepared mailto link
          const subject = encodeURIComponent(
            `Collection Interest List: ${firstName} (${selectedInterests.join(", ")})`
          );
          const body = encodeURIComponent(
            `Please add me to The Collection interest list.\n\nFirst Name: ${firstName}\nEmail: ${email}\nInterests: ${selectedInterests.join(
              ", "
            )}\n${notes ? `Notes: ${notes}\n` : ""}`
          );
          setMailtoHref(`mailto:${siteCopy.contactEmail}?subject=${subject}&body=${body}`);
          setStatusType("fallback");
          setStatusMessage(
            "Direct server email dispatch is not configured. Click the button below to submit your request via your email client."
          );
        } else {
          setStatusType("error");
          setStatusMessage(result.message || "Please check your inputs and try again.");
          if (result.errors) {
            setFieldErrors(result.errors);
          }
        }
      } else {
        setStatusType("success");
        setStatusMessage(
          result.message ||
            "Thank you for your interest. We’ll keep you informed as The Collection gets closer to launch."
        );
        // Reset form
        setFirstName("");
        setEmail("");
        setNotes("");
      }
    } catch {
      // Fallback
      const subject = encodeURIComponent(
        `Collection Interest List: ${firstName} (${selectedInterests.join(", ")})`
      );
      const body = encodeURIComponent(
        `Please add me to The Collection interest list.\n\nFirst Name: ${firstName}\nEmail: ${email}\nInterests: ${selectedInterests.join(
          ", "
        )}\n`
      );
      setMailtoHref(`mailto:${siteCopy.contactEmail}?subject=${subject}&body=${body}`);
      setStatusType("fallback");
      setStatusMessage(
        "Network connection interrupted. Please use the direct mailto link to send your interest registration."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <section
      id="interest-list"
      className="relative scroll-mt-24 border-t border-[rgba(198,165,92,0.3)] bg-gradient-to-b from-[var(--ivory)] via-[#f5ede0] to-[#ece1d0] px-4 py-20 sm:px-6 lg:px-8"
      aria-label="Collection Interest Capture"
    >
      <div className="mx-auto max-w-3xl">
        {/* Section Header */}
        <div className="text-center">
          <div className="inline-flex items-center gap-2 rounded-full border border-[rgba(198,165,92,0.4)] bg-white/80 px-3.5 py-1.5 backdrop-blur-sm">
            <Sparkles className="h-3.5 w-3.5 text-[var(--gold-dark)]" aria-hidden="true" />
            <span className="text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
              VIP Early Access
            </span>
          </div>

          <h2 className="mt-4 font-serif text-3xl font-normal tracking-tight text-[var(--ink)] sm:text-4xl">
            Be First to Know
          </h2>

          <p className="mt-3 text-base leading-relaxed text-[#5c5246] sm:text-lg">
            Join the interest list for collection updates, product announcements, and release information.
          </p>
        </div>

        {/* Form Container */}
        <div className="mt-10 rounded-2xl border border-[rgba(198,165,92,0.35)] bg-white p-6 shadow-[0_10px_40px_rgba(42,37,32,0.06)] sm:p-10">
          {statusType === "success" ? (
            <div className="rounded-xl border border-emerald-200 bg-emerald-50/80 p-6 text-center" role="alert">
              <div className="mx-auto flex h-12 w-12 items-center justify-center rounded-full bg-emerald-100 text-emerald-700">
                <Check className="h-6 w-6" aria-hidden="true" />
              </div>
              <h3 className="mt-4 font-serif text-2xl font-medium text-emerald-950">
                You’re on the List
              </h3>
              <p className="mt-2 text-sm leading-relaxed text-emerald-800">
                {statusMessage}
              </p>
              <button
                type="button"
                onClick={() => {
                  setStatusType(null);
                  setStatusMessage(null);
                }}
                className="mt-6 inline-flex min-h-11 items-center justify-center rounded-lg border border-emerald-300 bg-white px-5 text-xs font-bold uppercase tracking-wider text-emerald-900 transition hover:bg-emerald-50"
              >
                Register Another Email
              </button>
            </div>
          ) : (
            <form onSubmit={handleSubmit} noValidate className="space-y-6">
              {/* Honeypot field for spam prevention */}
              <div className="hidden" aria-hidden="true">
                <label htmlFor="website">Website</label>
                <input
                  id="website"
                  name="website"
                  type="text"
                  tabIndex={-1}
                  autoComplete="off"
                  value={honeypot}
                  onChange={(e) => setHoneypot(e.target.value)}
                />
              </div>

              {/* Status/Error alert */}
              {statusType === "error" && statusMessage && (
                <div className="flex items-center gap-3 rounded-lg border border-red-200 bg-red-50 p-4 text-sm text-red-800" role="alert">
                  <AlertCircle className="h-5 w-5 shrink-0 text-red-600" aria-hidden="true" />
                  <p>{statusMessage}</p>
                </div>
              )}

              {/* First Name & Email Grid */}
              <div className="grid gap-6 sm:grid-cols-2">
                <div>
                  <label
                    htmlFor="interest-first-name"
                    className="block text-xs font-bold uppercase tracking-wider text-[var(--charcoal)]"
                  >
                    First Name <span className="text-[var(--gold-dark)]">*</span>
                  </label>
                  <input
                    id="interest-first-name"
                    name="firstName"
                    type="text"
                    required
                    value={firstName}
                    onChange={(e) => setFirstName(e.target.value)}
                    placeholder="Lornette"
                    aria-describedby={fieldErrors.firstName ? "firstName-error" : undefined}
                    className={`mt-2 block w-full rounded-lg border bg-[#faf7f0]/50 px-4 py-3 text-base text-[var(--ink)] placeholder:text-[#a09485] focus:bg-white focus:outline-none focus:ring-2 focus:ring-[var(--gold-dark)] ${
                      fieldErrors.firstName
                        ? "border-red-400 focus:ring-red-500"
                        : "border-[var(--line)]"
                    }`}
                  />
                  {fieldErrors.firstName && (
                    <p id="firstName-error" className="mt-1 text-xs text-red-600">
                      {fieldErrors.firstName[0]}
                    </p>
                  )}
                </div>

                <div>
                  <label
                    htmlFor="interest-email"
                    className="block text-xs font-bold uppercase tracking-wider text-[var(--charcoal)]"
                  >
                    Email Address <span className="text-[var(--gold-dark)]">*</span>
                  </label>
                  <input
                    id="interest-email"
                    name="email"
                    type="email"
                    required
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="name@example.com"
                    aria-describedby={fieldErrors.email ? "email-error" : undefined}
                    className={`mt-2 block w-full rounded-lg border bg-[#faf7f0]/50 px-4 py-3 text-base text-[var(--ink)] placeholder:text-[#a09485] focus:bg-white focus:outline-none focus:ring-2 focus:ring-[var(--gold-dark)] ${
                      fieldErrors.email
                        ? "border-red-400 focus:ring-red-500"
                        : "border-[var(--line)]"
                    }`}
                  />
                  {fieldErrors.email && (
                    <p id="email-error" className="mt-1 text-xs text-red-600">
                      {fieldErrors.email[0]}
                    </p>
                  )}
                </div>
              </div>

              {/* Product Interests Multi-Select */}
              <div>
                <label className="block text-xs font-bold uppercase tracking-wider text-[var(--charcoal)]">
                  Product Categories of Interest <span className="text-[var(--gold-dark)]">*</span>
                </label>
                <p className="mt-1 text-xs text-[#7d7164]">
                  Select all categories you wish to receive announcements and release access for.
                </p>

                <div className="mt-3 grid grid-cols-1 gap-2.5 sm:grid-cols-2 lg:grid-cols-3">
                  {categoryInterestOptions.map((option) => {
                    const isChecked = selectedInterests.includes(option);
                    return (
                      <motion.button
                        key={option}
                        type="button"
                        onClick={() => toggleInterest(option)}
                        aria-pressed={isChecked}
                        whileHover={{ scale: 1.02 }}
                        whileTap={{ scale: 0.98 }}
                        className={`flex min-h-12 items-center justify-between rounded-xl border px-4 py-2.5 text-left text-xs font-semibold transition-all focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)] ${
                          isChecked
                            ? "border-[var(--gold-dark)] bg-[var(--ink)] text-[var(--ivory)] shadow-sm"
                            : "border-[rgba(198,165,92,0.3)] bg-[#faf7f0] text-[var(--charcoal)] hover:border-[var(--gold-dark)] hover:bg-white"
                        }`}
                      >
                        <span className="truncate pr-2">{option}</span>
                        {isChecked ? (
                          <motion.span
                            initial={{ scale: 0 }}
                            animate={{ scale: 1 }}
                            transition={{ type: "spring", stiffness: 500, damping: 25 }}
                            className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-[var(--gold-dark)] text-white"
                          >
                            <Check className="h-3 w-3" aria-hidden="true" />
                          </motion.span>
                        ) : (
                          <span className="h-5 w-5 shrink-0 rounded-full border border-[rgba(198,165,92,0.4)] bg-white/50" />
                        )}
                      </motion.button>
                    );
                  })}
                </div>
                {fieldErrors.interests && (
                  <p className="mt-1 text-xs text-red-600">{fieldErrors.interests[0]}</p>
                )}
              </div>

              {/* Submit Button */}
              <div className="pt-2">
                <motion.button
                  type="submit"
                  disabled={loading}
                  whileHover={loading ? {} : { scale: 1.02 }}
                  whileTap={loading ? {} : { scale: 0.98 }}
                  className={`inline-flex min-h-12 w-full items-center justify-center gap-2 rounded-xl bg-[var(--ink)] px-8 text-sm font-bold uppercase tracking-wider text-[var(--ivory)] shadow-md transition-all hover:bg-[var(--gold-dark)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)] ${
                    loading ? "cursor-wait opacity-70" : ""
                  }`}
                >
                  {loading ? (
                    <span>Submitting Registration...</span>
                  ) : (
                    <>
                      <Send className="h-4 w-4" aria-hidden="true" />
                      <span>Join the Interest List</span>
                    </>
                  )}
                </motion.button>
              </div>

              {/* Fallback mailto display */}
              {statusType === "fallback" && (
                <div className="rounded-lg border border-[rgba(198,165,92,0.4)] bg-[#faf7f0] p-4 text-center">
                  <p className="text-xs text-[#5c5246]">{statusMessage}</p>
                  {mailtoHref && (
                    <a
                      href={mailtoHref}
                      className="mt-3 inline-flex min-h-11 items-center justify-center gap-2 rounded-lg bg-[var(--gold-dark)] px-5 text-xs font-bold uppercase tracking-wider text-white shadow transition hover:bg-[var(--ink)]"
                    >
                      <Mail className="h-4 w-4" aria-hidden="true" />
                      Open Prepared Interest Email
                    </a>
                  )}
                </div>
              )}

              <p className="text-center text-xs text-[#8b7d6c]">
                We respect your privacy. No spam. You can unsubscribe at any time.
              </p>
            </form>
          )}
        </div>
      </div>
    </section>
  );
}
