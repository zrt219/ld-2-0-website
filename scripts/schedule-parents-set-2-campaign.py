# -*- coding: utf-8 -*-
import os
import sys
import json
import urllib.request
import urllib.error
import ssl
import time

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'  # Lornette Daye LinkedIn

CDN_BASE = 'https://lornettedaye.com/campaigns/parents-set-2'

posts_data = [
  {
    "id": 1,
    "slot": "Monday Morning (8:30 AM MDT)",
    "dueAt": "2026-09-28T14:30:00.000Z",
    "assetFile": "parents-2-1.png",
    "cta": "Speaking (lornettedaye.com/speaking)",
    "text": "BEFORE THE TROPHIES, THERE WAS FAMILY. 🇪🇸🎾❤️\n\nCarlos Alcaraz is already a 4-time Grand Slam champion, an Olympic silver medalist, and the youngest World No. 1 in tennis history.\n\nThe sports media loves to talk about his thunderous forehand and his supersonic court coverage. But long before Carlos was lifting the trophy at Wimbledon, his father Carlos Sr. was managing a modest tennis club in El Palmar, stretching every peseta and euro so his boy could travel to junior tournaments.\n\nIn my 40+ years coaching Olympic athletes and national champions, I have learned an undeniable truth: Talent attracts sponsors, but family builds staying power. When an athlete knows their value at home has nothing to do with whether they win or lose, they play with fearless freedom.\n\nCoaches & Parents: How do you build an environment where your young athlete feels valued for who they are, not just what they produce on the court?\n\n👉 Book Lornette Daye for keynotes and leadership workshops on parenting champions and cultivating healthy youth sports cultures: lornettedaye.com/speaking\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 2,
    "slot": "Monday Mid-day (1:00 PM MDT)",
    "dueAt": "2026-09-28T19:00:00.000Z",
    "assetFile": "parents-2-2.png",
    "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
    "text": "THE WORLD SAW CARLOS. HE SAW HIS PARENTS. 🏆👀\n\nLook at Carlos Alcaraz's eyes in this moment. The stadium is erupting, cameras are flashing, and 15,000 spectators are on their feet.\n\nYet where does his gaze immediately travel? Straight to the player box. To the mother who washed his dirty tennis socks and cooked his favorite paella. To the father who taught him how to hit a drop shot with soft hands and a calm heart.\n\nFathers and mentors: In seasons of intense career pressure and outside noise, how do you keep your sons anchored in core family values?\n\nTrue masculine leadership isn't about shouting from the sidelines. It is about steady, consistent presence that reminds a young man where his foundation lies.\n\n👉 Strengthen your emotional resilience and purposeful leadership. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 3,
    "slot": "Monday Evening (6:00 PM MDT)",
    "dueAt": "2026-09-29T00:00:00.000Z",
    "assetFile": "parents-2-1.png",
    "cta": "Speaking (lornettedaye.com/speaking)",
    "text": "WHY ALCARAZ STILL LIVES ABOVE A SHOP IN EL PALMAR. 🏠🇪🇸\n\nDo you know what Carlos Alcaraz did after winning his first US Open and reaching World No. 1 at 19 years old?\n\nHe went back home to El Palmar, Murcia, and slept in his childhood bedroom in his parents' apartment above a kebab shop. He ate breakfast at the kitchen table with his brothers, cleaned his room, and listened to his mother's advice.\n\nIn professional sports, premature independence and sudden wealth destroy more prodigies than injuries ever will. Carlos Alcaraz has dominated men's tennis because his family keeps him anchored to earth.\n\nAthletic Directors & Academy Leaders: Are you teaching your athletes how to manage fame and handle the isolation of the summit?\n\n👉 Bring Lornette Daye to your coaching conference or athletic department to train holistic champion mindsets: lornettedaye.com/speaking\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 4,
    "slot": "Tuesday Morning (8:30 AM MDT)",
    "dueAt": "2026-09-15T14:30:00.000Z",
    "assetFile": "parents-2-3.png",
    "cta": "Speaking (lornettedaye.com/speaking)",
    "text": "A CHAMPION DOESN'T RISE ALONE. COCO GAUFF & HER PARENTS. 🇺🇸✨\n\nWhen Coco Gauff collapsed onto the court in tears after winning the 2023 US Open at 19 years old, her very first instinct wasn't the trophy. It was scrambling into the stands to fall into the arms of her mother, Candi, and father, Corey.\n\nTo the casual observer, Coco is a generational tennis phenom. But to those of us who have spent four decades in Olympic sport, we know the real story:\n- Her father gave up his career as a college basketball star and executive to coach her on public park courts.\n- Her mother gave up her career as a collegiate heptathlete and educator to homeschool Coco on the road.\n- They moved their entire family into her grandparents' home in Delray Beach to fund coaching and travel.\n\nBehind every explosive serve is a family that mortgaged their comfort for a daughter's vision.\n\nCoaches & Parents: What is the biggest sacrifice you've made for your young athlete's development?\n\n👉 Empower your sports organization with Lornette Daye's keynote on youth sports leadership and family foundations: lornettedaye.com/speaking\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 5,
    "slot": "Tuesday Mid-day (1:00 PM MDT)",
    "dueAt": "2026-09-15T19:00:00.000Z",
    "assetFile": "parents-2-4.png",
    "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
    "text": "THE HARDEST THING A SPORTS PARENT WILL EVER DO: STEPPING BACK. 🎾🙏\n\nIn 2023, after years of serving as Coco Gauff's primary coach, Corey and Candi Gauff made a courageous, ego-free decision: they stepped back and brought in external coaches to lead Coco's technical team.\n\nCorey didn't fight for control. He knew that to unlock Coco's ultimate potential, she needed a specialized voice—and more importantly, she needed him to be her father first.\n\nMonths later, Coco held the US Open trophy.\n\nMothers, women mentors, and family leaders: Knowing when to hold on and when to release control is one of the highest forms of wisdom. It requires deep confidence in your identity outside of your child's accomplishments.\n\n👉 Rebuild your peace, clarity, and purpose through every season of transition. Read *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 6,
    "slot": "Tuesday Evening (6:00 PM MDT)",
    "dueAt": "2026-09-16T00:00:00.000Z",
    "assetFile": "parents-2-3.png",
    "cta": "Surviving Life Book (lornettedaye.com/books)",
    "text": "THE PRAYER IN THE PLAYER BOX: CANDI GAUFF'S QUIET STRENGTH. 🕊️❤️\n\nWatch Candi Gauff when Coco faces break point down 3-5 in the third set.\n\nWhile the stadium screams and coaches pace nervously, Candi closes her eyes and breathes. Her hands are folded. Her spirit is completely peaceful.\n\nWhy? Because she taught Coco that a tennis match is something she plays, not who she is. When an athlete knows that their mother's love is unconditional and unshakeable regardless of the scoreboard, fear loses its grip.\n\nParents: When your child is under immense pressure, do they feel your anxiety or your peace?\n\n👉 Find strength, embrace purpose, and build unshakeable hope through every trial. Read *Surviving Life* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 7,
    "slot": "Wednesday Morning (8:30 AM MDT)",
    "dueAt": "2026-09-16T14:30:00.000Z",
    "assetFile": "parents-2-5.png",
    "cta": "Speaking (lornettedaye.com/speaking)",
    "text": "HONOR THE FATHER. HONOR THE COACH. 🇺🇸🎾🤝\n\nLook at this courtside dialogue between Ben Shelton and his father, Bryan Shelton.\n\nBryan isn't just Ben's dad. He is a former ATP World Tour top-55 singles player, a mixed doubles Grand Slam finalist, and the only coach in NCAA history to win a Division I National Championship with both a women's and men's team.\n\nWhen Ben decided to turn professional, Bryan made the ultimate professional sacrifice: he resigned from his lifetime tenured head coaching position at the University of Florida to travel the globe in his son's corner.\n\nNavigating the dual role of father and coach is the most perilous high-wire act in modern athletics. Push too hard on technique, and you risk fracturing the father-son bond. Be too soft, and you handicap their competitive ceiling.\n\nAthletic Directors & Coaches: How does your program support athletes who have family members in their coaching corners?\n\n👉 Book Lornette Daye for your sports leadership summit on navigating family-coach dynamics: lornettedaye.com/speaking\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 8,
    "slot": "Wednesday Mid-day (1:00 PM MDT)",
    "dueAt": "2026-09-16T19:00:00.000Z",
    "assetFile": "parents-2-6.png",
    "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
    "text": "THE SCOREBOARD SHOWS BEN. THE STORY SHOWS TWO. 🤜🤛\n\nLook at the grip between Ben Shelton and Bryan Shelton at the player box rail. That isn't a corporate handshake. That is decades of shared discipline.\n\nNotice that Bryan never allowed Ben to travel outside the United States for junior tennis until he turned 20 years old. While other parents were flying 12-year-olds to Europe and burning them out, Bryan made Ben play high school and college tennis, stay in school, and build emotional grit.\n\nThe result? Ben arrived on the ATP tour healthy, joyful, and hungry rather than exhausted.\n\nMen and fathers: Delayed gratification is the ultimate mark of mature leadership. Playing the long game with your children always outperforms chasing short-term applause.\n\n👉 Build steadier habits, emotional resilience, and generational legacy. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 9,
    "slot": "Wednesday Evening (6:00 PM MDT)",
    "dueAt": "2026-09-17T00:00:00.000Z",
    "assetFile": "parents-2-5.png",
    "cta": "Speaking (lornettedaye.com/speaking)",
    "text": "COMMUNICATION UNDER PRESSURE: WHAT OLYMPIC COACHING TEACHES US. 🗣️⚡\n\nWhen Ben Shelton is down match point, Bryan Shelton never lectures. He gives one clear focal cue. One steady breath. One nod.\n\nIn my 40+ years coaching Olympic athletes, I tell parents: An athlete's brain during elite competition is already flooded with cortisol and sensory overload. If you shout five tactical adjustments from the stands, you paralyze them.\n\nA champion doesn't need a lecture on court. They need an emotional lighthouse.\n\nCoaches & Parents: What is the emotional tone of your sideline voice when your athlete is failing?\n\n👉 Bring Lornette Daye to your athletic department or coaching symposium to teach the high-performance psychology of communication under pressure: lornettedaye.com/speaking\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 10,
    "slot": "Thursday Morning (8:30 AM MDT)",
    "dueAt": "2026-09-17T14:30:00.000Z",
    "assetFile": "parents-2-7.png",
    "cta": "Speaking (lornettedaye.com/speaking)",
    "text": "HER MOTHER HELPED CARRY THE DREAM: NAOMI & TAMAKI OSAKA. 🇯🇵🗽❤️\n\nThe world knows Naomi Osaka as a 4-time Grand Slam champion and the global face of modern tennis.\n\nBut long before the multimillion-dollar endorsements, there was a woman named Tamaki Osaka. Growing up in Nemuro, Hokkaido, Tamaki defied societal norms to build a family with Leonard Francois. When they moved to Long Island, New York, they had no sponsor, no academy backing, and no tennis connections.\n\nWhile Leonard took Naomi and Mari to public courts with second-hand tennis balls, Tamaki worked grueling 16-hour night shifts in offices and retail. She left before sunrise and returned long after dark, paying for court fees, tournament registrations, and cheap motels.\n\nShe didn't see the training sessions. She funded them with her sleep.\n\nMothers & Mentors: How often do we forget to honor the parent whose sacrifice is completely silent?\n\n👉 Book Lornette Daye for keynotes on the untold resilience of sporting families and women in leadership: lornettedaye.com/speaking\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 11,
    "slot": "Thursday Mid-day (1:00 PM MDT)",
    "dueAt": "2026-09-17T19:00:00.000Z",
    "assetFile": "parents-2-8.png",
    "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
    "text": "SHE WORKED SO HER DAUGHTERS COULD DREAM. 🕊️✍️\n\nLook closely at this image. A mother working late into the night at her desk while her young daughters sleep with a tennis racket by their pillow.\n\nThat was Tamaki Osaka. She never complained. She never demanded public credit. She absorbed the financial terror, the exhaustion, and the uncertainty so her girls could walk onto court with clean shoes and belief in their hearts.\n\nWomen leaders, mothers, and caregivers: How often do you carry the emotional weight of your entire family while pushing your own needs into the background?\n\nCarrying others requires you to have an internal reservoir of grace and emotional strength.\n\n👉 Restore your confidence, protect your inner peace, and thrive through heavy seasons. Read *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 12,
    "slot": "Thursday Evening (6:00 PM MDT)",
    "dueAt": "2026-09-18T00:00:00.000Z",
    "assetFile": "parents-2-7.png",
    "cta": "Surviving Life Book (lornettedaye.com/books)",
    "text": "WHEN THE WORLD PRESSES IN: TAMAKI OSAKA AS NAOMI'S SANCTUARY. 🛡️🌸\n\nWhen Naomi Osaka stepped away from Roland Garros in 2021 to prioritize her mental health, the international media ignited a firestorm of criticism.\n\nIn that storm, Tamaki Osaka didn't ask Naomi about ranking points or sponsor contracts. She welcomed her daughter into her home, cooked her favorite Japanese meals, and reminded her of who she was before the world gave her a title.\n\nThat is the true role of a parent in elite sport: To be the shelter where the warrior can take off their armor.\n\nParents & Mentors: Is your home a second arena of pressure, or a sanctuary of renewal?\n\n👉 Rebuild hope, confidence, and peace after grueling seasons of burnout. Read *Surviving Life* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 13,
    "slot": "Friday Morning (8:30 AM MDT)",
    "dueAt": "2026-09-18T14:30:00.000Z",
    "assetFile": "parents-2-9.png",
    "cta": "Speaking (lornettedaye.com/speaking)",
    "text": "HE TAUGHT HIM TO FLY. MONDO DUPLANTIS & HIS FATHER GREG. 🇸🇪🚀\n\nArmand \"Mondo\" Duplantis is the greatest pole vaulter the world has ever seen. He has broken the World Record 10+ times, soaring over 6.30m into the sky.\n\nWho is the man standing at the end of the runway? Greg Duplantis—an elite American vaulter himself (5.80m personal best) and Mondo's lifelong coach.\n\nGreg understands the biomechanics of takeoff speed, plant angles, and energy transfer. But his greatest genius as a father wasn't his physics knowledge. It was his patience. Greg never forced Mondo to vault; he made it so irresistible that Mondo couldn't stay away.\n\nIn four decades of Olympic coaching, I have watched hundreds of talented kids quit sports because their parents pushed with fear instead of passion.\n\nCoaches & Parents: How do you transfer technical excellence without killing the child's innate joy?\n\n👉 Book Lornette Daye for your sports leadership seminar on nurturing generational talent: lornettedaye.com/speaking\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 14,
    "slot": "Friday Mid-day (1:00 PM MDT)",
    "dueAt": "2026-09-18T19:00:00.000Z",
    "assetFile": "parents-2-10.png",
    "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
    "text": "LONG BEFORE THE RECORDS, THERE WAS A FATHER IN THE BACKYARD. 🏡🌱\n\nWhen Mondo was 4 years old, Greg Duplantis built a full-length pole vault pit in the backyard of their Lafayette, Louisiana home.\n\nMondo didn't practice in a sterile, high-pressure Olympic training center. He vaulted in his socks after school. He vaulted with his brothers. He vaulted while his mother Helena cooked dinner. It was play, not punishment.\n\nBy the time Mondo competed on the world stage, the pole vault was as natural to him as walking.\n\nAthletes: When you compete, do you carry the burden of expectation or the freedom of child-like joy?\n\n👉 Master the mental discipline and inner focus of elite performers. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 15,
    "slot": "Friday Evening (6:00 PM MDT)",
    "dueAt": "2026-09-19T00:00:00.000Z",
    "assetFile": "parents-2-9.png",
    "cta": "Speaking (lornettedaye.com/speaking)",
    "text": "THE CHEMISTRY OF A PARENT-COACH WHO KNOWS WHEN TO SHUT UP. 🤫👑\n\nHave you watched Greg Duplantis coach Mondo during a World Championship?\n\nWhen Mondo misses a height at 6.15m, Greg doesn't wave his arms. He doesn't scowl. He walks to the barrier, speaks three sentences, and steps back. He trusts the preparation.\n\nOver-coaching during competition is the #1 sign of parental anxiety. Elite coaching is about emotional restraint.\n\nAthletic Directors & Youth Coaches: Are your coaches empowering athletes to solve problems in real-time, or micromanaging them into dependency?\n\n👉 Keynote Lornette Daye for your coaching symposium on Olympic communication and athletic autonomy: lornettedaye.com/speaking\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 16,
    "slot": "Saturday Morning (8:30 AM MDT)",
    "dueAt": "2026-09-19T14:30:00.000Z",
    "assetFile": "parents-2-2.png",
    "cta": "Finish Strong Book (lornettedaye.com/books)",
    "text": "THE BOY WHO NEVER FORGOT HIS HOMETOWN: CARLOS ALCARAZ. 🇪🇸🎾\n\nIn the modern era of professional sports, early stardom often creates an unbridgeable gap between the athlete and reality. Private jets, VIP entourages, and multi-million dollar deals isolate young stars from the values that made them great.\n\nCarlos Alcaraz is the antidote.\n\nHis mother Virginia and father Carlos Sr. instilled a simple rule from his first junior tournament: \"Win or lose, you shake hands, look people in the eye, and remember you are a boy from El Palmar.\"\n\nThat groundedness is why Carlos smiles through 5-hour slugfests. He knows tennis is his passion, but family is his identity.\n\nAthletes & Leaders: Are you anchored deep enough to survive the storm of your own success?\n\n👉 Build an elite mindset rooted in resilience, perseverance, and legacy. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 17,
    "slot": "Saturday Mid-day (1:00 PM MDT)",
    "dueAt": "2026-09-19T19:00:00.000Z",
    "assetFile": "parents-2-1.png",
    "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
    "text": "VIRGINIA GARFIA: THE MOTHER WHO PROTECTED THE PERSON OVER THE PRODIGY. 🌸🇪🇸\n\nBehind Carlos Alcaraz's explosive athleticism is the quiet, protective heart of his mother, Virginia.\n\nWhile scouts and agents circled Carlos when he was 14, Virginia refused to let him become a corporate commodity. She insisted he finish his schooling, spend time with his grandparents, and maintain normal teenage friendships.\n\nIn youth athletics, the greatest gift a mother can give a prodigy is the courage to say NO to premature exploitation.\n\nMothers, women leaders, and mentors: Protecting those you love requires fierce discernment and quiet courage.\n\n👉 Rebuild your foundation and thrive with meaning through seasons of intense demand. Read *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 18,
    "slot": "Saturday Evening (6:00 PM MDT)",
    "dueAt": "2026-09-20T00:00:00.000Z",
    "assetFile": "parents-2-2.png",
    "cta": "Speaking (lornettedaye.com/speaking)",
    "text": "WHEN PRESSURE MOUNTS, WHERE DO YOUR ATHLETES LOOK? 👀🏟️\n\nWatch Carlos Alcaraz when he is trailing two sets to one in a Grand Slam final.\n\nHe doesn't panic. He turns toward his box, looks at his father and coach, pumps his fist, and cracks a smile. That box is his psychological oxygen tank.\n\nIn my 40+ years coaching Olympic athletes, I tell sporting directors: You cannot build mental toughness with cruelty or humiliation. Mental toughness is forged when an athlete knows their corner has their back no matter how ugly the match gets.\n\nAthletic Directors & Coaches: What culture are you creating in your team's corner?\n\n👉 Bring Lornette Daye to your coaching summit to transform your team's sideline culture: lornettedaye.com/speaking\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 19,
    "slot": "Sunday Morning (8:30 AM MDT)",
    "dueAt": "2026-09-20T14:30:00.000Z",
    "assetFile": "parents-2-4.png",
    "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
    "text": "THE UNSEEN MILES: COREY GAUFF'S SACRIFICE. 🚗🎾\n\nBefore Coco Gauff was flying first class to Wimbledon, Corey Gauff was driving thousands of miles along Interstate 95 in an old family van packed with racquets, coolers, and textbooks.\n\nCorey wasn't guaranteed that Coco would become a Grand Slam champion. There are tens of thousands of junior players whose families make identical sacrifices and never break into the top 500.\n\nSacrifice in youth sports isn't a business transaction; it is an act of deep, sacrificial love.\n\nFathers and male mentors: When you invest in the next generation, do you demand a guaranteed return, or do you pour yourself out because it is your duty?\n\n👉 Clarify your purpose, master pressure, and lead your family with conviction. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 20,
    "slot": "Sunday Mid-day (1:00 PM MDT)",
    "dueAt": "2026-09-20T19:00:00.000Z",
    "assetFile": "parents-2-3.png",
    "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
    "text": "BEHIND EVERY POISED YOUNG WOMAN IS A MOTHER WHO TAUGHT HER WORTH. 👑❤️\n\nLook at Coco Gauff's poise when addressing controversy, handling tough press conferences, or standing up for social justice. She speaks with a clarity that defies her youth.\n\nThat poise wasn't learned from media trainers. It was absorbed from Candi Gauff at the dinner table.\n\nCandi taught Coco that she didn't need a trophy to prove her dignity. When a young woman knows she is fundamentally worthy, she does not shrink in front of kings, critics, or opponents.\n\nWomen and mothers: The lessons you model in private become the armor your children wear in public.\n\n👉 Cultivate unshakeable dignity and purposeful resilience. Read *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 21,
    "slot": "Sunday Evening (6:00 PM MDT)",
    "dueAt": "2026-09-21T00:00:00.000Z",
    "assetFile": "parents-2-4.png",
    "cta": "Speaking (lornettedaye.com/speaking)",
    "text": "WHEN THE DREAM COMES TRUE, WHO STANDS BESIDE YOU? 🏆👨‍👩‍👧\n\nThe image of Coco Gauff hugging her parents after winning the US Open will live in sports history forever.\n\nBecause in that single embrace was the redemption of every 5:00 AM alarm, every missed family vacation, every financial gamble, and every prayer whispered in the bleachers.\n\nAs an Olympic coach, I remind parents and coaches: The journey is the destination. If you destroy your relationship with your child on the way to the trophy, the victory will taste like ash.\n\nParents & Athletic Leaders: How are you ensuring your family relationships survive the athletic grind?\n\n👉 Book Lornette Daye for keynotes and workshops on raising champions with intact hearts: lornettedaye.com/speaking\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 22,
    "slot": "Monday Morning (8:30 AM MDT)",
    "dueAt": "2026-09-21T14:30:00.000Z",
    "assetFile": "parents-2-6.png",
    "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
    "text": "TWO GENERATIONS OF MEN. ONE SHARED LEGACY. 🇺🇸🎾🤝\n\nBryan Shelton played on the ATP tour in the 1990s. He fought through the brutal realities of professional tennis as a Black man in a predominantly white sport.\n\nWhen he coached his son Ben, he didn't just teach him how to strike a 149 mph serve. He taught him how to carry himself with joy, self-respect, and unshakeable confidence in rooms where people might doubt him.\n\nGenerational legacy isn't about passing down financial assets. It is about passing down emotional strength, discipline, and moral courage.\n\nFathers & Mentors: What principles are you actively passing down to the young men who look up to you?\n\n👉 Build purpose, mental balance, and generational fortitude. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 23,
    "slot": "Monday Mid-day (1:00 PM MDT)",
    "dueAt": "2026-09-21T19:00:00.000Z",
    "assetFile": "parents-2-5.png",
    "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
    "text": "WHY COLLEGE SPORTS WAS BEN SHELTON'S SECRET WEAPON. 🐊🎾\n\nMost tennis prodigies turn pro at 16, skip college, and miss out on team culture.\n\nBryan Shelton refused to let Ben do that. He brought Ben to the University of Florida. Ben had to share locker rooms, compete for his teammates, sit through classes, and learn accountability.\n\nWhen Ben won the NCAA singles championship and later reached the US Open semifinals at 20, he had the emotional maturity of a 28-year-old veteran.\n\nAthletes & Competitors: Are you rushing into individual glory at the expense of your character development?\n\n👉 Build the mental poise, team-first discipline, and champion mindset of elite athletes. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 24,
    "slot": "Monday Evening (6:00 PM MDT)",
    "dueAt": "2026-09-22T00:00:00.000Z",
    "assetFile": "parents-2-6.png",
    "cta": "Speaking (lornettedaye.com/speaking)",
    "text": "HOW TO CRITIQUE YOUR CHILD WITHOUT BREAKING THEIR SPIRIT. 🎯💬\n\nEvery sports parent knows the hardest car ride is the one after a heartbreaking loss.\n\nWhat do you say when your athlete just double-faulted away the match?\n- If you attack their mistakes, they associate your love with winning.\n- If you make excuses for them, you rob them of accountability.\n\nBryan Shelton mastered the art of the 24-hour rule: Let emotions settle, buy ice cream, be dad first. Review the technical film tomorrow.\n\nCoaches & Parents: What is your protocol for the post-game car ride?\n\n👉 Book Lornette Daye for your sports academy or school board keynote on youth athletic emotional intelligence: lornettedaye.com/speaking\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 25,
    "slot": "Tuesday Morning (8:30 AM MDT)",
    "dueAt": "2026-09-22T14:30:00.000Z",
    "assetFile": "parents-2-8.png",
    "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
    "text": "THE FINANCIAL GAMBLE OF JUNIOR TENNIS: TAMAKI OSAKA'S STEEL. 🎾💼\n\nLet's be completely honest about junior sports: Elite tennis is outrageously expensive. Between coaching, travel, equipment, and court time, families spend upwards of $50,000 to $100,000 annually.\n\nTamaki Osaka and Leonard Francois didn't have that kind of money. Not even close.\n\nTamaki worked second jobs, skipped holidays, and balanced household books down to the last dollar. She absorbed the terror of financial precarity so Naomi and Mari could hold their heads high on court.\n\nTo every mother currently stretching her budget so her child can chase an improbable dream: You are the unsung hero of sport.\n\n👉 Renew your inner strength, navigate pressure, and build steadier hope. Read *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 26,
    "slot": "Tuesday Mid-day (1:00 PM MDT)",
    "dueAt": "2026-09-22T19:00:00.000Z",
    "assetFile": "parents-2-7.png",
    "cta": "Surviving Life Book (lornettedaye.com/books)",
    "text": "WHEN THE APPLAUSE FADES: BEING AN UNCONDITIONAL HAVEN. 🌸🤍\n\nIn 2021, when Naomi Osaka withdrew from major tournaments to address depression and anxiety, the public discourse was brutal. Commentators accused her of being \"unprofessional.\"\n\nDo you know what Tamaki Osaka did? She opened the front door, wrapped Naomi in a blanket, and told her she loved her.\n\nThe commercial sports machine views athletes as entertainment assets. When they produce, they are celebrated. When they break, they are discarded.\n\nOnly a parent's love remains constant when the lights go out.\n\nParents: When your athlete encounters personal failure or emotional burnout, do they run toward you or away from you?\n\n👉 Find strength and renewal through life's hardest chapters. Read *Surviving Life* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 27,
    "slot": "Tuesday Evening (6:00 PM MDT)",
    "dueAt": "2026-09-23T00:00:00.000Z",
    "assetFile": "parents-2-8.png",
    "cta": "Speaking (lornettedaye.com/speaking)",
    "text": "MOTHERHOOD, RACE & RESILIENCE: THE TAMAKI OSAKA BLUEPRINT. 🇯🇵🗽\n\nRaising multicultural, biracial daughters in international tennis required Tamaki Osaka to navigate cultural misunderstandings, language barriers, and intense scrutiny.\n\nShe taught Naomi and Mari how to honor their Japanese heritage, their Haitian roots, and their American upbringing simultaneously. She gave them identity pride before the world could label them.\n\nIn my 40+ years coaching Olympic athletes, identity clarity is the greatest predictor of psychological endurance. When an athlete knows who they are, hostile environments cannot intimidate them.\n\nCollegiate Coaches & Athletic Leaders: How are you cultivating identity resilience in your student-athletes?\n\n👉 Keynote Lornette Daye for your university or sports organization on cultural resilience and student-athlete identity: lornettedaye.com/speaking\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 28,
    "slot": "Wednesday Morning (8:30 AM MDT)",
    "dueAt": "2026-09-23T14:30:00.000Z",
    "assetFile": "parents-2-10.png",
    "cta": "Speaking (lornettedaye.com/speaking)",
    "text": "WHY MONDO DUPLANTIS STILL CALLS HIS DAD HIS CHIEF COACH. 🇸🇪🥇\n\nArmand Duplantis has achieved everything an athlete could ever dream of: Olympic Gold, World Championships, European titles, and 10+ World Records.\n\nHe could hire any coach in Europe or America. Yet in his corner at every major championship stands his father, Greg, and his mother, Helena (who manages his strength & conditioning).\n\nWhy? Because Greg understands Mondo's nervous system better than any high-tech sports science lab. He knows the exact rhythm of Mondo's run-up, the subtle signs of fatigue, and when to tell him to pack up the poles and go get a burger.\n\nTrust between an athlete and coach takes 15 years to build and 15 seconds to destroy.\n\nAthletic Directors & Coaches: How do you protect long-term trust in high-stakes coaching relationships?\n\n👉 Bring Lornette Daye to your coaching symposium to master the art of long-term athlete development: lornettedaye.com/speaking\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 29,
    "slot": "Wednesday Mid-day (1:00 PM MDT)",
    "dueAt": "2026-09-23T19:00:00.000Z",
    "assetFile": "parents-2-9.png",
    "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
    "text": "OVERCOMING FEAR: HOW TO FLY 20 FEET IN THE AIR. 🚀⚡\n\nPole vaulting is arguably the most terrifying event in track and field. You sprint full speed with a 17-foot fiberglass pole, plant it into an 8-inch box, and launch your body upside down over a two-story crossbar.\n\nOne split second of hesitation can cause catastrophic injury.\n\nHow did Greg Duplantis train Mondo to be fearless? By never using fear as a coaching tool. When Mondo fell as a kid in their backyard pit, Greg laughed with him, picked him up, and analyzed what happened without anger.\n\nFearlessness is not the absence of danger; it is the presence of unconditional trust.\n\nCompetitors & Athletes: When you face your biggest obstacle, do you tense up or trust your training?\n\n👉 Build unshakeable mental poise and competitive courage. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 30,
    "slot": "Wednesday Evening (6:00 PM MDT)",
    "dueAt": "2026-09-24T00:00:00.000Z",
    "assetFile": "parents-2-10.png",
    "cta": "Finish Strong Book (lornettedaye.com/books)",
    "text": "THE LEGACY OF A BACKYARD: WHERE GENERATIONS MEET. 🏡🌟\n\nThink about that backyard in Lafayette, Louisiana.\n\nLong before sold-out stadiums in Paris and Tokyo were chanting Mondo's name, there was just a dad with a hammer and nails building wooden box covers, cutting foam mats, and measuring jump heights with a wooden stick.\n\nBig dreams don't require billion-dollar facilities. They require dedicated parents who show up every single day and say: \"Let's try it one more time.\"\n\nTo every parent building a makeshift batting cage in the garage or painting lines on the driveway: Keep building. You are making history.\n\n👉 Unleash your inner champion and finish your race with purpose. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 31,
    "slot": "Thursday Morning (8:30 AM MDT)",
    "dueAt": "2026-09-24T14:30:00.000Z",
    "assetFile": "parents-2-1.png",
    "cta": "Speaking (lornettedaye.com/speaking)",
    "text": "THE GENERATION OF GRACE: CARLOS ALCARAZ & COCO GAUFF. 👑🇪🇸🇺🇸\n\nLook at the two young icons carrying international tennis into the next decade: Carlos Alcaraz and Coco Gauff.\n\nBoth are fierce, explosive competitors. Both have won Grand Slams as teenagers. But what stands out most about them?\n- Their infectious smiles.\n- Their respect for ball kids, officials, and opponents.\n- Their absolute humility off the court.\n\nWhy? Because both were raised in close-knit, highly engaged family units that prioritized character over trophies.\n\nIn an era of sports entitlement, character is the ultimate competitive moat.\n\nSchool Leaders & Athletic Directors: Are your programs graduating good athletes or great human beings?\n\n👉 Keynote Lornette Daye for your educational institution on building holistic student-athlete excellence: lornettedaye.com/speaking\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 32,
    "slot": "Thursday Mid-day (1:00 PM MDT)",
    "dueAt": "2026-09-24T19:00:00.000Z",
    "assetFile": "parents-2-4.png",
    "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
    "text": "MULTI-SPORT ATHLETES VS. EARLY SPECIALIZATION: THE TRUTH. 🏃‍♂️🎾\n\nDid you know Coco Gauff ran track and played basketball before focusing on tennis? Did you know Carlos Alcaraz played soccer and loved multiple sports as a child?\n\nTheir parents resisted the modern myth of early sports specialization. They allowed their children's bodies to develop diverse movement patterns, coordination, and mental stamina.\n\nWhen you force an 8-year-old into 20 hours a week of a single sport, you guarantee two things: chronic overuse injuries by 16, and psychological burnout by 18.\n\nAthletes & Parents: How are you protecting your physical longevity and passion for sport?\n\n👉 Build sustainable discipline, injury resilience, and mental toughness. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 33,
    "slot": "Thursday Evening (6:00 PM MDT)",
    "dueAt": "2026-09-25T00:00:00.000Z",
    "assetFile": "parents-2-2.png",
    "cta": "Surviving Life Book (lornettedaye.com/books)",
    "text": "DO THE DISHES: THE BEST PARENTAL ADVICE FOR A PHENOM. 🍽️🏆\n\nWhen Carlos Alcaraz returned home after winning his first ATP title, his mother Virginia handed him a dish towel and told him to dry the dishes.\n\nIt wasn't disrespect. It was profound parental wisdom.\n\nWhen the entire world tells a teenager they are a superstar, their nervous system begins to disconnect from reality. The best thing a parent can do is treat them completely normally at home.\n\nParents: What daily rituals in your household keep your children anchored in humility?\n\n👉 Navigate life's sudden transitions and pressures with calm, steady perspective. Read *Surviving Life* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 34,
    "slot": "Friday Morning (8:30 AM MDT)",
    "dueAt": "2026-09-25T14:30:00.000Z",
    "assetFile": "parents-2-5.png",
    "cta": "Speaking (lornettedaye.com/speaking)",
    "text": "DIVERSE JOURNEYS, SHARED COURAGE: SHELTON & OSAKA. 🎾🌍\n\nConsider the journeys of Ben Shelton and Naomi Osaka.\n\nBoth navigated elite tennis as minority competitors breaking into spaces with deep historical barriers. In both cases, their parents acted not just as coaches and drivers, but as cultural shields.\n\nBryan Shelton taught Ben how to walk into elite tennis clubs with pride, professionalism, and joy. Tamaki Osaka and Leonard Francois taught Naomi how to embrace her mixed heritage and speak her truth without fear.\n\nWhen parents teach their children to stand tall in their identity, the world's criticism cannot shake them.\n\nAthletic Directors & Diversity Leaders: How is your athletic department supporting minority athletes in non-traditional sports?\n\n👉 Book Lornette Daye for keynotes on inclusive leadership and athletic resilience: lornettedaye.com/speaking\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 35,
    "slot": "Friday Mid-day (1:00 PM MDT)",
    "dueAt": "2026-09-25T19:00:00.000Z",
    "assetFile": "parents-2-7.png",
    "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
    "text": "HOW FATHERS CAN PROTECT THEIR DAUGHTERS' MENTAL HEALTH. 🛡️🌸\n\nLeonard Francois's role in Naomi Osaka's career is often overlooked because he deliberately stayed out of the public spotlight.\n\nWhen Naomi faced intense pressure at Grand Slams, Leonard would walk the tournament grounds with headphones on, unable to bear watching her in pain. He was her gentle protector who reminded her that her worth was never on the scoreboard.\n\nFathers: Your daughters don't need you to be their loudest critic. They need you to be their safest harbor.\n\n👉 Strengthen emotional balance, family leadership, and protective care. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 36,
    "slot": "Friday Evening (6:00 PM MDT)",
    "dueAt": "2026-09-26T00:00:00.000Z",
    "assetFile": "parents-2-6.png",
    "cta": "Finish Strong Book (lornettedaye.com/books)",
    "text": "THE LONG GAME: SACRIFICING SHORT-TERM APPLAUSE FOR LONGEVITY. ⏳🏆\n\nIf you look at the greatest sports parents in history—Bryan Shelton, Tamaki Osaka, Corey Gauff, Greg Duplantis, Carlos Sr.—they all shared one common trait:\n\nThey were willing to look foolish in the short term to win in the long term.\n\nThey didn't chase meaningless U-12 rankings. They didn't overplay injured kids for cheap trophies. They focused on fundamentals, emotional balance, and character.\n\nCoaches & Parents: Are you building an athlete for next week's tournament, or for a healthy, fulfilling life?\n\n👉 Finish your race with endurance, purpose, and lasting impact. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 37,
    "slot": "Saturday Morning (8:30 AM MDT)",
    "dueAt": "2026-09-26T14:30:00.000Z",
    "assetFile": "parents-2-9.png",
    "cta": "Speaking (lornettedaye.com/speaking)",
    "text": "JOY IS THE HIGHEST FORM OF DISCIPLINE. 🇸🇪🇪🇸✨\n\nLook at Mondo Duplantis before he jumps 6.30m. Look at Carlos Alcaraz before he serves on match point at Roland Garros.\n\nNeither looks miserable. Neither looks terrified. They are smiling.\n\nIn 40+ years coaching Olympic athletes, I have found that grim, joyless discipline always breaks down under extreme pressure. But when an athlete truly LOVES the battle, pressure becomes a playground.\n\nThat joy was protected by their parents. Greg Duplantis and Carlos Sr. never allowed sports to become an emotional prison.\n\nCoaches: How do you cultivate intense athletic rigor while keeping joy alive?\n\n👉 Keynote Lornette Daye for your sports leadership seminar on unlocking joy-based high performance: lornettedaye.com/speaking\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 38,
    "slot": "Saturday Mid-day (1:00 PM MDT)",
    "dueAt": "2026-09-26T19:00:00.000Z",
    "assetFile": "parents-2-10.png",
    "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
    "text": "A FATHER'S CALMNESS IS A SON'S SUPERPOWER. 🧘‍♂️⚡\n\nWhen a young man is on the verge of greatness, he mirrors his father's nervous system.\n\nIf the father is frantic, anxious, and shouting from the sidelines, the son's muscles tighten and his decision-making freezes. But when the father stands calm, rooted, and poised, the son absorbs that calm into his bones.\n\nGreg Duplantis and Carlos Alcaraz Sr. are masters of emotional composure.\n\nFathers and mentors: Your presence speaks louder than your words. When you master your own emotions, you liberate your children to master theirs.\n\n👉 Develop steady inner discipline and grounded masculine presence. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 39,
    "slot": "Saturday Evening (6:00 PM MDT)",
    "dueAt": "2026-09-27T00:00:00.000Z",
    "assetFile": "parents-2-2.png",
    "cta": "Surviving Life Book (lornettedaye.com/books)",
    "text": "WHO YOU ARE VS. WHAT YOU DO: THE ULTIMATE PARENTAL LESSON. 🌿❤️\n\nAt some point, the cheering stops.\nAt some point, the knees give out, the records are broken, and the stadium lights go dark.\n\nWhat remains when an athletic career ends?\n\nOnly your character, your faith, and the people who love you for who you are. The greatest gift Carlos Alcaraz, Coco Gauff, Ben Shelton, Naomi Osaka, and Mondo Duplantis received from their parents wasn't athletic coaching.\n\nIt was the unwavering truth: \"You are our child first. Everything else is just a game.\"\n\nParents: Are you preparing your child for the end of sport?\n\n👉 Find lasting meaning, rebuild hope, and ground your identity in purpose. Read *Surviving Life* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 40,
    "slot": "Sunday Morning (8:30 AM MDT)",
    "dueAt": "2026-09-27T14:30:00.000Z",
    "assetFile": "parents-2-8.png",
    "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
    "text": "TO EVERY MOTHER ON THE SIDELINES: THIS IS YOUR TRIBUTE. 💐❤️\n\nTo the mothers packing water bottles at 5:30 AM.\nTo the mothers sitting on hard metal bleachers in freezing rain.\nTo the mothers washing grass-stained uniforms at midnight while their family sleeps.\nTo the mothers who hold their child's hand through tears after an unfair loss.\n\nYou will never get a championship ring. Your name will never appear in a newspaper headline. But without you, there is no champion.\n\nTamaki Osaka, Candi Gauff, Virginia Garfia, and Helena Duplantis represent millions of unsung mothers who pour out their lives in silence.\n\nWe see you. We honor you. You are the foundation of greatness.\n\n👉 Restore your soul, protect your peace, and thrive with deep purpose. Read *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 41,
    "slot": "Sunday Mid-day (1:00 PM MDT)",
    "dueAt": "2026-09-27T19:00:00.000Z",
    "assetFile": "parents-2-4.png",
    "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
    "text": "TO EVERY FATHER WHO BELIEVED FIRST: WE SALUTE YOU. 🤝🏆\n\nTo the fathers who built makeshift pitching mounds in the backyard.\nTo the fathers who drove 6 hours on a Friday night after working a 50-hour week.\nTo the fathers who swallowed their own fears so their children felt unstoppable.\nTo the fathers who taught their sons and daughters to win with humility and lose with dignity.\n\nBryan Shelton, Corey Gauff, Greg Duplantis, Carlos Alcaraz Sr., and Leonard Francois proved that a father's faithful presence can change the trajectory of an entire life.\n\nFathers: Never underestimate the power of your belief in your child's eyes.\n\n👉 Lead your home with integrity, strength, and quiet fortitude. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  },
  {
    "id": 42,
    "slot": "Sunday Evening Grand Finale (6:00 PM MDT)",
    "dueAt": "2026-09-28T00:00:00.000Z",
    "assetFile": "parents-2-6.png",
    "cta": "Speaking (lornettedaye.com/speaking)",
    "text": "GRAND FINALE: THE TROPHY BELONGS TO THE FAMILY. 🏆👨‍👩‍👧‍👦🌟\n\nAs our 2-week campaign celebrating the parents behind the world's greatest champions comes to a close, remember this:\n\nIn my 40+ years coaching Olympic athletes and national champions, medals tarnish and trophies collect dust in school display cases. But the character forged in a young athlete through the sacrificial love of their parents will echo for generations.\n\nBehind Carlos Alcaraz, Coco Gauff, Ben Shelton, Naomi Osaka, and Mondo Duplantis were ordinary parents who made extraordinary commitments.\n\nTo athletic directors, coaches, and sports executives: If you want to build enduring athletic dynasties, you must partner with, support, and honor the families behind your athletes.\n\n👉 Bring Olympian coach Lornette Daye to your university, athletic conference, or corporate keynote to inspire your leaders: lornettedaye.com/speaking\n\n👉 Explore Lornette's complete library of books for athletes, leaders, and families: lornettedaye.com/books\n\n#BehindTheChampion #YouthSports #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #SportsParenting #HighPerformance #AthleticDirector #CoachingExcellence #OlympicMindset #LornetteDaye #FamilyFoundation #RaisingChampions"
  }
]

# Fix CDN_BASE in posts_data
for p in posts_data:
    p["assetUrl"] = f"{CDN_BASE}/{p['assetFile']}"

def schedule_post(post):
    query = '''
    mutation CreatePost($input: CreatePostInput!) {
        createPost(input: $input) {
            __typename
            ... on PostActionSuccess {
                post {
                    id
                    status
                    dueAt
                }
            }
            ... on LimitReachedError {
                message
            }
            ... on InvalidInputError {
                message
            }
            ... on UnexpectedError {
                message
            }
            ... on UnauthorizedError {
                message
            }
        }
    }
    '''

    variables = {
        "input": {
            "channelId": CHANNEL_ID,
            "text": post["text"],
            "schedulingType": "automatic",
            "mode": "customScheduled",
            "dueAt": post["dueAt"],
            "saveToDraft": False,
            "needsApproval": False,
            "assets": [
                {
                    "image": {
                        "url": post["assetUrl"]
                    }
                }
            ]
        }
    }

    data = json.dumps({"query": query, "variables": variables}).encode('utf-8')
    req = urllib.request.Request(
        'https://api.buffer.com',
        data=data,
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {TOKEN}',
            'User-Agent': 'Mozilla/5.0'
        }
    )

    ctx = ssl._create_unverified_context()
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            body = json.loads(resp.read().decode('utf-8'))
            return body
    except urllib.error.HTTPError as e:
        retry_after = e.headers.get('Retry-After')
        return {
            "error": str(e),
            "status_code": e.code,
            "retry_after": int(retry_after) if retry_after and retry_after.isdigit() else 60
        }
    except Exception as e:
        return {"error": str(e)}

