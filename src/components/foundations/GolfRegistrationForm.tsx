"use client";

import Link from "next/link";
import { useState } from "react";
import { CheckCircle2, Loader2, Lock, Mail } from "lucide-react";

interface FormState {
  firstName: string;
  lastName: string;
  email: string;
  phone: string;
  cityState: string;
  homeClub: string;
  handicapIndex: string;
  competitiveRole: string;
  hearAbout: string;
  cohortInterest: "next" | "future" | "unsure";
  notes: string;
  website: string; // honeypot
}

const initialFormState: FormState = {
  firstName: "",
  lastName: "",
  email: "",
  phone: "",
  cityState: "",
  homeClub: "",
  handicapIndex: "",
  competitiveRole: "",
  hearAbout: "",
  cohortInterest: "next",
  notes: "",
  website: "",
};

export function GolfRegistrationForm({ id }: { id?: string }) {
  const [formData, setFormData] = useState<FormState>(initialFormState);
  const [submitting, setSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [mailtoUrl, setMailtoUrl] = useState<string | null>(null);
  const [recipient, setRecipient] = useState<string>("lornettedayespeaking@umattr.ca");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setErrorMessage(null);
    setSubmitting(true);

    try {
      const res = await fetch("/api/registration", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      const data = await res.json();

      if (!res.ok && !data.ok) {
        throw new Error(data.message || "Failed to submit registration.");
      }

      if (data.mailtoUrl) {
        setMailtoUrl(data.mailtoUrl);
      }
      if (data.recipient) {
        setRecipient(data.recipient);
      }

      setSubmitted(true);
    } catch (err: unknown) {
      const msg = err instanceof Error ? err.message : "Something went wrong. Please try again.";
      setErrorMessage(msg);
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div id={id} className="w-full max-w-xl mx-auto rounded-2xl bg-white border border-[#e5ded4] shadow-xl overflow-hidden">
      {/* Top Tabs */}
      <div className="grid grid-cols-1 sm:grid-cols-2 border-b border-[#e5ded4]">
        <div className="bg-[var(--champagne)] text-black font-semibold text-xs tracking-wider uppercase px-4 py-3.5 flex items-center justify-center gap-1 text-center select-none shadow-sm">
          <span>Register for 10-Week Program</span>
          <span className="text-xs">↗</span>
        </div>
        <Link
          href="/foundations/golf/club-partnership"
          className="bg-[#f8f5f0] hover:bg-[#efe8dd] text-[#6b6255] hover:text-black font-medium text-xs tracking-wider uppercase px-4 py-3.5 flex items-center justify-center gap-1 text-center transition-colors border-t sm:border-t-0 border-[#e5ded4]"
        >
          <span>Inquire for Your Club / Organization</span>
          <span className="text-xs">→</span>
        </Link>
      </div>

      <div className="p-6 sm:p-8">
        {submitted ? (
          <div role="status" aria-live="polite" className="py-8 text-center space-y-5">
            <div role="status" aria-live="polite" className="w-16 h-16 rounded-full bg-[rgba(198,165,92,0.15)] text-[var(--champagne)] flex items-center justify-center mx-auto border border-[var(--champagne)]">
              <CheckCircle2 className="w-8 h-8" />
            </div>
            <div className="space-y-2">
              <h3 className="font-serif text-2xl text-black">Registration Received</h3>
              <p className="text-sm text-neutral-600 max-w-md mx-auto">
                Thank you, <span className="font-semibold text-black">{formData.firstName}</span>. We have received your application for the 10-Week Guided Athlete Development Program.
              </p>
              <p className="text-xs text-neutral-500 max-w-md mx-auto">
                A notification has been routed to <span className="font-mono text-neutral-800 font-medium">{recipient}</span>. Coach Lornette Daye&apos;s team will follow up within 1–2 business days with your enrollment package.
              </p>
            </div>

            {mailtoUrl && (
              <div className="pt-2">
                <a
                  href={mailtoUrl}
                  className="inline-flex items-center gap-2 text-xs font-semibold text-neutral-700 bg-neutral-100 hover:bg-neutral-200 border border-neutral-300 rounded-lg px-4 py-2 transition-colors"
                >
                  <Mail className="w-3.5 h-3.5 text-[var(--champagne)]" />
                  <span>Open Email Client Backup</span>
                </a>
              </div>
            )}

            <div className="pt-4">
              <button
                type="button"
                onClick={() => {
                  setFormData(initialFormState);
                  setSubmitted(false);
                }}
                className="text-xs font-semibold text-[var(--champagne-dark)] hover:underline"
              >
                Register another participant →
              </button>
            </div>
          </div>
        ) : (
          <form onSubmit={handleSubmit} aria-describedby={errorMessage ? "form-error" : undefined} className="space-y-5">
            {/* Header */}
            <div className="flex flex-col sm:flex-row sm:items-baseline justify-between gap-2 pb-2 border-b border-neutral-100">
              <div>
                <h3 className="font-serif text-2xl sm:text-3xl text-black">Program Registration</h3>
                <p className="text-[11px] font-bold uppercase tracking-[0.2em] text-[var(--champagne-dark)] mt-0.5">
                  Join the Next Cohort ↗
                </p>
              </div>
              <p className="text-xs text-neutral-500 sm:text-right max-w-[200px] leading-relaxed">
                Individuals welcome. Limited spots for a more personal experience.
              </p>
            </div>

            {/* Error Message */}
            {errorMessage && (
              <div id="form-error" role="alert" aria-live="assertive" className="p-3 bg-red-50 border border-red-200 rounded-lg text-xs text-red-700">
                {errorMessage}
              </div>
            )}

            {/* Honeypot field */}
            <input
              type="text"
              name="website"
              value={formData.website}
              id="website" onChange={(e) => setFormData({ ...formData, website: e.target.value })}
              className="hidden"
              tabIndex={-1}
              autoComplete="off"
            />

            {/* First & Last Name */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div className="space-y-1.5">
                <label className="block text-xs font-medium text-neutral-700" htmlFor="firstName">
                  First Name <span className="text-amber-700" aria-hidden="true">*</span><span className="sr-only"> (required)</span>
                </label>
                <input
                  type="text"
                  required aria-required="true"
                  placeholder="e.g. Taylor"
                  value={formData.firstName}
                  id="firstName" onChange={(e) => setFormData({ ...formData, firstName: e.target.value })}
                  className="w-full rounded-lg border border-neutral-300 bg-white px-3.5 py-2.5 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-[var(--champagne)] focus:outline-none focus:ring-1 focus:ring-[var(--champagne)]"
                />
              </div>
              <div className="space-y-1.5">
                <label className="block text-xs font-medium text-neutral-700" htmlFor="lastName">
                  Last Name <span className="text-amber-700" aria-hidden="true">*</span><span className="sr-only"> (required)</span>
                </label>
                <input
                  type="text"
                  required aria-required="true"
                  placeholder="e.g. Morgan"
                  value={formData.lastName}
                  id="lastName" onChange={(e) => setFormData({ ...formData, lastName: e.target.value })}
                  className="w-full rounded-lg border border-neutral-300 bg-white px-3.5 py-2.5 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-[var(--champagne)] focus:outline-none focus:ring-1 focus:ring-[var(--champagne)]"
                />
              </div>
            </div>

            {/* Email & Phone */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div className="space-y-1.5">
                <label className="block text-xs font-medium text-neutral-700" htmlFor="email">
                  Email Address <span className="text-amber-700" aria-hidden="true">*</span><span className="sr-only"> (required)</span>
                </label>
                <input
                  type="email"
                  required aria-required="true"
                  placeholder="you@email.com"
                  value={formData.email}
                  id="email" onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                  className="w-full rounded-lg border border-neutral-300 bg-white px-3.5 py-2.5 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-[var(--champagne)] focus:outline-none focus:ring-1 focus:ring-[var(--champagne)]"
                />
              </div>
              <div className="space-y-1.5">
                <label className="block text-xs font-medium text-neutral-700" htmlFor="phone">
                  Phone Number <span className="text-amber-700" aria-hidden="true">*</span><span className="sr-only"> (required)</span>
                </label>
                <input
                  type="tel"
                  required aria-required="true"
                  placeholder="(555) 123-4567"
                  value={formData.phone}
                  id="phone" onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
                  className="w-full rounded-lg border border-neutral-300 bg-white px-3.5 py-2.5 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-[var(--champagne)] focus:outline-none focus:ring-1 focus:ring-[var(--champagne)]"
                />
              </div>
            </div>

            {/* City / State & Home Club */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div className="space-y-1.5">
                <label className="block text-xs font-medium text-neutral-700" htmlFor="cityState">
                  City / State <span className="text-amber-700" aria-hidden="true">*</span><span className="sr-only"> (required)</span>
                </label>
                <input
                  type="text"
                  required aria-required="true"
                  placeholder="e.g. Vancouver, BC or Atlanta, GA"
                  value={formData.cityState}
                  id="cityState" onChange={(e) => setFormData({ ...formData, cityState: e.target.value })}
                  className="w-full rounded-lg border border-neutral-300 bg-white px-3.5 py-2.5 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-[var(--champagne)] focus:outline-none focus:ring-1 focus:ring-[var(--champagne)]"
                />
              </div>
              <div className="space-y-1.5">
                <label className="block text-xs font-medium text-neutral-700" htmlFor="homeClub">
                  Home Club, Course, or Tour
                </label>
                <input
                  type="text"
                  placeholder="e.g. Capilano G&CC / CJGA / NCAA"
                  value={formData.homeClub}
                  id="homeClub" onChange={(e) => setFormData({ ...formData, homeClub: e.target.value })}
                  className="w-full rounded-lg border border-neutral-300 bg-white px-3.5 py-2.5 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-[var(--champagne)] focus:outline-none focus:ring-1 focus:ring-[var(--champagne)]"
                />
              </div>
            </div>

            {/* Handicap & Competitive Role */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div className="space-y-1.5">
                <label className="block text-xs font-medium text-neutral-700" htmlFor="handicapIndex">
                  Current Handicap / Playing Index
                </label>
                <select
                  value={formData.handicapIndex}
                  id="handicapIndex" onChange={(e) => setFormData({ ...formData, handicapIndex: e.target.value })}
                  className="w-full rounded-lg border border-neutral-300 bg-white px-3 py-2.5 text-sm text-neutral-900 focus:border-[var(--champagne)] focus:outline-none focus:ring-1 focus:ring-[var(--champagne)]"
                >
                  <option value="">Select your handicap range</option>
                  <option value="Plus / Scratch (+1.0 or better)">Plus / Scratch (+1.0 or better)</option>
                  <option value="0.0 – 4.9 Index">0.0 – 4.9 Index</option>
                  <option value="5.0 – 9.9 Index">5.0 – 9.9 Index</option>
                  <option value="10.0 – 14.9 Index">10.0 – 14.9 Index</option>
                  <option value="15.0 – 19.9 Index">15.0 – 19.9 Index</option>
                  <option value="20.0+ Index">20.0+ Index</option>
                  <option value="Junior / Unranked Competitive">Junior / Unranked Competitive</option>
                </select>
              </div>
              <div className="space-y-1.5">
                <label className="block text-xs font-medium text-neutral-700" htmlFor="competitiveRole">
                  Competitive Background / Role
                </label>
                <select
                  value={formData.competitiveRole}
                  id="competitiveRole" onChange={(e) => setFormData({ ...formData, competitiveRole: e.target.value })}
                  className="w-full rounded-lg border border-neutral-300 bg-white px-3 py-2.5 text-sm text-neutral-900 focus:border-[var(--champagne)] focus:outline-none focus:ring-1 focus:ring-[var(--champagne)]"
                >
                  <option value="">Select your competitive level</option>
                  <option value="Tournament Amateur / Championship Player">Tournament Amateur / Championship Player</option>
                  <option value="Elite Junior / Collegiate Prospect">Elite Junior / Collegiate Prospect</option>
                  <option value="Club Member / Competitive Weekender">Club Member / Competitive Weekender</option>
                  <option value="PGA Coach / Director of Golf">PGA Coach / Director of Golf</option>
                  <option value="Parent / Guardian of Competitive Golfer">Parent / Guardian of Competitive Golfer</option>
                </select>
              </div>
            </div>

            {/* Referral Source */}
            <div className="space-y-1.5">
              <label className="block text-xs font-medium text-neutral-700" htmlFor="hearAbout">
                  How did you hear about us? <span className="text-amber-700" aria-hidden="true">*</span><span className="sr-only"> (required)</span>
              </label>
              <select
                required aria-required="true"
                value={formData.hearAbout}
                id="hearAbout" onChange={(e) => setFormData({ ...formData, hearAbout: e.target.value })}
                className="w-full rounded-lg border border-neutral-300 bg-white px-3 py-2.5 text-sm text-neutral-900 focus:border-[var(--champagne)] focus:outline-none focus:ring-1 focus:ring-[var(--champagne)]"
              >
                <option value="">Select an option</option>
                <option value="Club / Course Recommendation">Club / Course Recommendation</option>
                <option value="Lornette Daye Speaking Event">Lornette Daye Speaking Event</option>
                <option value="PGA Coach / Pro Recommendation">PGA Coach / Pro Recommendation</option>
                <option value="Colleague or Friend">Colleague or Friend</option>
                <option value="Social Media">Social Media</option>
                <option value="Google / Web Search">Google / Web Search</option>
                <option value="Other">Other</option>
              </select>
            </div>

            {/* Cohort Interest Radios */}
            <div className="space-y-2">
              <label className="block text-xs font-medium text-neutral-700" htmlFor="cohortInterest">
                  Select Your Cohort Interest <span className="text-amber-700" aria-hidden="true">*</span><span className="sr-only"> (required)</span>
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
                <label
                  className={`cursor-pointer rounded-xl border p-3 text-left transition-all ${
                    formData.cohortInterest === "next"
                      ? "border-[var(--champagne)] bg-[#fffcf5] ring-1 ring-[var(--champagne)]"
                      : "border-neutral-200 bg-white hover:bg-neutral-50"
                  }`}
                >
                  <div className="flex items-start gap-2">
                    <input
                      type="radio"
                      name="cohortInterest"
                      value="next"
                      checked={formData.cohortInterest === "next"}
                      onChange={() => setFormData({ ...formData, cohortInterest: "next" })}
                      className="mt-0.5 text-[var(--champagne)] focus:ring-[var(--champagne)] min-w-[24px] min-h-[24px]"
                    />
                    <div>
                      <p className="text-xs font-bold text-neutral-900 leading-tight">
                        Next Available Cohort
                      </p>
                      <p className="mt-1 text-[11px] text-neutral-500 leading-snug">
                        I&apos;m ready to join the next 10-week program.
                      </p>
                    </div>
                  </div>
                </label>

                <label
                  className={`cursor-pointer rounded-xl border p-3 text-left transition-all ${
                    formData.cohortInterest === "future"
                      ? "border-[var(--champagne)] bg-[#fffcf5] ring-1 ring-[var(--champagne)]"
                      : "border-neutral-200 bg-white hover:bg-neutral-50"
                  }`}
                >
                  <div className="flex items-start gap-2">
                    <input
                      type="radio"
                      name="cohortInterest"
                      value="future"
                      checked={formData.cohortInterest === "future"}
                      onChange={() => setFormData({ ...formData, cohortInterest: "future" })}
                      className="mt-0.5 text-[var(--champagne)] focus:ring-[var(--champagne)] min-w-[24px] min-h-[24px]"
                    />
                    <div>
                      <p className="text-xs font-bold text-neutral-900 leading-tight">
                        Future Cohort
                      </p>
                      <p className="mt-1 text-[11px] text-neutral-500 leading-snug">
                        Keep me informed about upcoming dates.
                      </p>
                    </div>
                  </div>
                </label>

                <label
                  className={`cursor-pointer rounded-xl border p-3 text-left transition-all ${
                    formData.cohortInterest === "unsure"
                      ? "border-[var(--champagne)] bg-[#fffcf5] ring-1 ring-[var(--champagne)]"
                      : "border-neutral-200 bg-white hover:bg-neutral-50"
                  }`}
                >
                  <div className="flex items-start gap-2">
                    <input
                      type="radio"
                      name="cohortInterest"
                      value="unsure"
                      checked={formData.cohortInterest === "unsure"}
                      onChange={() => setFormData({ ...formData, cohortInterest: "unsure" })}
                      className="mt-0.5 text-[var(--champagne)] focus:ring-[var(--champagne)] min-w-[24px] min-h-[24px]"
                    />
                    <div>
                      <p className="text-xs font-bold text-neutral-900 leading-tight">
                        Not Sure Yet
                      </p>
                      <p className="mt-1 text-[11px] text-neutral-500 leading-snug">
                        I&apos;d like to learn more before committing.
                      </p>
                    </div>
                  </div>
                </label>
              </div>
            </div>

            {/* Additional Notes */}
            <div className="space-y-1.5">
              <label className="block text-xs font-medium text-neutral-700" htmlFor="notes">
                  Additional Notes (Optional)
              </label>
              <textarea
                rows={3}
                placeholder="Tell us a bit about your goals, experience level, or any questions you have..."
                value={formData.notes}
                id="notes" onChange={(e) => setFormData({ ...formData, notes: e.target.value })}
                className="w-full rounded-lg border border-neutral-300 bg-white px-3.5 py-2.5 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-[var(--champagne)] focus:outline-none focus:ring-1 focus:ring-[var(--champagne)]"
              />
            </div>

            {/* Submit Button */}
            <button
              type="submit"
              disabled={submitting}
              className="w-full flex items-center justify-center gap-2 rounded-xl bg-[var(--champagne)] hover:bg-[#b5954f] text-black font-semibold text-sm px-6 py-3.5 shadow-md hover:shadow-lg transition-all disabled:opacity-50 uppercase tracking-wider"
            >
              {submitting ? (
                <>
                  <Loader2 className="w-4 h-4 animate-spin" />
                  <span>Submitting Registration...</span>
                </>
              ) : (
                <>
                  <span>Register for the Program</span>
                  <span className="text-base">↗</span>
                </>
              )}
            </button>

            {/* Security note */}
            <div className="flex items-center justify-center gap-1.5 text-neutral-400 text-xs pt-1">
              <Lock className="w-3.5 h-3.5" />
              <span>Your information is secure and will never be shared.</span>
            </div>
          </form>
        )}
      </div>
    </div>
  );
}
