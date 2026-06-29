import type { SiteImage } from "@/content/site";

export type AboutGallerySlide = {
  image: SiteImage;
  title: string;
  body: string;
};

export const canadaSummerGamesSlide: AboutGallerySlide = {
  image: {
    src: "/about-gallery/canada-summer-games-1985.webp",
    alt: "Black-and-white newspaper clipping of Lornette Daye on the medal podium after winning the 200 metre sprint at the 1985 Canada Summer Games.",
    crop: "object-center",
  },
  title: "Lornette at the 1985 Canada Summer Games, winning the 200 metre sprint.",
  body:
    "Lornette's athletic career is one of numerous accolades, winning high school championships, multiple Canada and Western Canada sprint events (including the one above), as well as regional competitions. Competing across Canada, the United States, and even Europe, her commitment to excellence took her far.",
};

export const flightAttendantSlide: AboutGallerySlide = {
  image: {
    src: "/about-gallery/flight-attendant-1993.webp",
    alt: "Lornette Daye in her 1993 flight attendant uniform holding a certificate at a reception.",
    crop: "object-center",
  },
  title: "Lornette as a flight attendant in 1993.",
  body:
    "After her athletic career, Lornette entered the corporate sector, becoming the top flight attendant at her company before transitioning to other industries. She founded multiple soccer and Track & Field clubs both in Canada and abroad, supported non-profit groups such as JANA as a project coordinator, helped Shaw's roll out of fiber optics as a customer service coordinator. From business analysis to project management, Lornette used her skills to support any organization she was a part of.",
};

export const aboutGallerySlides: AboutGallerySlide[] = [
  canadaSummerGamesSlide,
  flightAttendantSlide,
];