def main():
    print("Starting Buffer queue scheduling for Behind the Champion (Parents Set 2)...")
    print(f"Total Posts to Schedule: {len(posts_data)}")
    print(f"Channel: {CHANNEL_ID}")
    print(f"Token: {TOKEN[:6]}...{TOKEN[-4:]}")
    print("-" * 60)

    report_path = os.path.join(os.path.dirname(__file__), "parents-set-2-scheduled-report.json")
    results = {}
    if os.path.exists(report_path):
        try:
            with open(report_path, "r", encoding="utf-8") as f:
                existing_report = json.load(f)
                for item in existing_report.get("results", []):
                    if item.get("success") and item.get("bufferPostId"):
                        results[item["id"]] = item
        except Exception as e:
            print(f"Note: Could not parse existing report: {e}")

    print(f"Loaded {len(results)} previously scheduled posts from report.")

    daily_limit_hit = False

    for idx, post in enumerate(posts_data, 1):
        post_id_num = post["id"]
        if post_id_num in results and results[post_id_num].get("success"):
            print(f"[{idx}/42] Post #{post_id_num} already scheduled (Buffer ID: {results[post_id_num]['bufferPostId']}). Skipping.")
            continue

        while True:
            print(f"[{idx}/42] Scheduling: Post #{post['id']} ({post['slot']}) - {post['dueAt']}...")
            resp = schedule_post(post)

            # Check for 429 rate limit
            if resp.get("status_code") == 429 or "429" in str(resp.get("error", "")):
                wait_sec = resp.get("retry_after", 60)
                if wait_sec > 900:
                    print(f"   [DAILY 24H LIMIT] Buffer 24-hour daily limit reached. Reset in {wait_sec}s.")
                    print(f"   [AUTONOMOUS PERSISTENCE] Persisting queue state to report for background timer catchup.")
                    daily_limit_hit = True
                    break
                print(f"   [RATE LIMIT] HTTP 429 encountered. Buffer cooldown: sleeping {wait_sec + 5} seconds...")
                time.sleep(wait_sec + 5)
                print(f"   [RESUMING] Retrying Post #{post['id']} now...")
                continue

            create_post_data = resp.get("data", {}).get("createPost", {})
            typename = create_post_data.get("__typename")
            post_obj = create_post_data.get("post")

            if typename == "PostActionSuccess" and post_obj and post_obj.get("id"):
                b_id = post_obj["id"]
                status = post_obj.get("status")
                due_at = post_obj.get("dueAt")
                print(f"   --> SUCCESS! Post ID: {b_id} | Status: {status} | Due: {due_at}")
                results[post_id_num] = {
                    "id": post["id"],
                    "slot": post["slot"],
                    "dueAt": post["dueAt"],
                    "bufferPostId": b_id,
                    "status": status,
                    "assetUrl": post["assetUrl"],
                    "cta": post["cta"],
                    "success": True
                }
                break
            else:
                err_msg = create_post_data.get("message") or resp.get("errors") or resp.get("error") or str(resp)
                print(f"   --> FAILED: {err_msg}")
                results[post_id_num] = {
                    "id": post["id"],
                    "slot": post["slot"],
                    "dueAt": post["dueAt"],
                    "error": str(err_msg),
                    "success": False
                }
                break

        # Save checkpoint after each post
        ordered_results = [results[p["id"]] for p in posts_data if p["id"] in results]
        successful_count = sum(1 for r in ordered_results if r.get("success"))
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump({
                "campaign": "Behind the Champion - Parents Set 2",
                "total_posts": len(posts_data),
                "successful_posts": successful_count,
                "daily_limit_hit": daily_limit_hit,
                "channelId": CHANNEL_ID,
                "scheduled_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "results": ordered_results
            }, f, indent=2)

        if daily_limit_hit:
            print("   [AUTONOMOUS HANDOFF] Stopping execution loop for background timer catchup.")
            break

        time.sleep(1.0)

    ordered_results = [results[p["id"]] for p in posts_data if p["id"] in results]
    successful_count = sum(1 for r in ordered_results if r.get("success"))
    print("-" * 60)
    print(f"Parents Set 2 Campaign Scheduling Complete: {successful_count}/42 posts placed into Buffer Scheduled Queue.")
    print(f"Report updated at {report_path}")

if __name__ == "__main__":
    main()
