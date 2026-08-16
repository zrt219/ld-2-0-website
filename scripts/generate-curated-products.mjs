import fs from "node:fs";
import path from "node:path";

const allProductsData = [
  // --- CLOTHING & APPAREL ---
  {
    id: "product-01",
    name: "Ivory Long Trench Coat & Tailored Suit Ensemble",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Tailored Suits & Outerwear",
    image: "/products/clean/product-01.png",
    curationReason: "Chosen for Lornette's signature executive stage presence and timeless monochromatic elegance.",
    shortDescription: "A coordinated luxury ivory tailoring set featuring a fluid floor-length trench coat over matching wide-leg trousers.",
    details: [
      "Structured lightweight wool-silk blend with gold LD monogram embroidery",
      "Floor-length duster trench with deep storm flap and belt",
      "Wide-leg high-waisted trousers with tailored front crease",
      "Dry clean only, crafted in small artisanal batches"
    ],
    fabric: "70% Virgin Wool, 30% Mulberry Silk",
    fit: "Tailored contemporary fit with fluid drape",
    editorialQuote: "Confidence is tailored from the inside out."
  },
  {
    id: "product-02",
    name: "Double-Breasted Power Blazer & Wide-Leg Trouser Suit",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Tailored Suits & Blazers",
    image: "/products/clean/product-02.png",
    curationReason: "Designed for boardroom leadership and keynote stages with an empowering sculptural fit.",
    shortDescription: "An elegant ivory double-breasted blazer with gold crest buttons paired with high-waist fluid wide-leg trousers.",
    details: [
      "Double-breasted front with 6 polished gold-tone LD crest buttons",
      "Peak lapel with subtle signature hand-stitching",
      "Fully lined in breathable cupro silk",
      "High-rise palazzo trousers with hidden side zipper"
    ],
    fabric: "100% Fine Italian Wool Crepe",
    fit: "Sculpted silhouette with structured shoulder pads",
    editorialQuote: "Every room you enter should feel your presence before you speak."
  },
  {
    id: "product-03",
    name: "Camel Wool Tailored Blazer",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Tailored Suits & Blazers",
    image: "/products/clean/product-03.png",
    curationReason: "A versatile neutral investment piece pairing effortless authority with relaxed warmth.",
    shortDescription: "A structured camel wool single-breasted blazer worn over a fluid silk camisole and ivory tailored pants.",
    details: [
      "Single-breasted 2-button front in polished horn-effect buttons",
      "Slim notch lapel and functional welt pockets",
      "Interior passport and pen pocket for executive travel",
      "Tailored back vent for ease of movement"
    ],
    fabric: "100% Superfine Camel Wool",
    fit: "Modern relaxed tailoring",
    editorialQuote: "Warmth, authority, and ease in one singular staple."
  },
  {
    id: "product-04",
    name: "Ivory Wrap Midi Dress",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Women's Dresses",
    image: "/products/clean/product-04.png",
    curationReason: "Flattering across body shapes with fluid movement that transitions effortlessly from day engagements to evening receptions.",
    shortDescription: "A flowing ivory midi dress designed with a graceful wrap silhouette, tie belt, and three-quarter sleeves.",
    details: [
      "Self-tie belt with gold-tipped hardware",
      "Graceful surplice V-neckline with modesty snap",
      "Flared A-line midi skirt with fluid asymmetric hem",
      "Wrinkle-resistant double-stretch crepe"
    ],
    fabric: "96% Crepe Polyester, 4% Spandex",
    fit: "Adjustable wrap silhouette",
    editorialQuote: "Elegance is the balance between freedom and intention."
  },
  {
    id: "product-05",
    name: "Cowl Neck Satin Slip Dress",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Women's Dresses",
    image: "/products/clean/product-05.png",
    curationReason: "Liquid gold luster designed for evening galas, award dinners, and private celebrations.",
    shortDescription: "A lustrous champagne liquid satin slip dress featuring an alluring draped cowl neckline and delicate straps.",
    details: [
      "Bias-cut silhouette that drapes gracefully across curves",
      "Delicate adjustable rouleau shoulder straps",
      "Floor-grazing length with subtle side walking slit",
      "Heavyweight lustrous satin that does not cling"
    ],
    fabric: "100% Silk Satin Charm",
    fit: "Fluid bias cut",
    editorialQuote: "Luminous grace that catches the evening light."
  },
  {
    id: "product-06",
    name: "One-Shoulder Drape Evening Gown",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Women's Dresses",
    image: "/products/clean/product-06.png",
    curationReason: "Sculptural drama in rich espresso tones for black-tie galas and milestone celebrations.",
    shortDescription: "A dramatic espresso brown satin evening gown with a sculptural one-shoulder neckline, belted waist, and sweeping train.",
    details: [
      "Architectural one-shoulder drape with interior boned bodice",
      "Detachable gold-buckle satin sash belt",
      "Cascading floor-length skirt with walking train",
      "Concealed side zipper with hook-and-eye closure"
    ],
    fabric: "Heavyweight Duchesse Satin",
    fit: "Structured bodice with flowing column skirt",
    editorialQuote: "Unforgettable grandeur crafted with poise."
  },
  {
    id: "product-07",
    name: "Stand Collar Wool Coat & Sheath Dress",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Women's Outerwear",
    image: "/products/clean/product-07.png",
    curationReason: "A dignified royal-inspired ensemble curated for high-profile ceremonies and speaking events.",
    shortDescription: "A formal cream wool tailored longline coat layered over a draped sheath dress and finished with a structured fascinator hat.",
    details: [
      "Architectural funnel stand collar with concealed snap placket",
      "Matching tailored shift dress with contoured seams",
      "Crafted from insulating double-faced woven wool",
      "Signature tonal jacquard lining"
    ],
    fabric: "90% Virgin Wool, 10% Cashmere",
    fit: "Structured regal silhouette",
    editorialQuote: "Dignity is quiet, steady, and undeniable."
  },
  {
    id: "product-08",
    name: "Tailored Blazer in Camel Wool",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Tailored Suits & Blazers",
    image: "/products/clean/product-08.png",
    curationReason: "An essential wardrobe building block that bridges professional power and casual weekend refinement.",
    shortDescription: "A classic camel wool blazer paired with a crisp ivory silk button-down and deep indigo denim.",
    details: [
      "Structured notch lapels and hand-finished pick stitching",
      "Gold-tone monogram embossed shank buttons",
      "Dual flap front pockets with chest welt pocket",
      "Breathable viscose lining"
    ],
    fabric: "100% Brushed Camel Wool",
    fit: "Classic tailored fit",
    editorialQuote: "The centerpiece of a thoughtfully curated wardrobe."
  },
  {
    id: "product-09",
    name: "Ribbed Knit Polo Top",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Women's Tops and Blouses",
    image: "/products/clean/product-09.png",
    curationReason: "Elevated daily knitwear that brings tactile comfort and understated luxury to travel days.",
    shortDescription: "A finely ribbed caramel knit polo sweater featuring an open collar and gold monogram embroidery.",
    details: [
      "Ultra-fine gauge ribbed knit with shape-recovery yarn",
      "Open spread collar without restrictive buttons",
      "Elbow-length sleeve with reinforced ribbed cuffs",
      "Embroidered tonal LD emblem at the hem"
    ],
    fabric: "70% Fine Merino Wool, 30% Cashmere",
    fit: "Close-to-body flattering stretch",
    editorialQuote: "Tactile warmth for the woman on the move."
  },
  {
    id: "product-10",
    name: "Utility Jacket & Travel Lounge Set",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Women's Outerwear",
    image: "/products/clean/product-10.png",
    curationReason: "Curated for transatlantic speaking tours where effortless comfort meets pristine polished style.",
    shortDescription: "A relaxed ivory utility overshirt jacket styled with matching lounge pants and signature monogram travel luggage.",
    details: [
      "Four front safari flap pockets with gold snap closures",
      "Internal drawstring waist for customizable shape",
      "Matching relaxed tapered trousers with elastic waistband",
      "Water-resistant compact cotton twill"
    ],
    fabric: "100% High-Density Pima Cotton Twill",
    fit: "Relaxed utility silhouette",
    editorialQuote: "Travel in comfort, arrive in command."
  },
  {
    id: "product-11",
    name: "Classic Double-Breasted Trench Coat",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Women's Outerwear",
    image: "/products/clean/product-11.png",
    curationReason: "The ultimate iconic outerwear piece engineered for all-weather executive travel.",
    shortDescription: "An iconic double-breasted camel trench coat with satin lining, styled over pleated trousers and a leather satchel.",
    details: [
      "Weather-treated gabardine with water-repellent finish",
      "Classic gun flap, epaulets, and throat latch",
      "Tortoiseshell buttons and buckled sleeve straps",
      "Removable quilted inner thermal liner"
    ],
    fabric: "100% Cotton Weather-Proof Gabardine",
    fit: "Tailored trench silhouette with waist belt",
    editorialQuote: "Timeless protection against the elements."
  },
  {
    id: "product-12",
    name: "Satin Button-Down Shirt",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Women's Tops and Blouses",
    image: "/products/clean/product-12.png",
    curationReason: "Smooth liquid drape that adds luminous dimension under blazers and statement outerwear.",
    shortDescription: "A silky champagne satin long-sleeve button-down blouse paired with a high-waisted chocolate pencil skirt.",
    details: [
      "Concealed front button placket for a clean minimalist facade",
      "Extended French cuffs with gold button studs",
      "Curved shirttail hem designed for easy tucking",
      "Silk blend that resists creases during long flights"
    ],
    fabric: "92% Mulberry Silk, 8% Elastane",
    fit: "Fluid tailored drape",
    editorialQuote: "Soft to the touch, powerful in perception."
  },
  {
    id: "product-13",
    name: "Tailored Longline Sleeveless Vest",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Women's Outerwear",
    image: "/products/clean/product-13.png",
    curationReason: "A contemporary layering hero piece that elongates the frame and adds architectural flair.",
    shortDescription: "A long ivory sleeveless duster vest layered effortlessly over a bronze silk blouse and pleated wide-leg trousers.",
    details: [
      "Floor-length open front with optional tie belt",
      "Clean notch lapels with sharp architectural tailoring",
      "Deep side slits for dramatic movement while walking",
      "Fully lined in breathable silk habotai"
    ],
    fabric: "80% Woven Viscose, 20% Wool",
    fit: "Longline architectural duster",
    editorialQuote: "Dynamic layers that command the room."
  },
  {
    id: "product-14",
    name: "Tailored Belted Tuxedo Jumpsuit",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Tailored Suits & Blazers",
    image: "/products/clean/product-14.png",
    curationReason: "A modern alternative to evening gowns offering supreme comfort and sharp power styling.",
    shortDescription: "A sculpted ivory tuxedo jumpsuit tailored with notched lapels, a monogram gold buckle belt, and pleated palazzo legs.",
    details: [
      "Satin lapel accents with hidden front zip closure",
      "Detachable gold LD monogram belt",
      "Deep functional side slant pockets",
      "Floor-length palazzo legs with reinforced hems"
    ],
    fabric: "Heavyweight Triacetate Crepe",
    fit: "Sculpted bodice with wide palazzo trousers",
    editorialQuote: "Stage-ready strength in a single piece."
  },
  {
    id: "product-15",
    name: "Men’s Cream Knit Polo",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Men’s Apparel",
    image: "/products/clean/product-15.png",
    curationReason: "Curated for the modern gentleman seeking quiet luxury, breathable comfort, and effortless polish.",
    shortDescription: "A textured cream knit short-sleeve polo shirt featuring a soft collar and tonal monogram embroidery.",
    details: [
      "Fine-gauge breathable cotton-silk yarn",
      "Three-button placket with mother-of-pearl buttons",
      "Ribbed collar, cuffs, and hem that maintain crisp structure",
      "Tonal crest embroidery on left chest"
    ],
    fabric: "60% Organic Cotton, 40% Silk",
    fit: "Modern tailored fit",
    editorialQuote: "Understated masculinity defined by exceptional texture."
  },
  {
    id: "product-16",
    name: "Men’s Tailored Power Blazer",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Men’s Apparel",
    image: "/products/clean/product-16.png",
    curationReason: "Sharp Italian tailoring for executives, keynote speakers, and mentors.",
    shortDescription: "A sophisticated espresso brown wool tailored blazer styled with a crisp white shirt and silk pocket square.",
    details: [
      "Two-button closure with genuine horn buttons",
      "Half-canvas construction for natural chest drape",
      "Soft shoulder construction (spalla camicia)",
      "Double back vents and interior travel pockets"
    ],
    fabric: "100% Super 130s Italian Wool",
    fit: "Contemporary tailored fit",
    editorialQuote: "Command every room with effortless precision."
  },
  {
    id: "product-17",
    name: "Men’s Relaxed Suit Jacket",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Men’s Apparel",
    image: "/products/clean/product-17.png",
    curationReason: "A modern unstructured jacket delivering executive authority with casual ease.",
    shortDescription: "A textured camel single-breasted sport jacket worn over a fine-gauge cream crewneck sweater and taupe trousers.",
    details: [
      "Unlined back and soft unpadded shoulders for maximum comfort",
      "Patch pockets and ticket pocket for relaxed styling",
      "Slightly shortened modern jacket length",
      "Breathable hopsack weave resistant to wrinkles"
    ],
    fabric: "100% Wool Hopsack",
    fit: "Unstructured relaxed tailoring",
    editorialQuote: "Refined comfort for modern changemakers."
  },
  {
    id: "product-18",
    name: "Men’s Linen Resort Shirt",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Men’s Apparel",
    image: "/products/clean/product-18.png",
    curationReason: "Pure luxury linen for warm climates, summit retreats, and relaxed executive travel.",
    shortDescription: "A breathable ivory linen long-sleeve button-down shirt paired with drawstring trousers for luxury resort styling.",
    details: [
      "Pre-washed French flax linen with soft vintage hand-feel",
      "Camp collar with convertible top loop button",
      "Reinforced side gussets and chest pocket",
      "Naturally cooling and moisture-wicking"
    ],
    fabric: "100% European Flax Linen",
    fit: "Relaxed resort fit",
    editorialQuote: "Natural breathability meets intentional design."
  },
  {
    id: "product-19",
    name: "Sport Luxe Tennis Polo Dress",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Sport Luxe & Active",
    image: "/products/clean/product-19.png",
    curationReason: "Drawing upon Lornette's athletic legacy, blending championship performance with country club refinement.",
    shortDescription: "Luxury cream-toned athletic tennis dress featuring a zipped bodice, pleated skirt, and coordinating knit men's polo.",
    details: [
      "Four-way stretch moisture-wicking pique knit",
      "Half-zip front with gold-toned monogram puller",
      "Sunburst micro-pleated skirt with built-in compression shorts",
      "UPF 50+ UV sun protection"
    ],
    fabric: "78% Recycled Polyamide, 22% Elastane",
    fit: "Athletic fitted bodice with flared pleated skirt",
    editorialQuote: "Championship mindset in every single stride."
  },
  {
    id: "product-20",
    name: "Luxe Track Jacket & Performance Legging Set",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Sport Luxe & Active",
    image: "/products/clean/product-20.png",
    curationReason: "A high-performance activewear tracksuit tailored for athlete training, travel days, and off-duty mornings.",
    shortDescription: "Tailored cream zip-front track jackets with matching high-waisted performance leggings and athletic joggers.",
    details: [
      "Buttery-soft double-knit performance fabric",
      "Gold zippered pockets and high mock-neck collar",
      "High-rise 4.5-inch waistband with zero roll-down support",
      "Laser-cut ventilation zones for breathability"
    ],
    fabric: "80% Micro-Nylon, 20% Spandex",
    fit: "Sculpting compression fit",
    editorialQuote: "Train with purpose, move with grace."
  },
  {
    id: "product-21",
    name: "Support Sports Bra & Performance Legging Set",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Sport Luxe & Active",
    image: "/products/clean/product-21.png",
    curationReason: "Engineered for high-impact support while maintaining a silky matte luxury finish.",
    shortDescription: "Monochrome cream sports bra and sculpting high-waist performance leggings paired with an airy hooded layering duster.",
    details: [
      "Reinforced crossover straps with supportive underbust band",
      "Removable breathable molded cups",
      "Seamless inner thigh construction to eliminate chafing",
      "Quick-dry and anti-odor antimicrobial yarn"
    ],
    fabric: "High-Gauge Supplex Lycra",
    fit: "Maximum support & compression",
    editorialQuote: "Built for peak resilience and athletic focus."
  },
  {
    id: "product-22",
    name: "Ribbed Knit Lounge Set with Wrap Robe",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Lounge & Wellness Wear",
    image: "/products/clean/product-22.png",
    curationReason: "Luxurious restorative loungewear for quiet reflection and morning mindfulness rituals.",
    shortDescription: "Ribbed cream athletic bralette and compression leggings styled effortlessly with an oversized lightweight lounge kimono.",
    details: [
      "Ultra-soft modal-cashmere ribbed knit",
      "Includes scoop crop top, wide lounge pants, and draped kimono robe",
      "Elasticated waistband with silk drawstring cord",
      "Naturally thermo-regulating and anti-static"
    ],
    fabric: "48% Modal, 47% Cotton, 5% Cashmere",
    fit: "Relaxed drape lounge fit",
    editorialQuote: "Rest is the foundation of enduring excellence."
  },
  {
    id: "product-23",
    name: "Tailored Ivory Jumpsuit with Organza Cape",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Tailored Suits & Outerwear",
    image: "/products/clean/product-23.png",
    curationReason: "A showstopping red-carpet couture piece combining sharp tailoring with ethereal golden organza.",
    shortDescription: "Impeccably tailored ivory sleeveless wide-leg jumpsuit accented with a gold LD buckle belt and cascading golden organza cape.",
    details: [
      "Detachable sheer gold silk organza cape that floats with movement",
      "Sleeveless jewel-neck tailored jumpsuit with structured bustier",
      "Signature gold LD buckle belt at the natural waist",
      "Concealed center-back zipper"
    ],
    fabric: "Jumpsuit: Heavy Crepe; Cape: 100% Silk Organza",
    fit: "Fitted waist with sweeping cape",
    editorialQuote: "Step forward with power and divine grace."
  },
  {
    id: "product-24",
    name: "Resort Crinkle Chiffon Kaftan Dress",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Women's Dresses",
    image: "/products/clean/product-24.png",
    curationReason: "Weightless breathability for warm-weather coastal retreats and summit gatherings.",
    shortDescription: "Breezy floor-length ivory crinkle chiffon kaftan dress with draped batwing sleeves and gold monogram detailing.",
    details: [
      "Airy semi-sheer crinkled chiffon with full-length slip included",
      "Plunging V-neck with gold tassel drawstring ties",
      "Voluminous batwing sleeves that catch the ocean breeze",
      "Deep side walking vents"
    ],
    fabric: "100% Organic Crinkle Silk Chiffon",
    fit: "Voluminous one-size flowing drape",
    editorialQuote: "Effortless freedom under sunlit skies."
  },
  {
    id: "product-25",
    name: "UMATTR Bridal Ivory Satin Pajama & Robe Set",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Lounge & Wellness Wear",
    image: "/products/clean/product-25.png",
    curationReason: "The pinnacle of bedtime luxury, offering skin-soothing Mulberry silk for restorative beauty sleep.",
    shortDescription: "Lustrous ivory silk-satin pajama set featuring a tailored button-down shirt, fluid wide-leg pants, and a floor-length robe.",
    details: [
      "22-Momme Grade 6A pure Mulberry silk",
      "Contrast champagne silk piping along collar, pocket, and cuffs",
      "Includes longline dressing robe with wide sash belt",
      "Hypoallergenic and friction-free for skin and hair health"
    ],
    fabric: "100% Pure 22-Momme Mulberry Silk",
    fit: "Fluid relaxed fit",
    editorialQuote: "Every night's rest is an act of self-honor."
  },
  {
    id: "product-26",
    name: "Ribbed Knit Lounge Set with Satin Robe",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Lounge & Wellness Wear",
    image: "/products/clean/product-26.png",
    curationReason: "Contrast textural styling pairing soft ribbed knit separates with a smooth satin lounging coat.",
    shortDescription: "Soft-ribbed ivory knit lounge top and wide-leg trousers topped with a contrasting bronze satin robe with fine piping.",
    details: [
      "Three-piece capsule: Ribbed tank, ribbed lounge pants, and satin kimono",
      "Rich bronze satin with ivory satin lapel piping",
      "Deep patch pockets on robe for practical ease",
      "Machine washable on delicate silk cycle"
    ],
    fabric: "Silk-Modal Blend & Duchesse Satin",
    fit: "Relaxed lounging silhouette",
    editorialQuote: "Comfort that never compromises elegance."
  },
  {
    id: "product-52",
    name: "UMATTR The Curated Lifestyle & Beauty Wardrobe",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Tailored Suits & Luxury Apparel",
    image: "/products/clean/product-52.png",
    curationReason: "An overarching campaign featuring neutral tailoring, silk blouses, knitwear, and beauty ritual essentials across generations.",
    shortDescription: "A multi-generational campaign showcase celebrating timeless luxury tailoring, silk blouses, and beauty essentials.",
    details: [
      "Curated capsule collection designed for cohesive mix-and-match styling",
      "Features neutral ivory, camel, and bronze palettes",
      "Includes tailored suits, silk separates, and lifestyle accessories",
      "Sustainably crafted with heirloom-quality standards"
    ],
    fabric: "Curated Silk, Wool & Cashmere Blends",
    fit: "Universal bespoke fits",
    editorialQuote: "Timeless style passed through generations."
  },
  {
    id: "product-54",
    name: "UMATTR Couture Tailoring & Ready-to-Wear Capsule",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Suits, Separates & Outerwear",
    image: "/products/clean/product-54.png",
    curationReason: "A luxury ready-to-wear collection displaying men's and women's tailored suits, silk separates, and leather travel totes.",
    shortDescription: "A luxury ready-to-wear collection displaying men's and women's tailored suits, silk separates, and leather tote bags.",
    details: [
      "Comprehensive wardrobe system for speaking engagements and summits",
      "Signature gold LD hardware and tailored finishes",
      "Coordinated travel totes and weekender luggage",
      "Designed in Canada, crafted in Italy"
    ],
    fabric: "Italian Suiting Wools & Silk Blends",
    fit: "Tailored executive fit",
    editorialQuote: "Tailored with purpose, worn with pride."
  },
  {
    id: "product-72",
    name: "UMATTR Brand Collective Lifestyle Ensemble",
    categorySlug: "clothing-apparel",
    categoryName: "Luxury Clothing & Apparel",
    subcategory: "Apparel & Lifestyle Ensemble",
    image: "/products/clean/product-72.png",
    curationReason: "The ultimate brand collective celebrating the entire UMATTR ecosystem across apparel, beauty, and wellness.",
    shortDescription: "A brand campaign ensemble showcasing models in luxury knitwear and tailored suiting surrounded by the complete beauty, crown care, wellness, and leather goods collection.",
    details: [
      "The complete UMATTR lifestyle ecosystem in one cohesive visual narrative",
      "Featuring luxury knitwear, suiting, skincare, and footwear",
      "Created under the visionary direction of Lornette Daye",
      "Exemplifying grace, resilience, and unapologetic self-worth"
    ],
    fabric: "Complete Brand Collective",
    fit: "Inclusive luxury sizing",
    editorialQuote: "You matter. Your journey matters. Live with purpose."
  },

  // --- FOOTWEAR & SHOES ---
  {
    id: "product-27",
    name: "UMATTR Everyday Loafer & Ballet Flat",
    categorySlug: "footwear-shoes",
    categoryName: "Footwear & Shoes",
    subcategory: "Dress & Everyday Shoes",
    image: "/products/clean/product-27.png",
    curationReason: "Butter-soft Italian calfskin engineered for day-long walking comfort without sacrificing polish.",
    shortDescription: "Supple cognac brown leather penny loafers with gold LD hardware beside butter-soft ivory leather ballet flats.",
    details: [
      "Handcrafted in Italy from full-grain calfskin leather",
      "Cushioned memory foam arch support footbed",
      "Gold-tone LD horsebit buckle hardware",
      "Durable non-slip leather and rubber outsole"
    ],
    fabric: "100% Italian Calf Leather",
    fit: "True to size with gentle break-in comfort",
    editorialQuote: "Every stride rooted in grounded confidence."
  },
  {
    id: "product-28",
    name: "UMATTR Luxury Court White Sneaker",
    categorySlug: "footwear-shoes",
    categoryName: "Footwear & Shoes",
    subcategory: "Luxury Sneakers",
    image: "/products/clean/product-28.png",
    curationReason: "The essential modern luxury sneaker pairing clean minimalist lines with athletic-grade cushioning.",
    shortDescription: "Handcrafted low-top leather and suede court sneaker with gold-tone LD lace plate and molded rubber cupsole.",
    details: [
      "Premium white nappa leather upper with suede mudguard accents",
      "Gold-embossed LD monogram on tongue and heel tab",
      "Ergonomic shock-absorbing removable insole",
      "Vulcanized rubber sole for lasting durability"
    ],
    fabric: "100% Nappa Leather Upper, Rubber Outsole",
    fit: "Standard medium width with supportive arch",
    editorialQuote: "Athletic agility meets executive sophistication."
  },
  {
    id: "product-29",
    name: "UMATTR Architectural Stiletto Pump",
    categorySlug: "footwear-shoes",
    categoryName: "Footwear & Shoes",
    subcategory: "Heels & Pumps",
    image: "/products/clean/product-29.png",
    curationReason: "A sculptural, empowering pointed pump designed to elongate the posture on stage.",
    shortDescription: "Sculptural pointed-toe pumps in smooth ivory leather highlighted by an architectural metallic gold heel and emblem.",
    details: [
      "85mm (3.3 inch) architectural metallic gold flare heel for stable footing",
      "Elongated pointed toe with low-cut vamp",
      "Padded leather insole with reinforced metatarsal cushion",
      "Signature red-tan leather sole with gold monogram stud"
    ],
    fabric: "100% Smooth Kidskin Leather",
    fit: "Snug secure heel grip with cushioned ball of foot",
    editorialQuote: "Rise to your full height with unwavering grace."
  },
  {
    id: "product-30",
    name: "UMATTR Knee-High Leather Riding Boot",
    categorySlug: "footwear-shoes",
    categoryName: "Footwear & Shoes",
    subcategory: "Boots",
    image: "/products/clean/product-30.png",
    curationReason: "Rich dark espresso calfskin boots that deliver commanding elegance over jeans or under midi skirts.",
    shortDescription: "Rich dark espresso calfskin knee-high riding boots with an ankle strap closure, gold LD buckle, and stacked block heel.",
    details: [
      "Hand-burnished espresso calfskin shaft with full inner zip",
      "50mm (2 inch) stacked leather block heel for all-day wear",
      "Ankle harness strap accented with polished gold LD buckle",
      "Hidden elastic calf gusset for flexible comfort"
    ],
    fabric: "100% Burnished Calfskin Leather",
    fit: "Tailored shaft with flexible calf gusset",
    editorialQuote: "Commanding craftsmanship built to endure every season."
  },
  {
    id: "product-68",
    name: "UMATTR Signature Footwear Collection Suite",
    categorySlug: "footwear-shoes",
    categoryName: "Footwear & Shoes",
    subcategory: "Footwear Collection",
    image: "/products/clean/product-68.png",
    curationReason: "The complete luxury footwear wardrobe covering sneakers, flats, pumps, and riding boots.",
    shortDescription: "An expansive boutique showcase of handcrafted Italian leather pumps, monogram horsebit loafers, knee-high boots, and sleek low-top sneakers.",
    details: [
      "Curated footwear wardrobe engineered for modern executive life",
      "Handcrafted by third-generation Italian shoemakers",
      "Consistent memory foam cushioning across all silhouettes",
      "Includes custom dust bags and cedar shoe trees"
    ],
    fabric: "Full-Grain Italian Leather & Suede",
    fit: "Engineered ergonomic lasts",
    editorialQuote: "Step forward with unwavering conviction."
  },

  // --- BAGS, JEWELRY & ACCESSORIES ---
  {
    id: "product-31",
    name: "UMATTR Structured Leather Handbag",
    categorySlug: "bags-accessories",
    categoryName: "Bags, Jewelry & Accessories",
    subcategory: "Handbags & Totes",
    image: "/products/clean/product-31.png",
    curationReason: "Architectural top-handle bag designed as the cornerstone accessory for the modern leader.",
    shortDescription: "Structured ivory leather top-handle satchel with hand-painted contrast edges and a gleaming square gold LD clasp.",
    details: [
      "Structured box calfskin with hand-lacquered edges",
      "Custom 24k gold-plated LD turnlock clasp",
      "Detachable and adjustable leather crossbody strap",
      "Interior divided into two main compartments with zip pocket"
    ],
    fabric: "100% Full-Grain Box Calfskin",
    fit: "Compact structured silhouette",
    editorialQuote: "Carrying authority, poise, and purpose."
  },
  {
    id: "product-32",
    name: "UMATTR Everyday Executive Work Tote",
    categorySlug: "bags-accessories",
    categoryName: "Bags, Jewelry & Accessories",
    subcategory: "Handbags & Totes",
    image: "/products/clean/product-32.png",
    curationReason: "Spacious luxury tote engineered to hold a 15-inch laptop, planner, and daily travel essentials.",
    shortDescription: "Spacious pebbled cognac leather tote bag with compartmentalized organizers, gold LD charm, and matching desk accessories.",
    details: [
      "Supple scratch-resistant pebbled leather",
      "Padded central compartment for 15-inch laptop and tablet",
      "Reinforced dual shoulder straps with comfortable 10-inch drop",
      "Protective gold metal base feet"
    ],
    fabric: "100% Pebbled Grain Cowhide",
    fit: "Generous capacity with structured base",
    editorialQuote: "Organized excellence for the visionary leader."
  },
  {
    id: "product-33",
    name: "UMATTR Pleated Satin Evening Clutch",
    categorySlug: "bags-accessories",
    categoryName: "Bags, Jewelry & Accessories",
    subcategory: "Clutches & Evening",
    image: "/products/clean/product-33.png",
    curationReason: "A radiant champagne satin clutch that gleams under evening chandeliers and gala lighting.",
    shortDescription: "Radiant pleated champagne satin hard-frame evening clutch featuring a gathered sunburst design and polished gold LD emblem.",
    details: [
      "Artisan-pleated champagne silk satin over rigid metal frame",
      "Concealed magnetic clasp closure with gold emblem",
      "Includes drop-in gold snake chain strap",
      "Sized to hold large smartphones, lipstick, and keys"
    ],
    fabric: "100% Silk Satin & Gold Brass Frame",
    fit: "Handheld or shoulder chain wear",
    editorialQuote: "A luminous companion for celebration nights."
  },
  {
    id: "product-34",
    name: "UMATTR Weekender Bag & Travel Luggage Suite",
    categorySlug: "bags-accessories",
    categoryName: "Bags, Jewelry & Accessories",
    subcategory: "Luggage & Travel",
    image: "/products/clean/product-34.png",
    curationReason: "Four-piece luxury travel luggage suite designed for seamless transitions through international airports.",
    shortDescription: "Four-piece luxury travel ensemble comprising ribbed cream spinner suitcases, a cognac leather weekender, and a structured cosmetic case.",
    details: [
      "Durable polycarbonate hard-shell carry-on with 360-degree silent spinner wheels",
      "Pebbled leather weekender duffel with trolley pass-through sleeve",
      "TSA-approved integrated combination locks",
      "Waterproof structured vanity beauty train case"
    ],
    fabric: "Polycarbonate Shell & Full-Grain Leather",
    fit: "Universal airline overhead carry-on compliant",
    editorialQuote: "Every journey begins with intentional preparation."
  },
  {
    id: "product-35",
    name: "UMATTR Signature Gold Jewelry Suite",
    categorySlug: "bags-accessories",
    categoryName: "Bags, Jewelry & Accessories",
    subcategory: "Fine Jewelry",
    image: "/products/clean/product-35.png",
    curationReason: "Heirloom-quality 18k gold vermeil jewelry designed to catch the light and frame the face with warmth.",
    shortDescription: "Polished yellow gold signature jewelry suite comprising an engraved signet ring, medallion pendant, chunky hoops, and toggle link bracelet.",
    details: [
      "18k Yellow Gold Vermeil over sterling silver (5-micron thickness)",
      "Includes chunky hollow hoops, toggle bracelet, medallion pendant, and signet ring",
      "Engraved with the inspirational UMATTR crest",
      "Hypoallergenic and tarnish-resistant protective coating"
    ],
    fabric: "18k Gold Vermeil on 925 Sterling Silver",
    fit: "Adjustable clasp lengths and comfort-fit ring sizes",
    editorialQuote: "Heirloom warmth that reflects your inner shine."
  },
  {
    id: "product-36",
    name: "UMATTR Signature Accessories & Eyewear Set",
    categorySlug: "bags-accessories",
    categoryName: "Bags, Jewelry & Accessories",
    subcategory: "Hats, Scarves & Eyewear",
    image: "/products/clean/product-36.png",
    curationReason: "Curated lifestyle finishers including UV400 sunglasses, pure silk square scarf, and embroidered hats.",
    shortDescription: "Curated lifestyle accessory ensemble featuring an ivory baseball cap, caramel bucket hat, silk square scarf, and tortoiseshell sunglasses.",
    details: [
      "Hand-polished Italian acetate sunglasses with 100% UVA/UVB polarized lenses",
      "90cm x 90cm pure Mulberry silk twill scarf with hand-rolled edges",
      "Embroidered cotton-twill cap and wool-felt bucket hat",
      "Packaged in custom presentation box"
    ],
    fabric: "Italian Acetate, 100% Silk Twill, Cotton Twill",
    fit: "Universal sizing",
    editorialQuote: "The finishing touches that complete the story."
  },
  {
    id: "product-38",
    name: "UMATTR Gold Signature Monogram Hair Pin",
    categorySlug: "bags-accessories",
    categoryName: "Bags, Jewelry & Accessories",
    subcategory: "Hair Jewelry & Accessories",
    image: "/products/clean/product-38.png",
    curationReason: "A polished gold jewelry hair clip designed to elevate loose waves, updos, and protective styles.",
    shortDescription: "A luxury gold-tone monogram hair pin clipped into glossy, voluminous cascading waves.",
    details: [
      "18k gold-plated brass with high-mirror polish",
      "Secure alligator clip mechanism with silicone grip lining",
      "Won't snag or pull delicate hair strands",
      "Presented in velvet keepsake pouch"
    ],
    fabric: "18k Gold-Plated Solid Brass",
    fit: "Gentle non-slip grip",
    editorialQuote: "Crowning your hair with refined gold luster."
  },
  {
    id: "product-39",
    name: "UMATTR Signature Monogram Hair Pin & Curly Bob",
    categorySlug: "bags-accessories",
    categoryName: "Bags, Jewelry & Accessories",
    subcategory: "Hair Jewelry & Accessories",
    image: "/products/clean/product-39.png",
    curationReason: "Showcases the iconic gold monogram clip on textured, defined curls and short crop cuts.",
    shortDescription: "An iconic gold monogram hair accessory styled into defined, voluminous shoulder-length curls.",
    details: [
      "Engineered with curved architecture to hug the scalp naturally",
      "Lightweight construction for all-day comfort",
      "Tarnish-resistant clear e-coating",
      "Versatile styling on natural curls, waves, or sleek wraps"
    ],
    fabric: "18k Gold-Plated Brass",
    fit: "Curved anatomical clip",
    editorialQuote: "Celebrate the unique beauty of your crown."
  },
  {
    id: "product-51",
    name: "UMATTR Curated Signature Luxury Gift Box",
    categorySlug: "bags-accessories",
    categoryName: "Bags, Jewelry & Accessories",
    subcategory: "Luxury Gift Sets",
    image: "/products/clean/product-51.png",
    curationReason: "The quintessential executive appreciation gift featuring silk scarves, gold jewelry, and leather goods.",
    shortDescription: "An opulent unboxing gift hamper featuring a chain-print silk scarf, leather jewelry case, gold cuff bracelet, and skincare sachets.",
    details: [
      "Handcrafted rigid presentation box with gold satin pull ribbon",
      "Includes 100% silk twill scarf, travel leather jewelry case, and gold cuff",
      "Scented packaging with custom embossed note card",
      "The perfect gift for executive milestones and graduations"
    ],
    fabric: "Curated Silk, Leather & Gold Accessories",
    fit: "Delivered gift-ready",
    editorialQuote: "Honoring those who make an indelible difference."
  },
  {
    id: "product-69",
    name: "UMATTR Handbag & Small Leather Goods Collection",
    categorySlug: "bags-accessories",
    categoryName: "Bags, Jewelry & Accessories",
    subcategory: "Handbags & Small Leather Goods",
    image: "/products/clean/product-69.png",
    curationReason: "A comprehensive leather goods suite covering totes, crossbody bags, clutches, and matching wallets.",
    shortDescription: "A timeless collection of pebbled leather tote bags, top-handle satchels, crescent hobo bags, crossbody purses, and matching zip wallets.",
    details: [
      "Consistent full-grain leather palette across all bag silhouettes",
      "Custom gold LD monogram zipper pulls and hardware",
      "Lined with wipe-clean stain-resistant microfiber suede",
      "Handcrafted in Florence, Italy"
    ],
    fabric: "100% Full-Grain Italian Leather",
    fit: "Varied functional capacities",
    editorialQuote: "Craftsmanship that holds your world together."
  },
  {
    id: "product-70",
    name: "UMATTR Signature Accessories & Jewelry Showcase",
    categorySlug: "bags-accessories",
    categoryName: "Bags, Jewelry & Accessories",
    subcategory: "Jewelry & Finishers",
    image: "/products/clean/product-70.png",
    curationReason: "An expansive showcase of watches, silk scarves, sunglasses, and gold jewelry pieces.",
    shortDescription: "A curated showcase of fine gold jewelry, classic leather-strap timepieces, Italian silk scarves, tailored leather belts, and designer sunglasses.",
    details: [
      "Swiss-movement leather timepieces with sapphire crystal",
      "Reversible Italian leather belts with interchangeable gold LD buckles",
      "100% silk twill printed scarves and pocket squares",
      "Polarized acetate sunglasses with UV400 protection"
    ],
    fabric: "Swiss Movements, Italian Leather & Silk",
    fit: "Universal adjustable fits",
    editorialQuote: "Every detail matters."
  },

  // --- HAIR & CROWN CARE ---
  {
    id: "product-37",
    name: "UMATTR Crown Luxury Wig & Style Showcase",
    categorySlug: "hair-crown-care",
    categoryName: "Hair & Crown Care (Wigs & Extensions)",
    subcategory: "Luxury Wigs & Extensions",
    image: "/products/clean/product-37.png",
    curationReason: "Four couture human hair hairstyles showing versatile transitions between sleek straight, wavy, and textured cuts.",
    shortDescription: "A campaign showcase featuring four couture hair styles ranging from sleek straight strands to bouncy waves and precision bob cuts.",
    details: [
      "100% Virgin cuticle-aligned human hair",
      "HD transparent Swiss lace front for an undetectable hairline",
      "Pre-plucked natural hair density with delicate baby hairs",
      "Can be heat styled, dyed, and customized"
    ],
    fabric: "100% Virgin Cuticle-Aligned Human Hair",
    fit: "Customizable 21.5 - 23.5 inch breathable mesh cap",
    editorialQuote: "Your hair is your crown—wear it with absolute pride."
  },
  {
    id: "product-40",
    name: "UMATTR Crown Braids, Locs & Gold Hair Cuffs",
    categorySlug: "hair-crown-care",
    categoryName: "Hair & Crown Care (Wigs & Extensions)",
    subcategory: "Protective Styling & Accents",
    image: "/products/clean/product-40.png",
    curationReason: "Celebrates protective styling artistry, micro braids, and textured locs adorned with gold accents.",
    shortDescription: "Protective styling couture featuring micro box braids and textured locs accented with polished gold hair cuffs.",
    details: [
      "Lightweight featherlight braiding hair that prevents scalp tension",
      "Includes set of 12 adjustable 18k gold-plated filigree hair cuffs",
      "Pre-stretched and hot-water setting friendly",
      "Gentle on edges and promotes healthy hair growth beneath"
    ],
    fabric: "Ultra-Fine Synthetic Braiding Fiber & Gold Cuffs",
    fit: "Featherweight protective styling",
    editorialQuote: "Ancestral beauty woven with royal distinction."
  },
  {
    id: "product-42",
    name: "UMATTR Crown Wig Care & Styling Essentials Kit",
    categorySlug: "hair-crown-care",
    categoryName: "Hair & Crown Care (Wigs & Extensions)",
    subcategory: "Wig Care & Tools",
    image: "/products/clean/product-42.png",
    curationReason: "A complete maintenance suite designed to prolong the lifespan and luster of luxury human hair units.",
    shortDescription: "A comprehensive wig maintenance kit containing conditioning cleansers, care mists, a folding wig stand, and a silk storage bag.",
    details: [
      "Sulfate-free revitalizing wig shampoo and leave-in moisture mist",
      "Collapsible rose-gold wig display stand for air drying",
      "Wide-tooth anti-static detangling comb and edge brush",
      "Zippered satin-lined protective travel storage bag"
    ],
    fabric: "Botanical Formulations & Satin Storage",
    fit: "Universal wig maintenance",
    editorialQuote: "Preserve the luster and vitality of your crown."
  },
  {
    id: "product-50",
    name: "UMATTR Crown Deep Repair Mask & Botanical Herbal Kit",
    categorySlug: "hair-crown-care",
    categoryName: "Hair & Crown Care (Wigs & Extensions)",
    subcategory: "Scalp & Hair Treatments",
    image: "/products/clean/product-50.png",
    curationReason: "Rich botanical hair masks infused with fresh aloe, chebe, and ginger root to restore moisture.",
    shortDescription: "Rejuvenating scalp scrubs, deep repair hair masks, and mineral clay powders infused with fresh aloe and ginger root.",
    details: [
      "Infused with organic aloe vera, chebe powder, and rosemary extract",
      "Intensive restorative hydration for dry, heat-treated, or brittle strands",
      "Includes bamboo application spoon and mixing bowl",
      "Free from sulfates, parabens, mineral oils, and synthetic silicones"
    ],
    fabric: "Organic Aloe, Shea Butter & Cold-Pressed Oils",
    fit: "Suitable for all hair curl types (1A to 4C)",
    editorialQuote: "Deep nourishment rooted in botanical wisdom."
  },
  {
    id: "product-57",
    name: "UMATTR Crown Clip-In Extensions & Ponytails",
    categorySlug: "hair-crown-care",
    categoryName: "Hair & Crown Care (Wigs & Extensions)",
    subcategory: "Hair Extensions",
    image: "/products/clean/product-57.png",
    curationReason: "Instant volume and length with seamless silicone-cushioned clips that protect natural hair.",
    shortDescription: "Premium multi-tonal human hair clip-in extensions, ponytail wraps, and curated wigs presented on elegant styling stands.",
    details: [
      "7-piece seamless clip-in set (160 grams of double-drawn hair)",
      "Ultra-thin silicone polyurethane wefts that lay completely flat",
      "Includes wraparound drawstring ponytail extension",
      "Available in 12 natural multi-dimensional shades"
    ],
    fabric: "100% Double-Drawn Remy Human Hair",
    fit: "Seamless lay-flat application",
    editorialQuote: "Instant volume and versatility on your own terms."
  },
  {
    id: "product-58",
    name: "UMATTR Crown Custom Wig Collection",
    categorySlug: "hair-crown-care",
    categoryName: "Hair & Crown Care (Wigs & Extensions)",
    subcategory: "Luxury Wigs & Extensions",
    image: "/products/clean/product-58.png",
    curationReason: "A curated pedestal showcase of lace front, closure, braided, and textured crown units.",
    shortDescription: "An elevated showcase of luxury lace front, closure, braided, and textured crown wigs perched on gold-accented display pedestals.",
    details: [
      "Individually hand-tied swiss lace closures and 13x6 lace frontals",
      "Custom bleached knots and pre-tinted lace matching diverse complexions",
      "Built-in adjustable elastic piano strap for glueless security",
      "Heat resistant and washable for lasting wear"
    ],
    fabric: "100% Pure Virgin Cuticle Hair",
    fit: "Glueless adjustable cap construction",
    editorialQuote: "A crown designed specifically for your story."
  },
  {
    id: "product-60",
    name: "UMATTR Crown Wig Storage & Care Set",
    categorySlug: "hair-crown-care",
    categoryName: "Hair & Crown Care (Wigs & Extensions)",
    subcategory: "Wig Care & Tools",
    image: "/products/clean/product-60.png",
    curationReason: "Luxury train case and satin storage system for the woman traveling with multiple crown units.",
    shortDescription: "A luxury wig care and maintenance kit featuring a canvas styling stand, satin protective bags, vegan leather train case, detangling combs, and conditioning spray.",
    details: [
      "Hard-shell vegan leather travel train case with mirror and compartments",
      "Three monogrammed satin storage pouches",
      "Cork canvas styling block head with clamp",
      "Organic silk sheen finishing mist"
    ],
    fabric: "Vegan Leather Case & Pure Satin Pouches",
    fit: "Accommodates up to 4 full units",
    editorialQuote: "Travel with your full royal arsenal intact."
  },

  // --- SKINCARE & MAKEUP ---
  {
    id: "product-41",
    name: "UMATTR Skin Complete Radiance Ritual Set",
    categorySlug: "skincare-makeup",
    categoryName: "Skincare & Makeup",
    subcategory: "Facial Skincare Rituals",
    image: "/products/clean/product-41.png",
    curationReason: "A 7-piece botanical skincare routine delivering hydration, barrier restoration, and lasting glow.",
    shortDescription: "A 7-piece botanical skincare collection including gentle cleansers, toner mist, glow serums, rich creams, and facial oil.",
    details: [
      "Formulated with cold-pressed rosehip oil, niacinamide, and hyaluronic acid",
      "Includes Hydrating Cleanser, Aloe Mist, Glow Serum, Barrier Cream, and Night Elixir",
      "Dermatologist tested for sensitive skin and rich melanated complexions",
      "Housed in recyclable frosted amber glass with gold pumps"
    ],
    fabric: "Clean Botanical Formulations & Glass Packaging",
    fit: "Suitable for all skin types",
    editorialQuote: "Nourish your skin with clean, intentional care."
  },
  {
    id: "product-43",
    name: "UMATTR Glow Neutral Eyeshadow Palette & Mascara Set",
    categorySlug: "skincare-makeup",
    categoryName: "Skincare & Makeup",
    subcategory: "Eye Makeup",
    image: "/products/clean/product-43.png",
    curationReason: "Warm neutral tones and velvet shimmers formulated to enhance natural eye depth for speaking stages.",
    shortDescription: "A six-pan warm neutral and shimmer eyeshadow palette paired with precision liquid liner and defining mascara.",
    details: [
      "Six richly pigmented matte, satin, and metallic shimmer pans",
      "High-adhesion formula with zero fallout during long days",
      "Waterproof smudge-proof liquid eyeliner pen with felt tip",
      "Volumizing clean mascara with hourglass silicone wand"
    ],
    fabric: "Talc-Free Mineral Pigments",
    fit: "Universal flattering neutral colorway",
    editorialQuote: "Express your vision with clarity and depth."
  },
  {
    id: "product-44",
    name: "UMATTR Glow Complexion Perfection Collection",
    categorySlug: "skincare-makeup",
    categoryName: "Skincare & Makeup",
    subcategory: "Face & Complexion",
    image: "/products/clean/product-44.png",
    curationReason: "A complete face lineup creating a smooth, radiant, flash-friendly canvas for photography and stage lights.",
    shortDescription: "A complete face makeup lineup comprising illuminating primer, radiant liquid foundation, concealer, compact powder, blush, and setting spray.",
    details: [
      "Radiance-boosting hydrating primer with gold micro-pearls",
      "Buildable medium-to-full coverage liquid foundation with natural finish",
      "Micro-milled translucent setting powder that eliminates camera flashback",
      "Hydrating 16-hour makeup setting mist"
    ],
    fabric: "Infused with Squalane & Vitamin E",
    fit: "Transfer-resistant all-day wear",
    editorialQuote: "Luminous skin that looks radiant under any light."
  },
  {
    id: "product-45",
    name: "UMATTR Glow Master Brush Set & Luxury Cosmetic Bag",
    categorySlug: "skincare-makeup",
    categoryName: "Skincare & Makeup",
    subcategory: "Brushes & Beauty Tools",
    image: "/products/clean/product-45.png",
    curationReason: "Ultra-plush cruelty-free synthetic bristles engineered for streak-free blending and easy travel.",
    shortDescription: "A handcrafted 6-piece makeup brush collection with a precision blending sponge, travel brush roll, and leather cosmetic pouch.",
    details: [
      "Densely packed vegan synthetic fibers that mimic natural hair softness",
      "Solid birchwood handles with gold-toned aluminum ferrules",
      "Includes Foundation Buffer, Powder Dome, Angled Blush, and Eye Blenders",
      "Supple vegan leather roll-up case that stands upright"
    ],
    fabric: "Vegan Taklon Bristles & Vegan Leather",
    fit: "Ergonomic weighted handles",
    editorialQuote: "Flawless precision at your fingertips."
  },
  {
    id: "product-46",
    name: "UMATTR Glow Luxury Lip Wardrobe Collection",
    categorySlug: "skincare-makeup",
    categoryName: "Skincare & Makeup",
    subcategory: "Lips",
    image: "/products/clean/product-46.png",
    curationReason: "A curated spectrum of nude, warm terracotta, berry, and classic red lipsticks with non-drying hydration.",
    shortDescription: "A curated lip collection featuring satin lipsticks and liquid glosses in signature nude, rich berry, and classic red tones.",
    details: [
      "Infused with shea butter, jojoba oil, and hyaluronic filling spheres",
      "Weightless satin finish with one-swipe opaque color payoff",
      "Magnetic gold-monogram lipstick bullets that click securely",
      "Non-sticky high-shine glass glosses for plump fullness"
    ],
    fabric: "Clean Hydrating Botanical Formulas",
    fit: "Flattering across all skin undertones",
    editorialQuote: "Speak your truth with bold confidence."
  },
  {
    id: "product-53",
    name: "UMATTR Glow 18-Shade Foundation & Concealer Spectrum",
    categorySlug: "skincare-makeup",
    categoryName: "Skincare & Makeup",
    subcategory: "Foundation & Concealer",
    image: "/products/clean/product-53.png",
    curationReason: "An inclusive spectrum crafted with true undertones (golden, olive, neutral, and red) for flawless matching.",
    shortDescription: "An 18-shade complexion spectrum offering matching luminous liquid foundations and hydrating concealers from fair to deep tones.",
    details: [
      "18 meticulously calibrated shades covering warm, cool, and neutral undertones",
      "Infused with hyaluronic acid and green tea antioxidants",
      "Non-comedogenic, fragrance-free, and oil-free formulation",
      "Sweat and humidity-resistant formula for stage performance"
    ],
    fabric: "Clean Skin-Loving Complexion Formula",
    fit: "Natural luminous second-skin finish",
    editorialQuote: "True matching for every skin tone, without compromise."
  },
  {
    id: "product-55",
    name: "UMATTR Glow Lip Kit & Shade Swatch Wardrobe",
    categorySlug: "skincare-makeup",
    categoryName: "Skincare & Makeup",
    subcategory: "Lips",
    image: "/products/clean/product-55.png",
    curationReason: "A complete lip studio set with matching lip liner pencils, satin lipsticks, and nourishing lip oils.",
    shortDescription: "A luxury lip set featuring assorted satin lipsticks, lip glosses, liquid lips, and lip liners with multifaceted shades swatched across diverse skin tones.",
    details: [
      "Includes 4 waterproof lip liner pencils and 4 coordinating satin lipsticks",
      "Enriched with avocado oil and antioxidant vitamin C",
      "Precise glide with 8-hour smudge-resistant contouring",
      "Beautifully presented in a mirrored gift box"
    ],
    fabric: "Jojoba Oil & Botanical Wax Formula",
    fit: "Full-coverage comfortable wear",
    editorialQuote: "Define, enhance, and celebrate your natural smile."
  },
  {
    id: "product-56",
    name: "UMATTR Glow 9-Pan Neutral Eyeshadow Palette & Brow Suite",
    categorySlug: "skincare-makeup",
    categoryName: "Skincare & Makeup",
    subcategory: "Eye Makeup",
    image: "/products/clean/product-56.png",
    curationReason: "Golden compact featuring nine ultra-blendable warm neutrals with brow pomade and liquid liner.",
    shortDescription: "Nine-pan golden compact eyeshadow palettes featuring velvety neutral and warm shimmer tones alongside luxury mascara, brow liners, and setting powder.",
    details: [
      "Nine curated shades: 4 creamy mattes, 3 molten metallics, 2 satin pearls",
      "Micro-milled pigments for seamless one-stroke blending",
      "Dual-ended brow definer pencil with ultra-fine precision spoolie",
      "Gold mirrored compact designed for on-the-go touch-ups"
    ],
    fabric: "Mineral Pigments & Clean Binders",
    fit: "All-day crease-free formula",
    editorialQuote: "Unleash your creativity with golden clarity."
  },
  {
    id: "product-59",
    name: "UMATTR Skin Starter Routine Kit",
    categorySlug: "skincare-makeup",
    categoryName: "Skincare & Makeup",
    subcategory: "Facial Skincare Rituals",
    image: "/products/clean/product-59.png",
    curationReason: "The essential 4-step daily skincare routine for balanced, hydrated, and radiant skin.",
    shortDescription: "A complete daily skincare ritual system including cream cleanser, restorative serum, barrier cream, and botanical mask treatments.",
    details: [
      "Step 1: Gentle Cleanser (150ml) to remove impurities without stripping",
      "Step 2: Aloe Toner Mist (100ml) to balance pH and prep skin",
      "Step 3: Vitamin Glow Serum (30ml) with 10% Vitamin C and Niacinamide",
      "Step 4: Daily Moisture Barrier Cream (50ml) with ceramides and peptides"
    ],
    fabric: "Clean Vegan & Cruelty-Free Skincare",
    fit: "Daily AM/PM regimen",
    editorialQuote: "Simple, potent rituals for glowing skin."
  },
  {
    id: "product-61",
    name: "UMATTR Skin Winter Moisture Body Box",
    categorySlug: "skincare-makeup",
    categoryName: "Skincare & Makeup",
    subcategory: "Body Care",
    image: "/products/clean/product-61.png",
    curationReason: "Intensive head-to-toe body hydration combating cold weather dryness and replenishing skin lipids.",
    shortDescription: "An ultra-nourishing body hydration gift box with rich body butter, barrier body cream, restorative body oil, and soothing hand cream.",
    details: [
      "Whipped Shea & Cocoa Body Butter (200g) with warm vanilla amber aroma",
      "Restorative Golden Body Oil (100ml) with squalane and argan oil",
      "Intensive Repair Hand Cream (75ml) with colloidal oatmeal",
      "Fast-absorbing formula that leaves zero greasy residue"
    ],
    fabric: "Raw Shea, Cocoa Butter & Cold-Pressed Argan",
    fit: "Rich head-to-toe hydration",
    editorialQuote: "Indulge in velvety softness from head to toe."
  },
  {
    id: "product-62",
    name: "UMATTR Skin & Glow Travel Vanity Set",
    categorySlug: "skincare-makeup",
    categoryName: "Skincare & Makeup",
    subcategory: "Brushes & Beauty Tools",
    image: "/products/clean/product-62.png",
    curationReason: "A compact travel companion keeping all brushes, serums, and skincare bottles neatly protected on trips.",
    shortDescription: "A curated travel companion set with a structured leather vanity case, brush organizer roll, luxury makeup brushes, and travel-sized skincare essentials.",
    details: [
      "Structured zippered vegan leather case with water-resistant lining",
      "Removable brush roll organizer holding 8 brushes",
      "Includes 4 TSA-approved refillable glass pump bottles (30ml each)",
      "Compact footprint fitting effortlessly into carry-on luggage"
    ],
    fabric: "Pebbled Vegan Leather & Clear TPU",
    fit: "TSA carry-on compliant",
    editorialQuote: "Your full beauty sanctuary, wherever you land."
  },

  // --- TEA, WELLNESS & LIFESTYLE GIFTS ---
  {
    id: "product-47",
    name: "UMATTR Wellness Herbal Tea Trio & Infusion Set",
    categorySlug: "tea-wellness",
    categoryName: "Tea, Wellness & Lifestyle Gifts",
    subcategory: "Artisanal Teas",
    image: "/products/clean/product-47.png",
    curationReason: "Crafted organic herbal blends supporting digestion, calm relaxation, and daily immune strength.",
    shortDescription: "Airtight gold tea canisters with biodegradable pyramid tea bags of chamomile, ginger mint, and hibiscus wellness blends.",
    details: [
      "Includes 3 airtight gold tin canisters with 20 pyramid sachets each",
      "Blend 1: Digest Comfort (Ginger, Peppermint, Fennel)",
      "Blend 2: Evening Calm (Chamomile, Lavender, Lemon Balm)",
      "Blend 3: Radiance Hibiscus (Hibiscus, Rosehips, Elderberry)",
      "100% Organic, non-GMO, naturally caffeine-free"
    ],
    fabric: "100% Organic Whole-Leaf Botanicals",
    fit: "60 total servings in keepsake tins",
    editorialQuote: "Sip with intention. Nurture your inner peace."
  },
  {
    id: "product-48",
    name: "UMATTR Glass Teapot, Infuser & Ceramic Mug Set",
    categorySlug: "tea-wellness",
    categoryName: "Tea, Wellness & Lifestyle Gifts",
    subcategory: "Teaware & Accessories",
    image: "/products/clean/product-48.png",
    curationReason: "Hand-blown borosilicate glass teapot with gold stainless infuser and custom ceramic mugs.",
    shortDescription: "A heat-resistant glass teapot with gold stainless infuser, paired with a custom monogram ceramic mug and gold tea scoop.",
    details: [
      "600ml hand-blown heat-resistant borosilicate glass teapot",
      "Laser-etched gold stainless steel micro-mesh infuser basket",
      "Two matte ivory ceramic mugs with gold-glazed handles",
      "Dishwasher and stovetop safe (low flame)"
    ],
    fabric: "Borosilicate Glass, 304 Stainless Steel & Ceramic",
    fit: "Serves 2 to 3 cups per brew",
    editorialQuote: "Transform daily tea into a sacred mindful ritual."
  },
  {
    id: "product-49",
    name: "UMATTR Evening Ritual Tea & Lounge Experience",
    categorySlug: "tea-wellness",
    categoryName: "Tea, Wellness & Lifestyle Gifts",
    subcategory: "Tea Ritual Sets",
    image: "/products/clean/product-49.png",
    curationReason: "An intimate evening relaxation set complete with herbal tea, steeping pot, and ambiance candle.",
    shortDescription: "An intimate tea ritual set featuring custom monogram mugs, glass steeping pot, botanical sachets, and ambiance candles.",
    details: [
      "Curated for pre-bedtime winding down and mindful decompression",
      "Includes Sleep Tea blend, ceramic mugs, and lavender soy candle",
      "Gold brass tea timer and honey wooden dripper included",
      "Elegantly gift-packaged in gold-embossed box"
    ],
    fabric: "Organic Botanicals, Soy Wax & Ceramics",
    fit: "Complete relaxation kit",
    editorialQuote: "End each day in quiet stillness and gratitude."
  },
  {
    id: "product-63",
    name: "UMATTR Artisanal Herbal Loose-Leaf Tea Collection",
    categorySlug: "tea-wellness",
    categoryName: "Tea, Wellness & Lifestyle Gifts",
    subcategory: "Artisanal Teas",
    image: "/products/clean/product-63.png",
    curationReason: "A master collection of six loose-leaf botanical blends housed in airtight gold canisters.",
    shortDescription: "A master collection of loose-leaf botanical tea blends in airtight gold canisters, featuring calming chamomile, revitalizing hibiscus, and antioxidant-rich herbal infusions.",
    details: [
      "Six full-size 100g loose-leaf gold canisters",
      "Includes: Focus Green, Digest Mint, Beauty Rose, Energy Citrus, Sleep Lavender, and Calm Chamomile",
      "Ethically sourced from single-origin organic tea estates",
      "Includes precision gold measuring scoop and silicone tea coasters"
    ],
    fabric: "100% Single-Origin Organic Whole-Leaf Teas",
    fit: "Over 180 total servings",
    editorialQuote: "Pure botanicals to elevate your mind, body, and spirit."
  },
  {
    id: "product-64",
    name: "UMATTR Organic Ginger Mint Digestive Tea",
    categorySlug: "tea-wellness",
    categoryName: "Tea, Wellness & Lifestyle Gifts",
    subcategory: "Artisanal Teas",
    image: "/products/clean/product-64.png",
    curationReason: "Warming ginger root and crisp spearmint formulated to soothe digestion and revitalize the senses.",
    shortDescription: "Soothing digestive and immune-supporting loose-leaf tea blend formulated with warming ginger, invigorating mint, and citrus peel in a gold canister.",
    details: [
      "Active ingredients: Dried organic ginger root, peppermint, spearmint, lemon peel",
      "Promotes healthy digestion and reduces bloating after meals",
      "100g loose-leaf tea (approximately 35-40 cups)",
      "Zero added sugars, artificial flavorings, or preservatives"
    ],
    fabric: "100% Organic Ginger & Mint Botanicals",
    fit: "100g airtight gold tin",
    editorialQuote: "Warmth and refreshing clarity in every cup."
  },
  {
    id: "product-65",
    name: "UMATTR Restorative Sleep & Nighttime Tea",
    categorySlug: "tea-wellness",
    categoryName: "Tea, Wellness & Lifestyle Gifts",
    subcategory: "Artisanal Teas",
    image: "/products/clean/product-65.png",
    curationReason: "Tranquil blend of Egyptian chamomile, French lavender, and valerian root for deep restorative sleep.",
    shortDescription: "A tranquil bedtime botanical tea blend enriched with chamomile, lavender, and vanilla notes, paired for restorative evening relaxation.",
    details: [
      "Formulated with whole chamomile flowers, lavender buds, and passionflower",
      "Helps calm racing thoughts and prepare the nervous system for deep rest",
      "Naturally non-habit forming and caffeine-free",
      "Brew 5-7 minutes before bedtime for optimal soothing results"
    ],
    fabric: "100% Organic Nighttime Herbals",
    fit: "100g airtight gold tin",
    editorialQuote: "Let the day fade gently into sweet restorative rest."
  },
  {
    id: "product-66",
    name: "UMATTR Focus Tea & Insulated Travel Tumbler Set",
    categorySlug: "tea-wellness",
    categoryName: "Tea, Wellness & Lifestyle Gifts",
    subcategory: "Teaware & Accessories",
    image: "/products/clean/product-66.png",
    curationReason: "An energizing green tea blend paired with a sleek gold double-wall insulated travel mug.",
    shortDescription: "An energizing lemongrass and green tea blend paired with a sleek, double-walled gold insulated travel tumbler for mindful focus on the go.",
    details: [
      "16oz double-wall vacuum insulated stainless tumbler keeping drinks hot for 8 hours",
      "Includes removable built-in tea strainer basket in lid",
      "Paired with 100g Focus Tea blend (Sencha green tea, lemongrass, ginkgo biloba)",
      "Leak-proof flip lid with carry loop"
    ],
    fabric: "18/8 Food-Grade Stainless Steel & Organic Tea",
    fit: "16oz / 500ml travel size",
    editorialQuote: "Sustained mental clarity wherever your day takes you."
  },
  {
    id: "product-67",
    name: "UMATTR Connoisseur Tea Gift Box Suite",
    categorySlug: "tea-wellness",
    categoryName: "Tea, Wellness & Lifestyle Gifts",
    subcategory: "Tea Ritual Sets",
    image: "/products/clean/product-67.png",
    curationReason: "The ultimate gifting presentation for tea enthusiasts, clients, and loved ones.",
    shortDescription: "An opulent gift presentation box containing three signature loose-leaf tea canisters, fresh refill pouches, a gold mesh infuser, and custom stationery.",
    details: [
      "Rigid gold foil keepsake presentation box",
      "Three 100g signature loose-leaf tea tins plus 3 foil-sealed refill pouches",
      "Gold stainless steel ball infuser with chain and drip dish",
      "Includes personalized Lornette Daye wellness message card"
    ],
    fabric: "Organic Teas & Gold-Plated Infuser",
    fit: "Complete luxury gifting presentation",
    editorialQuote: "A gift of wellness, serenity, and mindful living."
  },
  {
    id: "product-71",
    name: "UMATTR Full Sanctuary Lifestyle Box",
    categorySlug: "tea-wellness",
    categoryName: "Tea, Wellness & Lifestyle Gifts",
    subcategory: "Lifestyle & Home",
    image: "/products/clean/product-71.png",
    curationReason: "A comprehensive home sanctuary kit with soy candles, tea service, reed diffusers, and silk pillowcases.",
    shortDescription: "A luxury home sanctuary gift box featuring artisanal scented candles, bone china tea set, botanical reed diffuser, silk pillowcase, and fine jewelry dish.",
    details: [
      "Hand-poured coconut soy candle (amber & vanilla sandalwood scent)",
      "22-Momme pure Mulberry silk standard pillowcase",
      "Botanical reed diffuser with natural rattan reeds (150ml)",
      "Gold-trimmed ceramic jewelry catchall tray with monogram"
    ],
    fabric: "Silk, Coconut Soy Wax & Fine Ceramics",
    fit: "Sanctuary lifestyle hamper",
    editorialQuote: "Transform your personal space into a sanctuary of peace."
  }
];

