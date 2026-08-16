"use client";

import { useState } from "react";

import { siteCopy } from "@/content/site";

export function NewsletterBand() {
  const [message, setMessage] = useState("");
  const [mailtoHref, setMailtoHref] = useState("");

  return (
    <section className="bg-[var(--sand)] px-4 py-12 sm:px-6 lg:px-8">
      <div className="mx-auto grid max-w-7xl gap-6 border-y border-[rgba(198,165,92,0.5)] py-10 lg:grid-cols-[1fr_0.9fr] lg:items-center">
        <div>
          <p className="text-sm font-bold uppercase text-[var(--gold-dark)]">
            Stay Inspired
          </p>
          <h2 className="mt-3 font-serif text-4xl text-[var(--ink)]">
            Insights. Resilience. Purpose.
          </h2>
        </div>
        <form
          className="grid gap-3 sm:grid-cols-[1fr_auto]"
          onSubmit={(event) => {
            event.preventDefault();
            const form = event.currentTarget;
            const email = String(new FormData(form).get("newsletter-email") ?? "");
            setMailtoHref(
              `mailto:${siteCopy.contactEmail}?subject=${encodeURIComponent(
                "Stay Inspired newsletter request",
              )}&body=${encodeURIComponent(
                `Please add me to Lornette Daye updates.\n\nEmail: ${email}`,
              )}`,
            );
            setMessage("Your request is ready to send through your email client.");
          }}
        >
          <label htmlFor="newsletter-email" className="sr-only">
            Email address
          </label>
          <input
            id="newsletter-email"
            name="newsletter-email"
            type="email"
            required
            placeholder="Email address"
            className="min-h-12 border border-[var(--line)] bg-white px-4 text-base"
          />
          <button
            type="submit"
            className="min-h-12 bg-[var(--ink)] px-5 text-sm font-bold uppercase text-[var(--ivory)]"
          >
            Subscribe
          </button>
          {message ? (
            <div className="text-sm text-[#675d50] sm:col-span-2" aria-live="polite">
              <p>{message}</p>
              {mailtoHref ? (
                <a href={mailtoHref} className="mt-2 inline-flex font-bold text-[var(--gold-dark)] underline">
                  Open prepared email
                </a>
              ) : null}
            </div>
          ) : null}
        </form>
      </div>
    </section>
  );
}
