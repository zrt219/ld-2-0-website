import type { Metadata } from "next";
import Image from "next/image";
import Link from "next/link";
import {
  Flag,
  HelpCircle,
  Star,
  Target,
  Trophy,
  Users,
} from "lucide-react";

import { GolfRegistrationForm } from "@/components/foundations/GolfRegistrationForm";

export const metadata: Metadata = {
  title: "Register for Golf Program | Lornette’s Foundation Golf",
  description:
    "Register for the 10-Week Guided Athlete Development Program with Olympian Coach Lornette Daye. Build elite mental resilience, focus, and purposeful performance.",
  openGraph: {
    title: "Register for Golf Program | Lornette’s Foundation Golf",
    description:
      "Join the next 10-Week Guided Athlete Development Cohort with Lornette Daye. A Stronger Mind. A Calmer You. A Better Game.",
    images: [
      {
        url: "/foundations/golf/lornette-golf-fairway-composure-sunset.jpg",
        width: 1200,
        height: 630,
        alt: "Lornette Daye on the golf course fairway at sunset",
      },
    ],
  },
};

const valueFeatures = [
  {
    icon: Target,
    title: "MINDSET TRAINING",
    desc: "Build confidence on and off the course.",
  },
  {
    icon: Flag,
    title: "ON-COURSE APPLICATION",
    desc: "Turn insight into real performance.",
  },
  {
    icon: Users,
    title: "SMALL GROUP SUPPORT",
    desc: "Learn with a committed, like-minded community.",
  },
  {
    icon: Trophy,
    title: "LASTING RESULTS",
    desc: "Play with a stronger mind for a more fulfilling game.",
  },
];

const nextSteps = [
  {
    step: "1",
    text: "You'll receive a confirmation email with next steps.",
  },
  {
    step: "2",
    text: "Our team will follow up personally within 1–2 business days.",
  },
  {
    step: "3",
    text: "You'll get details about the program, dates, and how to prepare.",
  },
  {
    step: "4",
    text: "Get ready to invest in a stronger mind, and a better game.",
  },
];