// 6 Approved Categories definition
const categories = [
  {
    id: "clothing-apparel",
    slug: "clothing-apparel",
    name: "Luxury Clothing & Apparel",
    tagline: "Tailored Suits, Silk Dresses & Loungewear",
    description: "Impeccably tailored suits, flowing silk midi dresses, executive trench coats, and luxury sport-luxe separates chosen for presence, poise, and purposeful living.",
    products: allProductsData.filter(p => p.categorySlug === "clothing-apparel")
  },
  {
    id: "footwear-shoes",
    slug: "footwear-shoes",
    name: "Footwear & Shoes",
    tagline: "Italian Leather Loafers, Pumps, Boots & Sneakers",
    description: "Handcrafted Italian leather loafers, architectural stiletto pumps, court sneakers, and knee-high riding boots engineered for all-day comfort and commanding confidence.",
    products: allProductsData.filter(p => p.categorySlug === "footwear-shoes")
  },
  {
    id: "bags-accessories",
    slug: "bags-accessories",
    name: "Bags, Jewelry & Accessories",
    tagline: "Structured Handbags, Luggage & 18k Gold Accents",
    description: "Artisanal structured leather handbags, weekender luggage suites, silk scarves, polarized eyewear, and 18k gold vermeil jewelry designed to finish every look with intentional polish.",
    products: allProductsData.filter(p => p.categorySlug === "bags-accessories")
  },
  {
    id: "hair-crown-care",
    slug: "hair-crown-care",
    name: "Hair & Crown Care (Wigs & Extensions)",
    tagline: "Human Hair Wigs, Extensions & Restorative Masks",
    description: "Couture virgin human hair wigs, seamless clip-in extensions, protective styling braids with gold cuffs, and botanical hair masks formulated to honor and nurture your crown.",
    products: allProductsData.filter(p => p.categorySlug === "hair-crown-care")
  },
  {
    id: "skincare-makeup",
    slug: "skincare-makeup",
    name: "Skincare & Makeup",
    tagline: "Botanical Serums, Complexion Glow & Lip Wardrobes",
    description: "Clean botanical skincare rituals, 18-shade inclusive foundation spectrums, rich lip wardrobes, and master brush sets delivering camera-ready radiance and deep hydration.",
    products: allProductsData.filter(p => p.categorySlug === "skincare-makeup")
  },
  {
    id: "tea-wellness",
    slug: "tea-wellness",
    name: "Tea, Wellness & Lifestyle Gifts",
    tagline: "Artisanal Teas, Glass Teaware & Home Sanctuary",
    description: "Organic whole-leaf teas, heat-resistant glass teaware, artisanal candles, and luxury sanctuary gift boxes crafted to inspire mindful daily pause, rest, and renewal.",
    products: allProductsData.filter(p => p.categorySlug === "tea-wellness")
  }
];

const totalProducts = categories.reduce((sum, c) => sum + c.products.length, 0);

const tsContent = `// Auto-generated curated product data with exact image-to-title visual matching
// Total Products: ${totalProducts} across 6 Brand Categories

export interface ProductItem {
  id: string;
  name: string;
  categorySlug: string;
  categoryName: string;
  subcategory: string;
  image: string;
  curationReason: string;
  shortDescription: string;
  details: string[];
  fabric?: string;
  fit?: string;
  editorialQuote?: string;
}

export interface ProductCategory {
  id: string;
  slug: string;
  name: string;
  tagline: string;
  description: string;
  products: ProductItem[];
}

export const collectionMeta = {
  title: "The Collection",
  eyebrow: "COMING SOON",
  signature: "Curated by Lornette Daye",
  heroHeading: "A Thoughtful Curation of Beauty, Wellness & Style",
  heroDescription:
    "An exclusive preview of Lornette Daye's curated essentials—spanning luxury tailoring, footwear, leather goods, crown care, skincare, and wellness teas chosen with confidence, purpose, and uncompromising quality.",
  vipNote:
    "This is a coming-soon showcase. Products are not yet available for direct purchase. Join the priority interest list below to receive private launch invitations and exclusive early access.",
  seoTitle: "The Collection | Curated by Lornette Daye (Coming Soon)",
  seoDescription:
    "Explore The Collection curated by Lornette Daye—a thoughtful coming-soon showcase of luxury clothing, footwear, handbags, wigs, skincare, and wellness teas.",
  canonicalUrl: "https://lornettedaye.com/collection",
  ogImage: "/products/clean/product-01.png",
};

export const productCategories: ProductCategory[] = ${JSON.stringify(categories, null, 2)};

export function getAllProducts(): ProductItem[] {
  return productCategories.flatMap((category) => category.products);
}

export function getProductById(id: string): ProductItem | undefined {
  return getAllProducts().find((product) => product.id === id);
}

export function getActiveCategories(): ProductCategory[] {
  return productCategories.filter((category) => category.products.length > 0);
}
`;

fs.writeFileSync("src/content/products.ts", tsContent, "utf8");
console.log(`Generated src/content/products.ts with ${totalProducts} products across ${categories.length} categories.`);
categories.forEach(c => console.log(` - ${c.name}: ${c.products.length} products`));