export default function GolfRegisterPage() {
  return (
    <main className="min-h-screen bg-[#faf8f5] text-neutral-900 selection:bg-[var(--gold)] selection:text-black">
      {/* Subnav Breadcrumb */}
      <div className="border-b border-[#e8e2d8] bg-white/80 backdrop-blur-md sticky top-0 z-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex items-center justify-between text-xs">
          <div className="flex items-center gap-2 text-neutral-500">
            <Link href="/foundations" className="hover:text-black transition-colors">
              Foundations
            </Link>
            <span>/</span>
            <Link href="/foundations/golf" className="hover:text-black transition-colors">
              Golf
            </Link>
            <span>/</span>
            <Link href="/foundations/golf/program" className="hover:text-black transition-colors">
              Program
            </Link>
            <span>/</span>
            <span className="font-semibold text-neutral-900">Registration</span>
          </div>
          <Link
            href="#register"
            className="hidden sm:inline-flex items-center gap-1 font-medium text-[var(--champagne-dark)] hover:underline"
          >
            Jump to Application Form &darr;
          </Link>
        </div>
      </div>

      {/* Hero Registration Section */}
      <section className="py-10 sm:py-16 lg:py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-12 items-start">
            {/* Left Column: Context & Imagery */}
            <div className="lg:col-span-6 space-y-8">
              <div className="space-y-3">
                <p className="text-[11px] font-bold uppercase tracking-[0.24em] text-[var(--champagne-dark)]">
                  Lornette’s Foundation Golf
                </p>
                <h1 className="font-serif text-3xl sm:text-4xl lg:text-5xl text-neutral-950 leading-[1.12]">
                  Join the 10-Week Guided Program
                </h1>
                <p className="font-serif text-lg sm:text-xl text-[var(--champagne-dark)] italic">
                  A Stronger Mind. A Calmer You. A Better Game.
                </p>
                <p className="text-sm sm:text-base text-neutral-600 leading-relaxed pt-2">
                  Lornette’s Foundation Golf, powered by the Performance Edge Framework, is a transformational experience designed for individuals, teams, and organizations who are ready to play with greater focus, confidence, and purpose. Choose your path below to register for the next cohort or inquire about bringing the program to your club or organization.
                </p>
              </div>

              {/* 4 Icon Features */}
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-2">
                {valueFeatures.map((feat) => {
                  const Icon = feat.icon;
                  return (
                    <div key={feat.title} className="text-center sm:text-left space-y-1.5">
                      <div className="w-10 h-10 rounded-xl bg-[rgba(198,165,92,0.12)] text-[var(--champagne-dark)] flex items-center justify-center mx-auto sm:mx-0 border border-[rgba(198,165,92,0.3)]">
                        <Icon className="w-5 h-5" />
                      </div>
                      <p className="text-[10px] font-bold uppercase tracking-wider text-neutral-900 leading-tight">
                        {feat.title}
                      </p>
                      <p className="text-[11px] text-neutral-500 leading-snug">
                        {feat.desc}
                      </p>
                    </div>
                  );
                })}
              </div>

              {/* Photographic Card with Lornette Fairway Portrait */}
              <div className="rounded-2xl overflow-hidden border border-[#e5ded4] shadow-xl bg-black relative group">
                <div className="relative aspect-[16/10] sm:aspect-[16/9] w-full">
                  <Image
                    src="/foundations/golf/lornette-golf-fairway-composure-sunset.jpg"
                    alt="Coach Lornette Daye standing on the fairway with golf clubs at sunset"
                    fill
                    sizes="(max-width: 1024px) 100vw, 50vw"
                    className="object-cover object-[center_35%] transition-transform duration-700 group-hover:scale-[1.02]"
                    priority
                  />
                  {/* Subtle dark gradient for high-contrast typography */}
                  <div className="absolute inset-0 bg-gradient-to-t from-black/85 via-black/30 to-transparent" />

                  {/* Editorial Quote */}
                  <div className="absolute inset-x-0 bottom-0 p-5 sm:p-6 text-white space-y-2">
                    <p className="font-serif text-lg sm:text-xl md:text-2xl leading-snug italic max-w-lg text-[#faf7f2]">
                      &ldquo;Performance isn&apos;t just about what you do on the course. It&apos;s about who you become.&rdquo;
                    </p>
                    <p className="text-xs uppercase tracking-[0.2em] text-[var(--champagne)] font-semibold">
                      Coach Lornette Daye &middot; <span className="opacity-90 font-normal">Speaker. Coach. Leader.</span>
                    </p>
                  </div>
                </div>

                {/* Bottom Stat Bar */}
                <div className="grid grid-cols-2 sm:grid-cols-4 divide-y sm:divide-y-0 sm:divide-x divide-neutral-800 bg-[#120f0d] p-3 text-center text-white">
                  <div className="py-2 sm:py-0 px-2">
                    <p className="font-serif text-lg text-[var(--champagne)] font-bold">10</p>
                    <p className="text-[10px] tracking-wider uppercase text-neutral-400">Weeks</p>
                  </div>
                  <div className="py-2 sm:py-0 px-2">
                    <p className="font-serif text-lg text-[var(--champagne)] font-bold">1</p>
                    <p className="text-[10px] tracking-wider uppercase text-neutral-400">Stronger You</p>
                  </div>
                  <div className="py-2 sm:py-0 px-2">
                    <p className="font-serif text-lg text-[var(--champagne)] font-bold">Lifetime</p>
                    <p className="text-[10px] tracking-wider uppercase text-neutral-400">Of Impact</p>
                  </div>
                  <div className="py-2 sm:py-0 px-2 flex items-center justify-center">
                    <p className="text-[10px] uppercase font-medium tracking-wide text-neutral-300 leading-tight">
                      Great golf develops stronger people.
                    </p>
                  </div>
                </div>
              </div>
            </div>

            {/* Right Column: Interactive Registration Form */}
            <div className="lg:col-span-6">
              <GolfRegistrationForm id="register" />
            </div>
          </div>
        </div>
      </section>

      {/* Trust & Next Steps Section */}
      <section className="py-12 sm:py-16 bg-white border-t border-[#e8e2d8]">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-16 items-start">
            {/* Left: Testimonial & Value Pillars */}
            <div className="lg:col-span-7 space-y-6">
              <div className="space-y-2">
                <p className="text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--champagne-dark)]">
                  Trusted by Golfers, Teams, and Clubs
                </p>
                <h2 className="font-serif text-2xl sm:text-3xl text-neutral-950">
                  Real People. Real Progress.
                </h2>
              </div>

              <blockquote className="border-l-2 border-[var(--champagne)] pl-4 italic text-neutral-700 text-sm sm:text-base leading-relaxed">
                &ldquo;The Performance Edge gave me practical tools I could use immediately. I&apos;m more focused, more confident, and I enjoy the game again.&rdquo;
                <footer className="mt-2 not-italic text-xs font-semibold text-neutral-900 flex items-center gap-2">
                  <span>Program Participant</span>
                  <div className="flex text-amber-500">
                    {[...Array(5)].map((_, i) => (
                      <Star key={i} className="w-3.5 h-3.5 fill-amber-400" />
                    ))}
                  </div>
                </footer>
              </blockquote>

              <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-4 border-t border-neutral-100">
                <div className="space-y-1">
                  <div className="flex items-center gap-1.5 text-neutral-900 font-bold text-xs uppercase tracking-wider">
                    <Users className="w-4 h-4 text-[var(--champagne-dark)]" />
                    <span>Individuals</span>
                  </div>
                  <p className="text-xs text-neutral-600 leading-snug">
                    Play with more confidence and purpose.
                  </p>
                </div>
                <div className="space-y-1">
                  <div className="flex items-center gap-1.5 text-neutral-900 font-bold text-xs uppercase tracking-wider">
                    <Flag className="w-4 h-4 text-[var(--champagne-dark)]" />
                    <span>Clubs &amp; Teams</span>
                  </div>
                  <p className="text-xs text-neutral-600 leading-snug">
                    Elevate performance across your members.
                  </p>
                </div>
                <div className="space-y-1">
                  <div className="flex items-center gap-1.5 text-neutral-900 font-bold text-xs uppercase tracking-wider">
                    <Trophy className="w-4 h-4 text-[var(--champagne-dark)]" />
                    <span>Lasting Impact</span>
                  </div>
                  <p className="text-xs text-neutral-600 leading-snug">
                    Skills that extend far beyond the course.
                  </p>
                </div>
              </div>
            </div>

            {/* Right: What Happens Next? */}
            <div className="lg:col-span-5 bg-[#faf8f5] rounded-2xl p-6 sm:p-8 border border-[#e8e2d8] space-y-5">
              <h3 className="font-serif text-xl text-neutral-900">
                What Happens Next?
              </h3>
              <ul className="space-y-3.5">
                {nextSteps.map((s) => (
                  <li key={s.step} className="flex items-start gap-3">
                    <div className="w-6 h-6 rounded-full bg-[var(--champagne)] text-black font-bold text-xs flex items-center justify-center flex-shrink-0 mt-0.5">
                      {s.step}
                    </div>
                    <p className="text-xs sm:text-sm text-neutral-700 leading-snug">
                      {s.text}
                    </p>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Bottom Banner */}
      <section className="bg-[#120f0d] text-white py-12 sm:py-16 border-t border-[rgba(198,165,92,0.3)]">
        <div className="max-w-5xl mx-auto px-4 sm:px-6 text-center space-y-6">
          <p className="text-[11px] font-bold uppercase tracking-[0.24em] text-[var(--champagne)]">
            A Stronger Mind &middot; A Calmer You &middot; A Better Game
          </p>
          <h2 className="font-serif text-3xl sm:text-4xl md:text-5xl text-white">
            Play a More Purposeful Game.
          </h2>
          <div className="pt-2 flex flex-wrap items-center justify-center gap-4">
            <Link
              href="/speaking#inquiry"
              className="inline-flex items-center gap-2 rounded-xl bg-[var(--champagne)] hover:bg-[#b5954f] text-black font-semibold text-xs uppercase tracking-wider px-6 py-3.5 transition-all shadow-lg"
            >
              <HelpCircle className="w-4 h-4" />
              <span>Questions? Contact Us ↗</span>
            </Link>
            <Link
              href="/foundations/golf/club-partnership"
              className="inline-flex items-center gap-2 rounded-xl bg-white/10 hover:bg-white/15 text-white font-medium text-xs uppercase tracking-wider px-6 py-3.5 transition-all border border-white/20"
            >
              <span>Inquire for Your Club</span>
            </Link>
          </div>
        </div>
      </section>
    </main>
  );
}
